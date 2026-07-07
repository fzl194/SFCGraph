"""为每个命令生成结构化证据包 MD（支持 UDG post-build / UNC pre-build 两种模式）。

每包含：
  ① atom + atom-挂 rule/DP（已抽 yaml 原文）—— 仅 post-build 模式（命令已有 atom）
  ② 命令真相（mml_commands.jsonl：功能/参数表原文/notes/解析后真相 + 原始 md 路径）
  ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文片段）：
       - 数据规划表中该命令的参数行（参数/取值样例/获取方法/说明）
       - 操作步骤中该命令的上下文（±2 行原文）
       - 任务示例脚本中该命令的代码行
  ④ 自动比对（已绑 vs 命令真相 vs 特性实际用法；pre-build 模式无"已绑"，只给真相+范式+source 分布）

两种模式：
  - post-build（默认）：遍历 assert/{nf}/{ver}/tasks/ 里的 atom，逐 atom 出证据（含 ①）。
  - pre-build（--cmds <file>）：遍历命令清单文件（每行一条命令），逐命令出证据（无 ①，
    ③ 扫该 NF 全部特性 md）。用于 UNC 这种 atom 还没建、要先汇集跨特性范式的场景。

输出：assert/{nf}/{version}/command-evidence/{stem}.md
  - post-build: {stem} = atom 短 id（如 0-00001）
  - pre-build:  {stem} = 命令名空格替成 _（如 ADD_URR）

用法：
  python build_command_evidence.py [nf] [version]                 # post-build，遍历 atom
  python build_command_evidence.py [nf] [version] --only 0-00001  # 只出一个 atom
  python build_command_evidence.py [nf] [version] --cmds <file>   # pre-build，遍历命令清单
"""
import csv
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("需要 pyyaml")

ROOT = Path(__file__).resolve().parents[2]              # ConfigTask/
NF = sys.argv[1] if len(sys.argv) > 1 else "UDG"
VER = sys.argv[2] if len(sys.argv) > 2 else "20.15.2"
ONLY = None
CMDS_FILE = None
_args = sys.argv[3:]
_i = 0
while _i < len(_args):
    if _args[_i] == "--only" and _i + 1 < len(_args):
        ONLY = _args[_i + 1]; _i += 2
    elif _args[_i] == "--cmds" and _i + 1 < len(_args):
        CMDS_FILE = _args[_i + 1]; _i += 2
    else:
        _i += 1

A = ROOT / "assert" / NF / VER
CG = ROOT.parent / "CommandGraph" / "data" / "assets" / NF / VER
FEATURE_CSV = ROOT.parent / "FeatureGraph" / "data" / "legacy" / f"{NF}_feature_files.csv"


def short(ref: str) -> str:
    return ref.split("@")[-1] if ref else ""


def load_yaml_dir(d: Path):
    out = []
    if d.exists():
        for p in sorted(d.glob("*.yaml")):
            try:
                out.append(yaml.safe_load(p.read_text(encoding="utf-8")) or {})
            except Exception:
                pass
    return out


def parse_param_table(pd_text: str):
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


# ---- md 定位（csv 驱动，UDG/UNC 统一） ----
_FEATURE_FILES = None      # {feature_id: [abs_path,...]}
_MD_NAME_MAP = None        # {filename: abs_path}


def load_feature_files():
    fmap = {}
    if FEATURE_CSV.exists():
        with FEATURE_CSV.open(encoding="utf-8-sig", newline="") as f:
            for r in csv.DictReader(f):
                fid = (r.get("feature_id") or "").strip()
                fp = (r.get("file_path") or "").strip()
                if fid and fp:
                    p = (ROOT.parent / fp).resolve()
                    if p.exists():
                        fmap.setdefault(fid, []).append(p)
    return fmap


def _ensure_md_index():
    global _FEATURE_FILES, _MD_NAME_MAP
    if _FEATURE_FILES is None:
        _FEATURE_FILES = load_feature_files()
        _MD_NAME_MAP = {}
        for fid, ps in _FEATURE_FILES.items():
            for p in ps:
                _MD_NAME_MAP[p.name] = p


def md_path_by_evidence(ev_id: str):
    """ev_id 形如 'GWFD-020301/部署UPF_28493406.md' 或 'output/.../xxx.md' → abs path。"""
    if ev_id.startswith("output/") or ev_id.startswith("output\\"):
        return ROOT.parent / ev_id
    _ensure_md_index()
    return _MD_NAME_MAP.get(Path(ev_id).name)


_text_cache = {}


def md_text(p: Path) -> str:
    if p not in _text_cache:
        _text_cache[p] = p.read_text(encoding="utf-8", errors="ignore")
    return _text_cache[p]


def extract_command_from_md(md_txt: str, command_name: str):
    """从特性激活 md 抽取该命令的配置范式：数据规划表行 + 操作步骤上下文 + 任务示例脚本行。
    用词边界精确匹配 command_name，避免 ADD URR 误匹配 ADD URRGROUP。"""
    pat = re.compile(r"\b" + re.escape(command_name) + r"\b")
    lines = md_txt.splitlines()
    data_rows, step_ctx, script_lines = [], [], []
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith("|"):
            cells = [c.strip() for c in s.split("|")[1:-1]]
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


def collect_feature_evidence(cmd_name: str, feature_files):
    """扫该 NF 全部特性 md，收集 cmd 的跨特性配置范式（单命令，post-build 用）。"""
    feat_ev = []
    for fid, mds in feature_files.items():
        per_md = []
        for mp in mds:
            ext = extract_command_from_md(md_text(mp), cmd_name)
            if ext["data_rows"] or ext["script_lines"] or ext["step_context"]:
                per_md.append({"md": f"{fid}/{mp.name}", "extract": ext})
        if per_md:
            feat_ev.append({"feature": fid, "per_md": per_md})
    return feat_ev


def collect_all_evidence(commands, feature_files):
    """单遍扫描：每个 md 只读一次，合并正则找出命中的命令，只对命中的提取。
    返回 {command: feat_ev}，feat_ev 结构同 collect_feature_evidence（按特性分组，含 per_md）。"""
    cmd_set = set(commands)
    combined = re.compile(r"\b(" + "|".join(re.escape(c) for c in commands) + r")\b")
    grouped = {c: {} for c in commands}   # {cmd: {fid: [per_md entries]}}
    for fid, mds in feature_files.items():
        for mp in mds:
            txt = md_text(mp)
            found = set(combined.findall(txt)) & cmd_set
            if not found:
                continue
            for cmd in found:
                ext = extract_command_from_md(txt, cmd)
                if ext["data_rows"] or ext["script_lines"] or ext["step_context"]:
                    grouped[cmd].setdefault(fid, []).append({"md": f"{fid}/{mp.name}", "extract": ext})
    return {c: [{"feature": fid, "per_md": entries} for fid, entries in d.items()] for c, d in grouped.items()}


def source_distribution(feat_ev):
    sources = {}
    for fe in feat_ev:
        for pm in fe["per_md"]:
            for r in pm["extract"]["data_rows"]:
                cells = [c.strip() for c in r.split("|")[1:-1]]
                if len(cells) >= 4:
                    sources.setdefault(cells[3], 0)
                    sources[cells[3]] += 1
    return sources


def render_evidence(cmd_name, atom, rules, dps, truth, truth_params, feat_ev, bound_names):
    md = []
    ash = short(atom.get("task_id", "")) if atom else cmd_name.replace(" ", "_")
    md.append(f"# 命令证据包：{cmd_name}" + (f"（atom {ash}）\n" if atom else "\n"))
    md.append(f"> 原始命令 md：`{(truth.get('source_evidence_ids') or [''])[0]}`\n")
    md.append(f"> {'atom status：'+atom.get('status','')+' | ' if atom else ''}用该命令的特性数：{len(feat_ev)}\n\n")

    if atom:
        md.append("## ① atom + atom-挂 rule/DP（已抽 yaml）\n")
        md.append("```yaml\n" + yaml.safe_dump(atom, allow_unicode=True, sort_keys=False).strip() + "\n```\n")
        for r in rules:
            md.append(f"**rule {short(r.get('rule_id',''))}** ({r.get('rule_type','')}) {r.get('rule_name','')}\n")
            md.append("```yaml\n" + yaml.safe_dump(r, allow_unicode=True, sort_keys=False).strip() + "\n```\n")
        for dp in dps:
            md.append(f"**DP {short(dp.get('decision_id',''))}** ({dp.get('decision_type','')}) {dp.get('decision_name','')}\n")
            md.append("```yaml\n" + yaml.safe_dump(dp, allow_unicode=True, sort_keys=False).strip() + "\n```\n")

    md.append("## ② 命令真相（mml_commands.jsonl）\n")
    md.append(f"**功能**：{(truth.get('command_function') or '')[:200]}\n")
    notes = truth.get("notes", [])
    md.append("**notes（规格/上限→应投影 atom rule）**：\n" + ("\n".join(f"- {x[:200]}" for x in notes) if notes else "- （无）") + "\n\n")
    md.append("**参数真相表（代码解析）**：\n\n| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |\n|---|---|---|---|---|---|\n")
    for p, t in truth_params.items():
        md.append(f"| {p} | {t['desc']} | {t['data_source']} | {t['requiredness']} | {t['default']} | {t['value_range'][:50]} |\n")
    md.append("\n")

    md.append("## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）\n")
    if not feat_ev:
        md.append("（无特性激活 md 含该命令的配置范式——可能经 compound 间接用，或属网络前置/非本 NF 配置类）\n")
    for fe in feat_ev:
        md.append(f"\n### {fe['feature']}\n")
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

    md.append("## ④ 自动比对\n")
    if bound_names is not None:
        missing = [p for p in truth_params if p not in bound_names]
        md.append(f"- atom 已绑参数：{sorted(bound_names)}\n")
        md.append(f"- 命令真相参数：{sorted(truth_params.keys())}\n")
        md.append(f"- 缺口（真相有、atom 未绑）：{missing}\n")
    else:
        md.append(f"- 命令真相参数（{len(truth_params)}）：{sorted(truth_params.keys())}\n")
        md.append("- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集\n")
    sd = source_distribution(feat_ev)
    if sd:
        md.append(f'- 各特性数据规划表"获取方法"列分布：{sd}（多值→atom 应考虑 decision_driven）\n')
    return ash, "".join(md)


def main():
    _ensure_md_index()
    feature_files = _FEATURE_FILES

    cmd_truth = {}
    cg_file = CG / "mml_commands.jsonl"
    if cg_file.exists():
        for line in cg_file.read_text(encoding="utf-8").splitlines():
            try:
                d = json.loads(line)
                cmd_truth[d.get("command_name", "")] = d
            except Exception:
                pass

    rules_by_owner, dps_by_owner = {}, {}
    for r in load_yaml_dir(A / "task_rules"):
        rules_by_owner.setdefault(r.get("owner_task_ref", ""), []).append(r)
    for dp in load_yaml_dir(A / "decision_points"):
        dps_by_owner.setdefault(dp.get("owner_task_ref", ""), []).append(dp)

    out_dir = A / "command-evidence"
    out_dir.mkdir(exist_ok=True)
    n = 0

    if CMDS_FILE:
        cmds_file = Path(CMDS_FILE)
        if not cmds_file.is_absolute():
            cmds_file = (ROOT / cmds_file).resolve() if (ROOT / cmds_file).exists() else cmds_file.resolve()
        commands = [l.strip() for l in cmds_file.read_text(encoding="utf-8").splitlines()
                    if l.strip() and not l.strip().startswith("#")]
        n_md = sum(len(v) for v in feature_files.values())
        print(f"pre-build 模式：{len(commands)} 条命令，单遍扫 {n_md} 个特性 md")
        all_ev = collect_all_evidence(commands, feature_files)
        for cmd in commands:
            truth = cmd_truth.get(cmd, {})
            if not truth:
                print(f"  [SKIP] {cmd}：CommandGraph 无此命令")
                continue
            truth_params = parse_param_table(truth.get("parameter_description", ""))
            ash, content = render_evidence(cmd, None, [], [], truth, truth_params, all_ev.get(cmd, []), None)
            (out_dir / f"{ash}.md").write_text(content, encoding="utf-8")
            n += 1
        # 命令命中分布
        hit = {c: len(all_ev.get(c, [])) for c in commands if all_ev.get(c)}
        print(f"生成 {n} 个命令证据包（pre-build）→ {out_dir}")
        print(f"其中有特性范式命中的命令：{len(hit)}；无命中（命令不在任何特性激活 md）的：{n - len(hit)}")
        return

    # post-build 模式：遍历 atom
    tasks = {}
    for d in load_yaml_dir(A / "tasks"):
        if d.get("task_id"):
            tasks[d["task_id"]] = d
    atoms = {t: d for t, d in tasks.items() if d.get("task_layer") == "atom"}
    features = {t: d for t, d in tasks.items() if d.get("task_layer") == "feature"}
    atom_usage = {}
    idx = A / "index.json"
    if idx.exists():
        atom_usage = json.loads(idx.read_text(encoding="utf-8")).get("atom_usage", {})

    for atom_id, atom in atoms.items():
        ash = short(atom_id)
        if ONLY and ash != ONLY:
            continue
        cmd_name = atom["ref"].split("@MMLCommand@", 1)[1] if "@MMLCommand@" in atom.get("ref", "") else ""
        truth = cmd_truth.get(cmd_name, {})
        truth_params = parse_param_table(truth.get("parameter_description", ""))
        bound_names = {((b.get("parameter_ref", "").split(":")[-1]) if ":" in b.get("parameter_ref", "") else short(b.get("parameter_ref", "")))
                       for b in (atom.get("parameter_bindings") or [])}
        # ③ 优先用 atom_usage 指向的特性 source_evidence；若无则全扫
        feat_ev = []
        using = atom_usage.get(atom_id, [])
        if using:
            for fid in using:
                ft = features.get(fid, {})
                per_md = []
                for ev in (ft.get("source_evidence_ids") or []):
                    mp = md_path_by_evidence(ev)
                    if not mp or not mp.exists():
                        continue
                    ext = extract_command_from_md(md_text(mp), cmd_name)
                    if ext["data_rows"] or ext["script_lines"] or ext["step_context"]:
                        per_md.append({"md": ev, "extract": ext})
                if per_md:
                    feat_ev.append({"feature": fid, "per_md": per_md})
        else:
            feat_ev = collect_feature_evidence(cmd_name, feature_files)
        ash2, content = render_evidence(cmd_name, atom, rules_by_owner.get(atom_id, []),
                                         dps_by_owner.get(atom_id, []), truth, truth_params, feat_ev, bound_names)
        (out_dir / f"{ash}.md").write_text(content, encoding="utf-8")
        n += 1
    print(f"生成 {n} 个命令证据包（post-build）→ {out_dir}")


if __name__ == "__main__":
    main()
