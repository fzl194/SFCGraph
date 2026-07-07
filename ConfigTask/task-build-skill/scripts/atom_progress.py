"""UNC atom 构建进度跟踪（progress md 的 init / update）。

  --init:  从候选命令清单初始化 progress md（全部 pending，按 10/批分批）
  --update: 扫描 assert/UNC/{ver}/tasks/ 已建 atom，回填 status/atom_id/参数数/DP/rule

进度 md：assert/UNC/{ver}/atom-build-progress.md
用法：
  python atom_progress.py [ver] --init
  python atom_progress.py [ver] --update
"""
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("需要 pyyaml")

ROOT = Path(__file__).resolve().parents[2]          # ConfigTask/
VER = sys.argv[1] if len(sys.argv) > 1 else "20.15.2"
MODE = next((a for a in sys.argv[2:] if a in ("--init", "--update")), "--init")
NF = "UNC"
A = ROOT / "assert" / NF / VER
CAND = ROOT / "task-build-skill" / "scripts" / "unc_candidate_commands.txt"
PROG = A / "atom-build-progress.md"
BATCH_SIZE = 10


def short(ref: str) -> str:
    return ref.split("@")[-1] if ref else ""


def read_candidates():
    return [l.strip() for l in CAND.read_text(encoding="utf-8").splitlines()
            if l.strip() and not l.strip().startswith("#")]


def scan_atoms():
    """返回 {command_name: (atom_id_short, n_params, has_dp, has_rule)}。"""
    tasks, rules, dps = {}, {}, {}
    for d in (A / "tasks").glob("*.yaml"):
        try:
            t = yaml.safe_load(d.read_text(encoding="utf-8")) or {}
            if t.get("task_id"):
                tasks[t["task_id"]] = t
        except Exception:
            pass
    for d in (A / "task_rules").glob("*.yaml"):
        try:
            r = yaml.safe_load(d.read_text(encoding="utf-8")) or {}
            rules.setdefault(r.get("owner_task_ref", ""), []).append(r)
        except Exception:
            pass
    for d in (A / "decision_points").glob("*.yaml"):
        try:
            dp = yaml.safe_load(d.read_text(encoding="utf-8")) or {}
            dps.setdefault(dp.get("owner_task_ref", ""), []).append(dp)
        except Exception:
            pass
    out = {}
    for tid, t in tasks.items():
        if t.get("task_layer") != "atom":
            continue
        ref = t.get("ref", "")
        cmd = ref.split("@MMLCommand@", 1)[1] if "@MMLCommand@" in ref else ""
        nparams = len(t.get("parameter_bindings") or [])
        out[cmd] = (short(tid), nparams, len(dps.get(tid, [])) > 0, len(rules.get(tid, [])) > 0)
    return out


def render(commands, atoms):
    done = sum(1 for c in commands if c in atoms)
    lines = [
        "# UNC atom 构建进度\n",
        f"> 候选命令 {len(commands)} 条（剔 LST）。每批 {BATCH_SIZE} 条。\n",
        f"> 已建 atom：**{done} / {len(commands)}**\n\n",
        "| batch | # | command | atom_id | status | params | DP | rule | notes |\n",
        "|---|---|---|---|---|---|---|---|---|\n",
    ]
    for i, cmd in enumerate(commands):
        batch = i // BATCH_SIZE + 1
        if cmd in atoms:
            aid, np_, dp, ru = atoms[cmd]
            status = "done"
            row = f"| {batch} | {i+1} | `{cmd}` | {aid} | {status} | {np_} | {'Y' if dp else '-'} | {'Y' if ru else '-'} | |\n"
        else:
            row = f"| {batch} | {i+1} | `{cmd}` | - | pending | - | - | - | |\n"
        lines.append(row)
    # 批次汇总
    lines.append("\n## 批次汇总\n\n| batch | 范围 | done / total |\n|---|---|---|\n")
    nbatches = (len(commands) + BATCH_SIZE - 1) // BATCH_SIZE
    for b in range(1, nbatches + 1):
        lo, hi = (b - 1) * BATCH_SIZE, min(b * BATCH_SIZE, len(commands))
        d = sum(1 for c in commands[lo:hi] if c in atoms)
        lines.append(f"| {b} | #{lo+1}~#{hi} | {d}/{hi-lo} |\n")
    return "".join(lines)


def main():
    commands = read_candidates()
    if not commands:
        sys.exit(f"候选清单为空：{CAND}")
    atoms = scan_atoms() if MODE == "--update" else {}
    PROG.write_text(render(commands, atoms), encoding="utf-8")
    print(f"[{MODE}] {PROG.relative_to(ROOT.parent)}  已建 {len(atoms)}/{len(commands)}")


if __name__ == "__main__":
    main()
