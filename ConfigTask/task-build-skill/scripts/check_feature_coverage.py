"""per-DP-分支覆盖校验(spec §4)—— compound/feature 抽取的硬闸。

每个 feature 抽取后,对其 variants.yaml 列出的每个 md 证实的配法变体 V,校验:
    active_commands(F, V) == md_required(F, V)
不等 → 报 缺/多;task_relations 出现 compound 环 → 报错回炉。

关键点(spec §4.1):
- 判定 key 在 impact 的 **target_type ∈ {task, command}**(不看 effect_type 名)。实测数据
  changes_command_set 0 用例,真实分叉多用 adds/excludes + target=task/command 表达。
- 结构基线 = feature 沿 task_relations(collect compound→atom + 直挂 atom)的命令集;
  DP impact target=task/command 的 adds/requires/changes_command_set → 加,excludes/skips → 减。
- variants.yaml 由 Agent 步骤①产出(只列 md 证实的变体 + 每变体的 md_required 命令集)——即"按 md 收口"。

用法:
    python check_feature_coverage.py <feature_task_short> [nf] [version]
    默认 nf=UDG version=20.15.2。exit 0=过 / 1=覆盖失败 / 2=缺输入。
"""
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("需要 pyyaml: pip install pyyaml")

ROOT = Path(__file__).resolve().parents[2]  # ConfigTask/

# effect_type → 命令集增删(仅在 target_type∈{task,command} 时生效)
ADD_EFFECTS = {"adds", "requires", "changes_command_set"}
REM_EFFECTS = {"skips", "excludes"}


def short(ref):
    return (ref or "").split("@")[-1] if ref else ""


def cmd_of(ref):
    if ref and "@MMLCommand@" in ref:
        return ref.split("@MMLCommand@", 1)[1]
    return ""


def feat_of(ref):
    if ref and "@Feature@" in ref:
        return ref.split("@Feature@", 1)[1]
    return ""


class _RingError(Exception):
    pass


def _collect_atom_shorts(seed_short, tby, path):
    """从 seed(feature/compound)沿 task_relations 收集所有 atom short id,经 compound 递归。
    path: 递归路径上的 compound short id 集(环检测)。"""
    atoms = set()
    seed_t = tby.get(seed_short)
    if not seed_t:
        return atoms
    for r in (seed_t.get("task_relations") or []):
        for k in ("from_task_ref", "to_task_ref"):
            s = short(r.get(k, ""))
            if not s or s == seed_short:
                continue
            t = tby.get(s)
            if not t:
                continue
            layer = t.get("task_layer")
            if layer == "atom":
                atoms.add(s)
            elif layer == "compound":
                if s in path:
                    raise _RingError(s)
                atoms |= _collect_atom_shorts(s, tby, path | {s})
    return atoms


def check_coverage(feature_short, tasks, dps, variants_doc):
    """纯函数:校验 feature 的 per-variant 覆盖。
    返回 {ok, feature, struct_commands, variants_checked, failures[], errors[]}。
    - failures[i] = {variant, missing[], extra[]}
    - errors[i]   = {kind: ring|no-feature|no-dp|no-option, detail}
    """
    tby = {short(t.get("task_id", "")): t for t in tasks if t.get("task_id")}
    dpby = {short(d.get("decision_id", "")): d for d in dps if d.get("decision_id")}
    result = {"feature": feature_short, "struct_commands": [], "variants_checked": 0,
              "failures": [], "errors": []}
    ft = tby.get(feature_short)
    if not ft:
        result["errors"].append({"kind": "no-feature", "detail": feature_short})
        result["ok"] = False
        return result

    # 1. 结构 atom 集(含环检测)
    try:
        atom_shorts = _collect_atom_shorts(feature_short, tby, {feature_short})
    except _RingError as e:
        result["errors"].append({"kind": "ring", "detail": f"compound 环涉及 {e}"})
        result["ok"] = False
        return result

    # atom short -> command(条件 atom 可能不在结构集,但 impact target=task 时按 tby 兜底解析)
    atom_to_cmd = {}
    for s in atom_shorts:
        c = cmd_of(tby.get(s, {}).get("ref", ""))
        if c:
            atom_to_cmd[s] = c
    struct_commands = set(atom_to_cmd.values())
    result["struct_commands"] = sorted(struct_commands)

    variants = (variants_doc or {}).get("variants", []) or []
    # 2. per-variant 校验
    for V in variants:
        active = set(struct_commands)
        for dp_short, opt_id in (V.get("dp_options") or {}).items():
            dp = dpby.get(dp_short)
            if not dp:
                result["errors"].append({"kind": "no-dp", "detail": dp_short})
                continue
            option = next((o for o in dp.get("options", []) if o.get("option_id") == opt_id), None)
            if not option:
                result["errors"].append({"kind": "no-option", "detail": f"{dp_short}/{opt_id}"})
                continue
            for imp in (option.get("impacts") or []):
                tt = imp.get("target_type")
                if tt not in ("task", "command"):
                    continue  # 纯参数 impact 不影响命令集
                if tt == "command":
                    cmd = imp.get("target_ref", "")
                    if cmd and "@" in cmd:
                        cmd = cmd.split("@")[-1]
                else:  # task
                    tref = short(imp.get("target_ref", ""))
                    cmd = atom_to_cmd.get(tref) or cmd_of(tby.get(tref, {}).get("ref", ""))
                if not cmd:
                    continue
                eff = imp.get("effect_type", "")
                if eff in REM_EFFECTS:
                    active.discard(cmd)
                elif eff in ADD_EFFECTS:
                    active.add(cmd)
                # 其他 effect_type(changes_scope 等)默认不动命令集
        md_req = set(V.get("md_required_commands") or [])
        missing = sorted(md_req - active)
        extra = sorted(active - md_req)
        if missing or extra:
            result["failures"].append({"variant": V.get("name", "?"),
                                       "missing": missing, "extra": extra})
        result["variants_checked"] += 1

    result["ok"] = (not result["failures"]) and (not result["errors"])
    return result


def _load_yaml_dir(d):
    out = []
    if not d.exists():
        return out
    for p in sorted(d.glob("*.yaml")):
        try:
            doc = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
            if isinstance(doc, dict):
                out.append(doc)
        except Exception:
            pass
    return out


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    if len(sys.argv) < 2:
        sys.exit("用法: python check_feature_coverage.py <feature_task_short> [nf] [version]")
    feature_short = sys.argv[1]
    nf = sys.argv[2] if len(sys.argv) > 2 else "UDG"
    ver = sys.argv[3] if len(sys.argv) > 3 else "20.15.2"
    A = ROOT / "task-assets" / nf / ver

    tasks = _load_yaml_dir(A / "tasks")
    dps = _load_yaml_dir(A / "decision_points")
    ft = next((t for t in tasks if short(t.get("task_id", "")) == feature_short), None)
    if not ft:
        print(f"[FAIL] feature task {feature_short} 不存在于 {A/'tasks'}")
        sys.exit(2)
    fid = feat_of(ft.get("ref", ""))
    vpath = A / "review" / f"{fid}-variants.yaml"
    if not vpath.exists():
        print(f"[FAIL] 缺 {vpath.name}:Agent 步骤① 须产出 review/{{feature_id}}-variants.yaml")
        print(f"       (feature {feature_short} → feature_id {fid})")
        sys.exit(2)
    variants = yaml.safe_load(vpath.read_text(encoding="utf-8"))

    r = check_coverage(feature_short, tasks, dps, variants)
    print(f"=== 覆盖校验:feature {feature_short} ({fid}) ===")
    print(f"结构命令集({len(r['struct_commands'])}):{r['struct_commands']}")
    print(f"变体校验数:{r['variants_checked']}")
    for e in r["errors"]:
        print(f"  [硬错] {e['kind']}: {e['detail']}")
    for f in r["failures"]:
        print(f"  [变体 {f['variant']}] 缺 {f['missing']}  多 {f['extra']}")
    print("结果:" + ("✓ 覆盖通过" if r["ok"] else "✗ 覆盖失败,回炉"))
    sys.exit(0 if r["ok"] else 1)


if __name__ == "__main__":
    main()
