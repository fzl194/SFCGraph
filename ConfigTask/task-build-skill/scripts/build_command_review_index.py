"""命令级审查预处理：为每个 atom(命令) 产出一个"审查卡"，汇总三输入 + 自动比对参数缺口。

输入三源：
  ① 已抽 yaml：atom task + atom 挂的 rule/DP（owner_task_ref = 该 atom）
  ② 命令证据 md：用该命令的各特性的激活/配置 md（index.atom_usage 反查 + 特性 source_evidence_ids）
  ③ 命令原始 md + 参数真相：mml_commands.jsonl（source_evidence_ids 指原始 md；parameter_description 含数据来源/必选可选/取值范围）

产出：assert/{nf}/{version}/command-review-index.json
  key = atom 短 id（如 0-00001），value = 审查卡（见 assemble_card）

用法：python build_command_review_index.py [nf] [version]   （默认 UDG 20.15.2）
"""
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("需要 pyyaml")

ROOT = Path(__file__).resolve().parents[2]          # ConfigTask/
NF = sys.argv[1] if len(sys.argv) > 1 else "UDG"
VER = sys.argv[2] if len(sys.argv) > 2 else "20.15.2"
A = ROOT / "assert" / NF / VER
CG = ROOT.parent / "CommandGraph" / "data" / "assets" / NF / VER


def short(ref):
    return ref.split("@")[-1] if ref else ""


def load_yaml_dir(d):
    out = {}
    if not d.exists():
        return out
    for p in sorted(d.glob("*.yaml")):
        try:
            doc = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        except Exception as e:
            doc = {"_error": str(e)}
        if doc.get("task_id") or doc.get("rule_id") or doc.get("decision_id"):
            out[p.name] = doc
    return out


def parse_param_table(pd_text):
    """把 mml_commands.parameter_description 的 markdown 表精确解析为 per-param 真相。
    行格式：| 参数标识 | 参数描述 | 可选必选说明：X参数<br>参数含义：...<br>数据来源：Y<br>取值范围：...<br>默认值：... |"""
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
            if "条件" in v:
                req = "conditional"
            elif "必选" in v:
                req = "required"
            elif "可选" in v:
                req = "optional"
            else:
                req = v
        val_range = ""
        m3 = re.search(r"取值范围：(.+?)(?:<br>|$)", detail)
        if m3:
            val_range = m3.group(1).strip()[:100]
        default = ""
        m4 = re.search(r"默认值：(.+?)(?:<br>|$)", detail)
        if m4:
            default = m4.group(1).strip()[:40]
        params[name] = {"desc": desc, "data_source": ds, "requiredness": req,
                        "value_range": val_range, "default": default}
    return params


def main():
    # ① atom + 特性 task
    tasks = load_yaml_dir(A / "tasks")
    atoms, features = {}, {}
    for doc in tasks.values():
        layer = doc.get("task_layer")
        tid = doc.get("task_id", "")
        if layer == "atom":
            atoms[tid] = doc
        elif layer == "feature":
            features[tid] = doc

    # ① atom 挂的 rule/DP（owner_task_ref = atom）
    rules_by_owner, dps_by_owner = {}, {}
    for doc in load_yaml_dir(A / "task_rules").values():
        rules_by_owner.setdefault(doc.get("owner_task_ref", ""), []).append(doc)
    for doc in load_yaml_dir(A / "decision_points").values():
        dps_by_owner.setdefault(doc.get("owner_task_ref", ""), []).append(doc)

    # ③ mml_commands 真相
    cmd_truth = {}
    mml_f = CG / "mml_commands.jsonl"
    if mml_f.exists():
        for line in mml_f.read_text(encoding="utf-8").splitlines():
            try:
                d = json.loads(line)
            except Exception:
                continue
            cmd_truth[d.get("command_name", "")] = d

    # ② atom_usage（命令 → 用它的特性）
    idx_f = A / "index.json"
    atom_usage = {}
    if idx_f.exists():
        idx = json.loads(idx_f.read_text(encoding="utf-8"))
        atom_usage = idx.get("atom_usage", {})

    cards = {}
    stat = {"with_truth": 0, "missing_truth": 0, "param_gaps": 0}
    for atom_id, atom in atoms.items():
        cmd_name = ""
        ref = atom.get("ref", "")
        if "@MMLCommand@" in ref:
            cmd_name = ref.split("@MMLCommand@", 1)[1]
        truth = cmd_truth.get(cmd_name, {})
        truth_params = parse_param_table(truth.get("parameter_description", ""))

        bound = []
        for b in (atom.get("parameter_bindings") or []):
            pref = b.get("parameter_ref", "")
            p = pref.split(":")[-1] if ":" in pref else short(pref)
            bound.append({
                "param": p,
                "binding_type": b.get("binding_type", ""),
                "variable_source": b.get("variable_source", ""),
                "requiredness": b.get("requiredness", ""),
                "decision_ref": short(b.get("decision_ref", "")),
            })
        bound_names = {b["param"] for b in bound}

        # 参数缺口：命令真相里有、atom 没绑的（标"通用配置"判定用，不强制全绑）
        missing = []
        for pname, ptruth in truth_params.items():
            if pname not in bound_names:
                missing.append({"param": pname, **ptruth})
        if missing:
            stat["param_gaps"] += 1

        if truth:
            stat["with_truth"] += 1
        else:
            stat["missing_truth"] += 1

        # ② 命令证据：用该命令的各特性 + 其 md
        using = atom_usage.get(atom_id, [])
        feat_ev = []
        for fid in using:
            ft = features.get(fid, {})
            feat_ev.append({
                "feature_task": short(fid),
                "feature_ref": (ft.get("ref", "").split("@Feature@")[-1] if "@Feature@" in ft.get("ref", "") else ""),
                "feature_name": ft.get("task_logical_name", ""),
                "evidence_mds": ft.get("source_evidence_ids", []),
            })

        cards[short(atom_id)] = {
            "atom_id": atom_id,
            "command_name": cmd_name,
            "command_name_zh": truth.get("command_name_zh", atom.get("task_logical_name", "")),
            "command_function": truth.get("command_function", ""),
            "original_md": (truth.get("source_evidence_ids") or [None])[0],
            "command_notes": truth.get("notes", []),  # 规格/唯一性/上限 → 应投影成 atom rule
            "atom_status": atom.get("status", ""),
            "atom_source_evidence": atom.get("source_evidence_ids", []),
            "atom_owned_rules": [{"rule_id": short(r.get("rule_id", "")), "rule_type": r.get("rule_type", ""),
                                  "rule_name": r.get("rule_name", "")} for r in rules_by_owner.get(atom_id, [])],
            "atom_owned_dps": [{"decision_id": short(d.get("decision_id", "")), "decision_name": d.get("decision_name", ""),
                                "decision_type": d.get("decision_type", "")} for d in dps_by_owner.get(atom_id, [])],
            "bound_params": bound,
            "truth_params": truth_params,
            "missing_params_in_atom": missing,
            "feature_evidence": feat_ev,
        }

    out = A / "command-review-index.json"
    out.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"命令级审查索引 → {out.relative_to(ROOT)}")
    print(f"  atom 总 {len(cards)} | 命中 mml_commands 真相 {stat['with_truth']} | 未命中 {stat['missing_truth']}")
    print(f"  有参数缺口（命令真相参数 > atom 已绑）的 atom: {stat['param_gaps']}")


if __name__ == "__main__":
    main()
