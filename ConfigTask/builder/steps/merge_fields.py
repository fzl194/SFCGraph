# ConfigTask/builder/steps/merge_fields.py
"""Step 4: Agent-2 合并确证 + ConfigTask 字段抽取。

每簇调一次 Agent，输入是 enrich 步内联进 member 的证据（step_text /
command_examples / param_rows），Agent 只做 LLM 推理，不再读任何 md。
产出：task_logical_name / task_goal / task_summary / commands+parameters+binding_type。
"""
import json
import re

from builder.steps.registry import step


def build_agent_input(cluster):
    """构造 Agent-2 输入：直接用 enrich 步内联进 member 的证据，不读 md。"""
    members_info = []
    for m in cluster["members"]:
        members_info.append({
            "candidate_id": m["candidate_id"],
            "feature_id": m["feature_id"],
            "candidate_desc": m.get("candidate_desc", ""),
            "commands": m["commands"],
            "step_text": m.get("step_text", ""),
            "command_examples": m.get("command_examples", []),
            "param_rows": m.get("param_rows", []),
        })

    return {
        "cluster_id": cluster["cluster_id"],
        "core_commands": cluster["core_commands"],
        "member_count": cluster["member_count"],
        "business_domains": cluster.get("business_domains", []),
        "members": members_info,
    }


def build_prompt(cluster_input):
    """构造 Agent-2 prompt（纯内联证据，无文件读取）。"""
    members_json = json.dumps(cluster_input["members"], ensure_ascii=False, indent=2)
    n = cluster_input["member_count"]
    domains = "/".join(cluster_input.get("business_domains", []))

    return f"""你是 ConfigTask 合并抽取 Agent。下面是一个 task 簇（{n} 个配置案例，业务域：{domains}）的内联证据，请确证合并并抽取 ConfigTask 字段。

【内联证据说明】（无需、也不要读任何文件）
每个 member 已携带三类证据：
- step_text：操作步骤里命中命令的描述（任务结构）
- command_examples：任务示例里的 MML 配置命令原文（含参数与实例取值，即"配置命令原文"）
- param_rows：数据规划表里命中命令的参数行，每行 {{command, param_code, sample, obtain_method, note}}。
  obtain_method 即"获取方法"（本端规划/全网规划/对端规划/与对端协商/已配置数据中获取），是 binding_type 的判定依据。

【你的任务】
1. 确认这 {n} 个 member 是否同一 task（命令集差异大 → 在 split_notes 说明应拆分）
2. 跨 member 聚合每条命令的参数，判定 binding_type

【binding_type 判定（以 param_rows.obtain_method + 跨案例是否变化为准）】
- "本端规划" → variable / local_planned
- "全网规划" → variable / global_planned
- "对端规划"/"与对端协商" → variable / peer_planned
- "已配置数据中获取"/"从已配置数据中获取" → reference（值来自本任务内其它命令刚创建的对象）
- 跨 member 取值或获取方法不同（如有的 OFFLINE 有的 ONLINE）→ variable / decision_driven
- 跨所有 member 稳定不变 → fixed + fixed_value
- parameter_ref 取 param_code（英文参数名）
- 不记实例取值（如 URRID=12500 不写）

【commands 范围】
只纳入这个 task 的核心命令；特性使能前置（如 SET LICENSESWITCH）和其它子任务命令不计入，放 split_notes。

【输出 JSON】（只输出 JSON，不要 markdown 包裹、不要解释文字）
{{
  "task_logical_name": "配置规则",
  "task_goal": "...",
  "task_summary": "...",
  "commands": [
    {{"command_ref": "ADD RULE", "parameters": [
      {{"parameter_ref": "RULENAME", "binding_type": "variable", "variable_source": "local_planned"}},
      {{"parameter_ref": "POLICYTYPE", "binding_type": "variable", "variable_source": "decision_driven"}},
      {{"parameter_ref": "FILTERINGMODE", "binding_type": "fixed", "fixed_value": "FLOWFILTER"}},
      {{"parameter_ref": "FLOWFILTERNAME", "binding_type": "reference"}}
    ]}}
  ],
  "decision_points": ["跨案例取值会分叉的参数及原因"],
  "split_notes": "前置/后续命令说明 / 是否应拆分的判断"
}}

【输入数据】
簇ID: {cluster_input["cluster_id"]}
核心命令: {cluster_input["core_commands"]}

{members_json}
"""


def parse_output(raw, cluster_id, nf, version, seq):
    """解析 Agent-2 输出文本 → ConfigTask 记录（dict）。失败返回 None。"""
    json_match = re.search(r'\{.*\}', raw, re.DOTALL)
    if not json_match:
        return None
    try:
        data = json.loads(json_match.group())
    except json.JSONDecodeError:
        return None
    return {
        "task_id": f"{nf}@{version}@ConfigTask@{seq+1:05d}",
        "cluster_id": cluster_id,
        "task_logical_name": data.get("task_logical_name", ""),
        "task_goal": data.get("task_goal", ""),
        "task_summary": data.get("task_summary", ""),
        "nf": nf,
        "version": version,
        "commands": data.get("commands", []),
        "decision_points": data.get("decision_points", []),   # 中间态，finalize_fields 加 _ 前缀
        "split_notes": data.get("split_notes", ""),           # 中间态
        "task_category": "配置",
        "status": "active",
        "extraction_method": "inline_enriched",
    }


@step("merge_fields", output_file="config_tasks.jsonl", agent=True)
def run(ctx):
    """prep → check → ingest。返回 int=完成数 / "PAUSE"=待回填。"""
    data_dir = ctx["data_dir"]
    nf, version = ctx["nf"], ctx["version"]
    prompts_dir = data_dir / "agent_prompts" / "merge_fields"
    outputs_dir = data_dir / "agent_outputs" / "merge_fields"
    prompts_dir.mkdir(parents=True, exist_ok=True)
    outputs_dir.mkdir(parents=True, exist_ok=True)

    # 读 enriched clusters
    clusters = []
    with open(data_dir / "task_clusters_enriched.jsonl", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                clusters.append(json.loads(line))

    # done = cluster_id 已在 config_tasks.jsonl（输出派生）
    out_path = data_dir / "config_tasks.jsonl"
    done_ids = set()
    if out_path.exists():
        with open(out_path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    done_ids.add(json.loads(line)["cluster_id"])

    rerun = ctx.get("rerun_target")
    pending = [c for c in clusters
               if c["cluster_id"] not in done_ids or (rerun and rerun in c["cluster_id"])]

    if not pending:
        print(f"  全部已完成 ({len(done_ids)}/{len(clusters)} 簇)")
        return len(done_ids)

    # 大簇优先（跨案例价值高）
    pending.sort(key=lambda c: -c["member_count"])

    # prep：每簇写 prompt（幂等）
    for c in pending:
        ai = build_agent_input(c)
        (prompts_dir / f"{c['cluster_id']}.txt").write_text(build_prompt(ai), encoding="utf-8")

    # check + ingest：输出齐了的簇回填
    seq = len(done_ids)
    ingested = 0
    still_pending = []
    with open(out_path, "a", encoding="utf-8") as f:
        for c in pending:
            cid = c["cluster_id"]
            out_file = outputs_dir / f"{cid}.json"
            if not out_file.exists():
                still_pending.append(cid)
                continue
            task = parse_output(out_file.read_text(encoding="utf-8"), cid, nf, version, seq)
            if task is None:
                still_pending.append(cid)  # 解析失败也算未完成
                continue
            f.write(json.dumps(task, ensure_ascii=False) + "\n")
            seq += 1
            ingested += 1

    if still_pending:
        print(f"  prep: {len(pending)} 簇 prompt 已就绪 → {prompts_dir}（大簇优先）")
        print(f"  已回填 {ingested} task；仍待处理 {len(still_pending)} 簇:")
        for cid in still_pending[:12]:
            print(f"    - {prompts_dir}/{cid}.txt  →  写输出到 {outputs_dir}/{cid}.json")
        if len(still_pending) > 12:
            print(f"    ... 等 {len(still_pending) - 12} 簇")
        return "PAUSE"

    print(f"  全部回填: {ingested} task（{len(pending)} 簇）")
    return ingested
