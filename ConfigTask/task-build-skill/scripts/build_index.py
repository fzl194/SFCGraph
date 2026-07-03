"""Task 资产只读索引生成器（不是构建 pipeline——只读现有 Agent 产出的 yaml，生成查询索引）。

每次 pass 末尾运行：python build_index.py [nf] [version]   （默认 UDG 20.15.2）
产出 task-assets/{nf}/{version}/index.json，供：
  - Agent 构建新特性前"快速查找已有 task"（命令→atom / 特性→tasks / atom→被谁用）
  - 审查 UI 渲染与检索
"""
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("需要 pyyaml")

ROOT = Path(__file__).resolve().parents[2]          # ConfigTask/
NF = sys.argv[1] if len(sys.argv) > 1 else "UDG"
VER = sys.argv[2] if len(sys.argv) > 2 else "20.15.2"
A = ROOT / "task-assets" / NF / VER


def short(ref):
    return ref.split("@")[-1] if ref else ""


def cmd_of(ref):
    """UDG@20.15.2@MMLCommand@ADD URR  ->  ADD URR"""
    if ref and "@MMLCommand@" in ref:
        return ref.split("@MMLCommand@", 1)[1]
    return ""


def feat_of(ref):
    if ref and "@Feature@" in ref:
        return ref.split("@Feature@", 1)[1]
    return ""


def build_compounds(tasks):
    """compound 登记表(spec §8.3)。compound short id → {compound_id, logical_name, phase, intent, command_set, features_using}。
    phase = logical_name(作受控相位词表);command_set 从 compound 的 task_relations 指向的 atom.ref 解析;
    features_using = 反查引用该 compound 的 feature/generalized task。"""
    tby = {short(t.get("task_id", "")): t for t in tasks if t.get("task_id")}
    # compound -> command_set
    cmd_sets = {}
    for t in tasks:
        if t.get("task_layer") != "compound":
            continue
        cid = short(t.get("task_id", ""))
        cs = set()
        for r in (t.get("task_relations") or []):
            for k in ("from_task_ref", "to_task_ref"):
                s = short(r.get(k, ""))
                at = tby.get(s)
                if at:
                    c = cmd_of(at.get("ref", ""))
                    if c:
                        cs.add(c)
        cmd_sets[cid] = cs
    # features_using 反查
    fu = {cid: set() for cid in cmd_sets}
    for t in tasks:
        if t.get("task_layer") not in ("feature", "generalized"):
            continue
        fshort = short(t.get("task_id", ""))
        for r in (t.get("task_relations") or []):
            for k in ("from_task_ref", "to_task_ref"):
                s = short(r.get(k, ""))
                if s in fu:
                    fu[s].add(fshort)
    compounds = {}
    for cid in sorted(cmd_sets):
        t = tby.get(cid, {})
        compounds[cid] = {
            "compound_id": cid,
            "logical_name": t.get("task_logical_name", ""),
            "phase": t.get("task_logical_name", ""),
            "intent": t.get("task_intent", ""),
            "command_set": sorted(cmd_sets[cid]),
            "features_using": sorted(fu[cid]),
        }
    return compounds


def load(d):
    out = []
    if d.exists():
        for p in sorted(d.glob("*.yaml")):
            try:
                out.append(yaml.safe_load(p.read_text(encoding="utf-8")) or {})
            except Exception as e:
                out.append({"task_id": p.stem, "_error": str(e)})
    return out


def main():
    tasks = load(A / "tasks")
    dps = load(A / "decision_points")
    rules = load(A / "task_rules")

    by_command = {}        # "ADD URR" -> atom task_id
    by_logical_name = {}   # logical_name -> task_id
    by_layer = {"atom": [], "compound": [], "feature": [], "solution": [], "generalized": []}
    compounds_atoms = {}   # compound_id -> [atom_ids]

    for t in tasks:
        tid = t.get("task_id", "")
        layer = t.get("task_layer", "")
        ln = t.get("task_logical_name", "")
        if layer == "atom":
            c = cmd_of(t.get("ref", ""))
            if c:
                by_command.setdefault(c, []).append(tid)
        if ln:
            by_logical_name.setdefault(ln, []).append(tid)
        if layer in by_layer:
            by_layer[layer].append(tid)
        if layer == "compound":
            atoms = []
            for r in (t.get("task_relations") or []):
                for ref in (r.get("from_task_ref"), r.get("to_task_ref")):
                    if ref and short(ref).startswith("0-"):
                        atoms.append(ref)
            compounds_atoms[tid] = sorted(set(atoms))

    # feature/generalized -> 直接 atom + 经 compound 的 atom；feature_id -> tasks
    by_feature = {}        # feature_id(如 GWFD-020301) -> {feature_task, compounds, atoms}
    atom_usage = {}        # atom_id -> [feature/generalized task_ids 使用它]
    for t in tasks:
        layer = t.get("task_layer", "")
        if layer not in ("feature", "generalized"):
            continue
        tid = t.get("task_id", "")
        used_atoms, used_compounds = set(), set()
        for r in (t.get("task_relations") or []):
            for ref in (r.get("from_task_ref"), r.get("to_task_ref")):
                if not ref:
                    continue
                s = short(ref)
                if s.startswith("0-"):
                    used_atoms.add(ref)
                elif s.startswith("1-"):
                    used_compounds.add(ref)
                    used_atoms |= set(compounds_atoms.get(ref, []))
        for a in used_atoms:
            atom_usage.setdefault(a, []).append(tid)
        fid = feat_of(t.get("ref", ""))
        if fid:
            by_feature.setdefault(fid, {"feature_task": None, "compounds": [], "atoms": []})
            if layer == "feature":
                by_feature[fid]["feature_task"] = tid
            by_feature[fid]["compounds"] = sorted(set(by_feature[fid]["compounds"] + list(used_compounds)))
            by_feature[fid]["atoms"] = sorted(set(by_feature[fid]["atoms"] + list(used_atoms)))

    # 挂载：每个 task 的 rule / dp
    rules_by_owner = {}
    for r in rules:
        rules_by_owner.setdefault(r.get("owner_task_ref", ""), []).append(r.get("rule_id", ""))
    dps_by_owner = {}
    for d in dps:
        dps_by_owner.setdefault(d.get("owner_task_ref", ""), []).append(d.get("decision_id", ""))

    summary = [{
        "task_id": short(t.get("task_id", "")),
        "layer": t.get("task_layer", ""),
        "logical_name": t.get("task_logical_name", ""),
        "ref": short(t.get("ref", "")) if t.get("ref") else "",
        "status": t.get("status", ""),
        "n_params": len(t.get("parameter_bindings") or []),
        "n_relations": len(t.get("task_relations") or []),
    } for t in tasks]

    compounds = build_compounds(tasks)

    index = {
        "nf_version": f"{NF}@{VER}",
        "generated_for": "Agent 构建前查找 + UI 渲染",
        "counts": {k: len(v) for k, v in by_layer.items()} | {"dp": len(dps), "rule": len(rules)},
        "by_command": by_command,            # 命令 -> atom（复用查找）
        "by_logical_name": by_logical_name,  # 语义名 -> task（合并查找）
        "by_feature": by_feature,            # 特性 -> 它的 feature task + 用到的 compound/atom
        "atom_usage": atom_usage,            # atom -> 谁在用（演进影响面）
        "compounds": compounds,              # compound -> 登记表条目(spec §8.3 复用查找 + canonical 词表)
        "rules_by_owner": {short(k): v for k, v in rules_by_owner.items()},
        "dps_by_owner": {short(k): v for k, v in dps_by_owner.items()},
        "tasks": summary,
    }
    out = A / "index.json"
    out.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")

    # 派生 canonical-compounds.md(人工可读登记表,spec §8.3)
    backbone = [(cid, e) for cid, e in compounds.items() if len(e["features_using"]) >= 5]
    specific = [(cid, e) for cid, e in compounds.items() if len(e["features_using"]) < 5]
    md = [f"# Canonical Compound 登记表 — {NF}@{VER}\n",
          "> 派生自 index.json compounds 段(spec §8.3)。Agent 复用查找用;人审通过的新 compound 自动入表(重跑 build_index.py 刷新)。\n",
          f"> compound 总数 {len(compounds)} | backbone(≥5 特性复用) {len(backbone)} | 专用 {len(specific)}\n\n"]
    md.append("## backbone(高频复用,≥5 特性)\n\n")
    for cid, e in sorted(backbone, key=lambda x: -len(x[1]["features_using"])):
        md.append(f"### {cid} {e['logical_name']}  (复用 {len(e['features_using'])} 特性)\n")
        md.append(f"- intent: {e['intent']}\n")
        md.append(f"- command_set: {', '.join(e['command_set'])}\n")
        md.append(f"- features_using: {', '.join(e['features_using'])}\n\n")
    md.append("## 专用(单/少特性,<5)\n\n")
    for cid, e in sorted(specific):
        md.append(f"### {cid} {e['logical_name']}  (复用 {len(e['features_using'])} 特性)\n")
        md.append(f"- intent: {e['intent']}\n")
        md.append(f"- command_set: {', '.join(e['command_set'])}\n")
        if e["features_using"]:
            md.append(f"- features_using: {', '.join(e['features_using'])}\n")
        md.append("\n")
    (A / "canonical-compounds.md").write_text("".join(md), encoding="utf-8")

    print(f"index.json 已生成：{out.relative_to(ROOT)}")
    print(f"  atom={len(by_layer['atom'])} compound={len(by_layer['compound'])} feature={len(by_layer['feature'])} generalized={len(by_layer['generalized'])}")
    print(f"  命令索引 {len(by_command)} 条，特性索引 {len(by_feature)} 条，compound 登记表 {len(compounds)} 条")
    print(f"  canonical-compounds.md 已生成(backbone {len(backbone)} / 专用 {len(specific)})")


if __name__ == "__main__":
    main()
