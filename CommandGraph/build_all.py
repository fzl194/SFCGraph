"""CommandGraph 一键编排入口。

用法：
  python build_all.py                # 全量（所有 nf / 所有 version）
  python build_all.py UDG            # 单网元（所有 version）
  python build_all.py UDG 20.15.2    # 单版本

机制：
  1. 读 pipeline.yaml
  2. 按 [nf_filter] [version_filter] 命令行参数选性过滤
  3. 对每个 (nf, version) 依序跑 steps 列表
  4. 每个 (nf, version, step) 用 try/except 隔离失败——打印三元组错误后继续其他
  5. project_root 指 SFCGraph 根（pipeline.yaml 里 `project_root: ..`）
"""
import argparse
import sys
import traceback
from pathlib import Path
from types import SimpleNamespace

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise ImportError("CommandGraph 需要 PyYAML：pip install pyyaml") from exc

# 让本脚本既能 `python build_all.py` 也能 `python CommandGraph/build_all.py` 跑
HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from builder.steps.registry import STEPS, validate_order  # noqa: E402


def load_pipeline(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def make_ctx(cfg: dict, nf: str, version: str, entry: dict) -> SimpleNamespace:
    """构造 step 用的 ctx（字段见模块 docstring）。"""
    here = HERE
    project_root = (here / cfg["project_root"]).resolve()
    assets_root = (here / cfg["assets_root"]).resolve()
    source = (project_root / entry["source"]).resolve()
    out_dir = assets_root / nf / version
    def _opt_csv(key):
        rel = entry.get(key)
        return str((project_root / rel).resolve()) if rel else None

    parameter_csv = None
    if entry.get("parameter_csv"):
        parameter_csv = str((project_root / entry["parameter_csv"]).resolve())
    return SimpleNamespace(
        nf=nf,
        version=version,
        source=str(source),
        project_root=str(project_root),
        assets_root=str(assets_root),
        out_dir=str(out_dir),
        parameter_csv=parameter_csv,
        mod_rules_csv=_opt_csv("mod_rules_csv"),
        rmv_rules_csv=_opt_csv("rmv_rules_csv"),
        uniqueness_rules_csv=_opt_csv("uniqueness_rules_csv"),
    )


def select_targets(cfg: dict, nf_filter, version_filter):
    """按命令行过滤参数挑出要执行的 (nf, version, entry) 三元组列表。"""
    targets = []
    for nf, versions in cfg.get("ne", {}).items():
        if nf_filter and nf != nf_filter:
            continue
        for version, entry in versions.items():
            if version_filter and version != version_filter:
                continue
            targets.append((nf, version, entry))
    return targets


def run_pipeline(cfg: dict, nf_filter=None, version_filter=None) -> int:
    targets = select_targets(cfg, nf_filter, version_filter)
    if not targets:
        print("没有匹配的 (nf, version)，检查 pipeline.yaml 或命令行过滤参数。")
        return 1

    failures = 0
    for nf, version, entry in targets:
        steps = entry.get("steps", [])
        ctx = make_ctx(cfg, nf, version, entry)
        try:
            ordered = validate_order(steps, ctx.out_dir)
        except ValueError as e:
            print(f"[{nf}/{version}] 步骤配置错误：{e}")
            failures += 1
            continue
        for step_name in ordered:
            try:
                STEPS[step_name](ctx)
            except Exception as e:  # 单步失败隔离：打印三元组 + 栈，继续其他
                failures += 1
                print(f"[ERROR] {nf}/{version}/{step_name} 失败：{e}")
                traceback.print_exc()

    print(f"\n=== pipeline 完成：{len(targets)} 个 (nf,version) 处理，{failures} 个步骤失败 ===")
    return 1 if failures else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="CommandGraph 一键编排")
    ap.add_argument("nf", nargs="?", default=None, help="网元过滤，如 UDG（默认全量）")
    ap.add_argument("version", nargs="?", default=None, help="版本过滤，如 20.15.2（默认全量）")
    args = ap.parse_args(argv)

    cfg = load_pipeline(HERE / "pipeline.yaml")
    return run_pipeline(cfg, nf_filter=args.nf, version_filter=args.version)


if __name__ == "__main__":
    sys.exit(main())
