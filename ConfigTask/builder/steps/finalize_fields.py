# ConfigTask/builder/steps/finalize_fields.py
"""Step 4.5: ConfigTask 字段后处理（外网/当下可做的补齐）。

只补齐、不删信息（基本信息零丢失）。外网命令图谱只有 mml_commands 全集，
command_parameters / parameter_references 全集在内网——故：

本步补（外网 mml_commands 完整）：
- command_ref：裸名 → 全键 UDG@20.15.2@MMLCommand@<name>，校验存在；未知保留裸名（不臆造）
- source_evidence_ids：聚合 cluster member.doc_path（去重）——下一阶段读 md 的入口
- decision_points/split_notes → _decision_points/_split_notes（中间态加 _ 前缀，不污染权威 Schema）

留给内网程序（命令图谱参数表/依赖全集齐后）：
- parameter_ref 全键、source_ref（reference→源命令.参数、decision_driven→DecisionPoint）

幂等：已全键/已前缀则跳过，可重复运行。
"""
import json

from builder.steps.registry import step

_MML_TAG = "@MMLCommand@"


def _is_full_command_ref(ref: str) -> bool:
    return _MML_TAG in ref


def finalize_record(task, clusters_by_id, mml_names, nf, version):
    """就地补齐单个 ConfigTask 记录字段（只补不删）。

    Args:
        task: ConfigTask 记录（dict，就地修改）
        clusters_by_id: {cluster_id: cluster} 用于取 member.doc_path
        mml_names: 命令图谱 MMLCommand 名集合（校验 command_ref 用）
        nf, version: 网元/版本（构造全键）
    Returns:
        list[str]: 警告信息（未知命令等），空表表示无警告
    """
    warns = []

    # 1. command_ref 裸名 → 全键
    for cmd in task.get("commands", []):
        ref = cmd.get("command_ref", "")
        if not ref or _is_full_command_ref(ref):
            continue
        if ref in mml_names:
            cmd["command_ref"] = f"{nf}@{version}@MMLCommand@{ref}"
        else:
            warns.append(f"command_ref 未命中命令图谱，保留裸名: {ref}")
            # 不臆造，保留裸名

    # 2. source_evidence_ids：聚合 cluster member.doc_path（去重，保持顺序）
    if "source_evidence_ids" not in task:
        cluster = clusters_by_id.get(task.get("cluster_id"))
        docs = []
        seen = set()
        if cluster:
            for m in cluster.get("members", []):
                dp = m.get("doc_path")
                if dp and dp not in seen:
                    seen.add(dp)
                    docs.append(dp)
        task["source_evidence_ids"] = docs

    # 3. 中间态字段加 _ 前缀（幂等：已前缀则跳过）
    for raw, prefixed in (("decision_points", "_decision_points"),
                          ("split_notes", "_split_notes")):
        if raw in task and prefixed not in task:
            task[prefixed] = task.pop(raw)

    # parameter_ref / source_ref 不动 —— 留给内网程序
    return warns


def _load_mml_names(command_graph_dir):
    """从命令图谱 mml_commands.jsonl 加载命令名集合。文件缺失返回空集。"""
    if not command_graph_dir:
        return set()
    import pathlib
    p = pathlib.Path(command_graph_dir) / "mml_commands.jsonl"
    if not p.exists():
        return set()
    names = set()
    with open(p, encoding="utf-8") as f:
        for line in f:
            try:
                names.add(json.loads(line)["command_name"])
            except (json.JSONDecodeError, KeyError):
                continue
    return names


@step("finalize_fields")  # 后处理 pass：无独立输出文件（改 config_tasks.jsonl），始终运行不跳过
def run(ctx):
    data_dir = ctx["data_dir"]
    output_path = data_dir / "config_tasks.jsonl"
    nf, version = ctx["nf"], ctx["version"]

    if not output_path.exists():
        print("  跳过: config_tasks.jsonl 不存在（merge_fields 未产出）")
        return 0

    mml_names = _load_mml_names(ctx.get("command_graph_dir"))
    print(f"  命令图谱 MMLCommand: {len(mml_names)} 条")

    # 簇索引（取 member.doc_path）
    clusters_by_id = {}
    clusters_path = data_dir / "task_clusters.jsonl"
    if clusters_path.exists():
        with open(clusters_path, encoding="utf-8") as f:
            for line in f:
                cl = json.loads(line)
                clusters_by_id[cl["cluster_id"]] = cl

    # 读 config_tasks
    with open(output_path, encoding="utf-8") as f:
        tasks = [json.loads(line) for line in f]
    print(f"  输入: {len(tasks)} ConfigTask")

    all_warns = []
    for t in tasks:
        warns = finalize_record(t, clusters_by_id, mml_names, nf, version)
        all_warns.extend(warns)

    # 写回
    with open(output_path, "w", encoding="utf-8") as f:
        for t in tasks:
            f.write(json.dumps(t, ensure_ascii=False) + "\n")

    print(f"  补齐: command_ref 全键 + source_evidence_ids + _decision_points/_split_notes")
    if all_warns:
        print(f"  警告({len(all_warns)}):")
        for w in all_warns[:10]:
            print(f"    - {w}")
    return len(tasks)
