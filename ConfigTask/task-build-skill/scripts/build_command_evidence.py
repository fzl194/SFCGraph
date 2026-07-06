"""为每个命令(atom)生成结构化证据包 MD。

每包含：
  ① atom + atom-挂 rule/DP（已抽 yaml 原文）
  ② 命令真相（mml_commands.jsonl：功能/参数表原文/notes/解析后真相 + 原始 md 路径）
  ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文片段）：
       - 数据规划表中该命令的参数行（参数/取值样例/获取方法/说明）
       - 操作步骤中该命令的上下文（±2 行原文）
       - 任务示例脚本中该命令的代码行
  ④ 自动比对（已绑 vs 命令真相 vs 特性实际用法）

输出：assert/{nf}/{version}/command-evidence/{atom-short}.md
用法：python build_command_evidence.py [nf] [version] [--only 0-00001]
"""
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("需要 pyyaml")

ROOT = Path(__file__).resolve().parents[2]
NF = sys.argv[1] if len(sys.argv) > 1 else "UDG"
VER = sys.argv[2] if len(sys.argv) > 2 else "20.15.2"
ONLY = sys.argv[4] if len(sys.argv) > 4 and sys.argv[3] == "--only" else None
A = ROOT / "assert" / NF / VER
CG = ROOT.parent / "CommandGraph" / "data" / "assets" / NF / VER
DOC_ROOT = ROOT.parent / "output" / f"{NF}_Product_Documentation_CH_{VER}"
GUIDE_ROOT = DOC_ROOT / "特性部署" / "特性指南" / f"{NF}特性指南"


def short(ref):
    return ref.split("@")[-1] if ref else ""


def load_yaml_dir(d):
    out = []
    if d.exists():
        for p in sorted(d.glob("*.yaml")):
            try:
                out.append(yaml.safe_load(p.read_text(encoding="utf-8")) or {})
            except Exception:
                pass
    return out


def parse_param_table(pd_text):
    ds_map = {"全网规划": "global_planned", "本端规划": "local_planned",
              "与对端协商": "peer_planned", "和对端协商": "peer_planned",
              "已配置数据中获取": "reference", "已配置中获取": "reference"}
    params = {}
    for line in (pd_text or "").splitlines():
        line = line.strip()
        if not line.startswith("|") or "参数标识" in line:
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) < 3:
            continue
        name, desc, detail = cells[0], cells[1], cells[2]
        if not name or set(name) <= set("-: "):
            continue
        ds = ""
        m = re.search(r"数据来源：([^\s<，,。；;]+)", detail)
        if m:
            ds = ds_map.get(m.group(1).strip(), m.group(1).strip())
        req = ""
        m2 = re.search(r"可选必选说明：([^\s<，,。；;]+)", detail)
        if m2:
            v = m2.group(1).strip()
            req = "conditional" if "条件" in v else "required" if "必选" in v else "optional" if "可选" in v else v
        mvr = re.search(r"取值范围：(.+?)(?:<br>|$)", detail)
        mdf = re.search(r"默认值：(.+?)(?:<br>|$)", detail)
        params[name] = {"desc": desc, "data_source": ds, "requiredness": req,
                        "value_range": (mvr.group(1).strip()[:100] if mvr else ""),
                        "default": (mdf.group(1).strip()[:40] if mdf else "")}
    return params


# md 文件名 → 全路径（特性激活 md 在 UDG特性指南/ 下，文件名带唯一 hash）
_MD_NAME_MAP = None
def md_path_by_evidence(ev_id):
    """ev_id 形如 'GWFD-020301/部署UPF_28493406.md' 或 'output/.../xxx.md' → 解析成全路径。"""
    global _MD_NAME_MAP
    fname = Path(ev_id).name
    if ev_id.startswith("output/") or ev_id.startswith("output\\"):
        return ROOT.parent / ev_id
    # 特性激活 md：按文件名在 GUIDE_ROOT 下找
    if _MD_NAME_MAP is None:
        _MD_NAME_MAP = {}
        if GUIDE_ROOT.exists():
            for p in GUIDE_ROOT.rglob("*.md"):
                _MD_NAME_MAP[p.name] = p
    return _MD_NAME_MAP.get(fname)


def extract_command_from_md(md_text, command_name):
    """从特性激活 md 抽取该命令的配置范式：数据规划表行 + 操作步骤上下文 + 任务示例脚本行。
    用词边界精确匹配 command_name，避免 ADD URR 误匹配 ADD URRGROUP。"""
    pat = re.compile(r"\b" + re.escape(command_name) + r"\b")
    lines = md_text.splitlines()
    data_rows, step_ctx, script_lines = [], [], []
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith("|"):
            cells = [c.strip() for c in s.split("|")[1:-1]]
            # 首 cell 去掉 markdown 标记(**、链接[]) 后精确含命令
            if cells and pat.search(re.sub(r"[*\[\]\(\)]", "", cells[0])):
                data_rows.append(s)
        elif pat.search(line):
            lo, hi = max(0, i - 2), min(len(lines), i + 3)
            step_ctx.append({"lineno": i + 1, "excerpt": lines[lo:hi]})
    in_code = False
    for line in lines:
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code and pat.search(line):
            script_lines.append(line.strip())
    return {"data_rows": data_rows, "step_context": step_ctx, "script_lines": script_lines}


def main():
    # ① atom + 特性
    tasks = {}
    for d in load_yaml_dir(A / "tasks"):
        if d.get("task_id"):
            tasks[d["task_id"]] = d
    atoms = {t: d for t, d in tasks.items() if d.get("task_layer") == "atom"}
    features = {t: d for t, d in tasks.items() if d.get("task_layer") == "feature"}

    rules_by_owner, dps_by_owner = {}, {}
    for r in load_yaml_dir(A / "task_rules"):
        rules_by_owner.setdefault(r.get("owner_task_ref", ""), []).append(r)
    for dp in load_yaml_dir(A / "decision_points"):
        dps_by_owner.setdefault(dp.get("owner_task_ref", ""), []).append(dp)

    cmd_truth = {}
    for line in (CG / "mml_commands.jsonl").read_text(encoding="utf-8").splitlines():
        try:
            d = json.loads(line)
            cmd_truth[d.get("command_name", "")] = d
        except Exception:
            pass

    atom_usage = json.loads((A / "index.json").read_text(encoding="utf-8")).get("atom_usage", {})

    out_dir = A / "command-evidence"
    out_dir.mkdir(exist_ok=True)

    n = 0
    for atom_id, atom in atoms.items():
        ash = short(atom_id)
        if ONLY and ash != ONLY:
            continue
        cmd_name = ""
        if "@MMLCommand@" in atom.get("ref", ""):
            cmd_name = atom["ref"].split("@MMLCommand@", 1)[1]
        truth = cmd_truth.get(cmd_name, {})
        truth_params = parse_param_table(truth.get("parameter_description", ""))

        bound = []
        for b in (atom.get("parameter_bindings") or []):
            bound.append({"param": (b.get("parameter_ref", "").split(":")[-1] if ":" in b.get("parameter_ref", "") else short(b.get("parameter_ref", ""))),
                          "binding_type": b.get("binding_type", ""), "variable_source": b.get("variable_source", ""),
                          "requiredness": b.get("requiredness", ""), "decision_ref": short(b.get("decision_ref", ""))})
        bound_names = {b["param"] for b in bound}
        missing = [p for p in truth_params if p not in bound_names]

        # ③ 各特性配置范式
        feat_ev = []
        for fid in atom_usage.get(atom_id, []):
            ft = features.get(fid, {})
            fshort = short(fid)
            fref = (ft.get("ref", "").split("@Feature@")[-1] if "@Feature@" in ft.get("ref", "") else "")
            fname = ft.get("task_logical_name", "")
            per_md = []
            for ev in (ft.get("source_evidence_ids") or []):
                mp = md_path_by_evidence(ev)
                if not mp or not mp.exists():
                    continue
                ext = extract_command_from_md(mp.read_text(encoding="utf-8"), cmd_name)
                if ext["data_rows"] or ext["script_lines"] or ext["step_context"]:
                    per_md.append({"md": ev, "extract": ext})
            if per_md:
                feat_ev.append({"feature": fshort, "feature_ref": fref, "name": fname, "per_md": per_md})

        # 组装 MD
        md = []
        md.append(f"# 命令审查证据包：{cmd_name}（atom {ash}）\n")
        md.append(f"> 原始命令 md：`{truth.get('source_evidence_ids',[''])[0]}`\n")
        md.append(f"> atom status：{atom.get('status','')} | 用该命令的特性数：{len(feat_ev)}\n\n")

        md.append("## ① atom + atom-挂 rule/DP（已抽 yaml）\n")
        md.append("```yaml\n" + yaml.safe_dump(atom, allow_unicode=True, sort_keys=False).strip() + "\n```\n")
        for r in rules_by_owner.get(atom_id, []):
            md.append(f"**rule {short(r.get('rule_id',''))}** ({r.get('rule_type','')}) {r.get('rule_name','')}\n")
            md.append("```yaml\n" + yaml.safe_dump(r, allow_unicode=True, sort_keys=False).strip() + "\n```\n")
        for dp in dps_by_owner.get(atom_id, []):
            md.append(f"**DP {short(dp.get('decision_id',''))}** ({dp.get('decision_type','')}) {dp.get('decision_name','')}\n")
            md.append("```yaml\n" + yaml.safe_dump(dp, allow_unicode=True, sort_keys=False).strip() + "\n```\n")

        md.append("## ② 命令真相（mml_commands.jsonl，= 命令原始 md 的结构化产物）\n")
        md.append(f"**功能**：{truth.get('command_function','')[:200]}\n")
        md.append(f"**notes（规格/上限→应投影 atom rule）**：\n" + "\n".join(f"- {x[:200]}" for x in truth.get("notes", [])) + "\n\n")
        md.append("**参数真相表（代码解析）**：\n\n| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |\n|---|---|---|---|---|---|\n")
        for p, t in truth_params.items():
            md.append(f"| {p} | {t['desc']} | {t['data_source']} | {t['requiredness']} | {t['default']} | {t['value_range'][:50]} |\n")
        md.append("\n")

        md.append("## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）\n")
        if not feat_ev:
            md.append("（无特性激活 md 含该命令的配置范式——可能经 compound 间接用）\n")
        for fe in feat_ev:
            md.append(f"\n### {fe['feature']} ({fe['feature_ref']}) {fe['name']}\n")
            for pm in fe["per_md"]:
                md.append(f"\n**md：`{pm['md']}`**\n")
                ex = pm["extract"]
                if ex["data_rows"]:
                    md.append("- 数据规划表（该命令的参数行）：\n")
                    for r in ex["data_rows"]:
                        md.append(f"  {r}\n")
                if ex["script_lines"]:
                    md.append("- 任务示例脚本（该命令行）：\n")
                    for s in ex["script_lines"]:
                        md.append(f"  `{s}`\n")
                if ex["step_context"]:
                    md.append("- 操作步骤上下文（±2 行原文）：\n")
                    for sc in ex["step_context"][:3]:
                        md.append(f"  L{sc['lineno']}:\n")
                        for ln in sc["excerpt"]:
                            md.append(f"    > {ln}\n")
        md.append("\n")

        md.append("## ④ 自动比对（供审查参考）\n")
        md.append(f"- atom 已绑参数：{sorted(bound_names)}\n")
        md.append(f"- 命令真相参数：{sorted(truth_params.keys())}\n")
        md.append(f"- 缺口（真相有、atom 未绑）：{missing}\n")
        # 跨特性 variable_source 分叉提示
        sources = {}
        for fe in feat_ev:
            for pm in fe["per_md"]:
                for r in pm["extract"]["data_rows"]:
                    cells = [c.strip() for c in r.split("|")[1:-1]]
                    if len(cells) >= 4:
                        src = cells[3]
                        sources.setdefault(src, 0)
                        sources[src] += 1
        if sources:
            md.append(f'- 各特性数据规划表"获取方法"列分布：{sources}（若多值→atom 应考虑 decision_driven）\n')

        (out_dir / f"{ash}.md").write_text("".join(md), encoding="utf-8")
        n += 1
    print(f"生成 {n} 个命令证据包 → {out_dir}")


if __name__ == "__main__":
    main()
