"""FeatureGraph pipeline 编排入口（半自动：自动步连续跑，Agent 步遇 PAUSE 停，尾随自动步仍跑）。

用法:
  python build_all.py UDG 20.15.2                                  # 全量（自动步 skip-if-exists）
  python build_all.py UDG 20.15.2 feature                           # 只跑某步（显式单步不 skip）
  python build_all.py UDG 20.15.2 --sample GWFD-020301,GWFD-020302  # 第一批小范围验证
  python build_all.py UDG 20.15.2 dependency --rerun GWFD-020301

模型：code → Agent(prep→PAUSE) → [填输出] → code(ingest) → ...
Agent 步不调 LLM，只把 prompt 写到 data/{nf}/{version}/agent_prompts/{step}/ 然后 PAUSE；
调 Agent 把输出写到 .../agent_outputs/{step}/ 后重跑本命令即续。
"""
from __future__ import annotations

import argparse
import pathlib
import sys

import yaml

HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from builder.steps.registry import STEPS, PRODUCT_FILE, AGENT_STEPS  # noqa: E402


def make_ctx(config: dict, nf: str, version: str) -> dict:
    ne = dict(config["ne"][nf][version])
    project_root = (HERE / config["project_root"]).resolve()
    license_source = ne.pop("license_source", None)
    if license_source:
        license_source = str((project_root / license_source).resolve())
    return {
        "nf": nf,
        "version": version,
        "project_root": project_root,
        "data_dir": HERE / "data" / nf / version,  # 网元×版本 隔离
        "license_source": license_source,
        **ne,
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="FeatureGraph pipeline")
    ap.add_argument("nf", help="网元 (UDG/UNC)")
    ap.add_argument("version", help="版本 (20.15.2)")
    ap.add_argument("step", nargs="?", default=None, help="只跑某步（显式单步不 skip）")
    ap.add_argument("--rerun", default=None, help="重跑指定 feature_code/doc")
    ap.add_argument("--sample", default=None, help="只处理指定 feature_code（逗号分隔），第一批验证用")
    args = ap.parse_args(argv)

    config = yaml.safe_load((HERE / "pipeline.yaml").read_text(encoding="utf-8"))
    if args.nf not in config["ne"] or args.version not in config["ne"][args.nf]:
        print(f"未配置 {args.nf}@{args.version}，检查 pipeline.yaml")
        return 1
    ctx = make_ctx(config, args.nf, args.version)
    if args.rerun:
        ctx["rerun_target"] = args.rerun
    if args.sample:
        ctx["sample"] = {c.strip() for c in args.sample.split(",") if c.strip()}

    single = args.step is not None
    steps_to_run = [args.step] if single else config["ne"][args.nf][args.version]["steps"]
    ctx["data_dir"].mkdir(parents=True, exist_ok=True)

    paused_at = None
    for s in steps_to_run:
        if s not in STEPS:
            print(f"{args.nf}@{args.version} {s}: 跳过（未实现）")
            continue
        # 暂停态：遇到下一个 agent 步前停（其前置 agent 步还没回填完）
        if paused_at and s in AGENT_STEPS:
            print(f"  跳过 agent 步 {s}（前置 {paused_at} 仍待回填）")
            break
        # 全量跑：自动步输出已存在则 skip；Agent 步总执行 prep/check
        if not single and s not in AGENT_STEPS and not args.rerun:
            out = PRODUCT_FILE.get(s)
            if out and (ctx["data_dir"] / out).exists():
                print(f"{args.nf}@{args.version} {s}: 跳过（{out} 已存在）")
                continue

        result = STEPS[s](ctx)
        if result == "PAUSE":
            paused_at = s
            # 不 break：让尾随自动步（verify）继续跑
            print(f"\n[PAUSE] @{s}：Agent 输出待回填 → data/{args.nf}/{args.version}/agent_outputs/{s}/<key>.json")
        else:
            print(f"{args.nf}@{args.version} {s}: {result}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
