# ConfigTask/build_all.py
"""ConfigTask pipeline 编排入口（半自动：自动步连续跑，Agent 步遇 PAUSE 停）。

用法:
  python build_all.py UDG 20.15.2                    # 全量：自动步跑+skip，Agent步遇PAUSE停
  python build_all.py UDG 20.15.2 scan               # 只跑某步（显式单步不 skip）
  python build_all.py UDG 20.15.2 merge_fields --rerun cluster-003  # 重跑指定簇

模型：code → Agent(prep→PAUSE) → [填输出] → code(ingest+verify) → code → ...
Agent 步不调 LLM，只把全部 prompt 写到 data/agent_prompts/{step}/ 然后 PAUSE；
调 Agent 把输出写到 data/agent_outputs/{step}/ 后重跑本命令即续。
"""
import argparse
import pathlib
import yaml

from builder.steps.registry import STEPS, PRODUCT_FILE, AGENT_STEPS


def make_ctx(config, nf, version):
    """构造 step 上下文。"""
    here = pathlib.Path(__file__).parent
    ne = dict(config["ne"][nf][version])  # 拷贝，避免 **ne 覆盖已解析字段
    project_root = (here / config["project_root"]).resolve()
    # 相对 project_root（仓库根）解析，与 corpus_root 一致
    command_graph_dir = ne.pop("command_graph_dir", None)
    if command_graph_dir:
        command_graph_dir = str((project_root / command_graph_dir).resolve())
    # 数字资产按 网元×版本 隔离（Schema §2：分层键 = 网元×版本）
    data_dir = here / "data" / nf / version
    return {
        "nf": nf,
        "version": version,
        "project_root": project_root,
        "data_dir": data_dir,
        "assets_root": data_dir / "assets",
        "command_graph_dir": command_graph_dir,
        **ne,
    }


def main():
    ap = argparse.ArgumentParser(description="ConfigTask pipeline")
    ap.add_argument("nf", help="网元 (UDG/UNC)")
    ap.add_argument("version", help="版本 (20.15.2)")
    ap.add_argument("step", nargs="?", default=None, help="只跑某步（显式单步不 skip）")
    ap.add_argument("--rerun", default=None, help="重跑指定文档/簇")
    args = ap.parse_args()

    config = yaml.safe_load(
        open(pathlib.Path(__file__).parent / "pipeline.yaml", encoding="utf-8")
    )
    ctx = make_ctx(config, args.nf, args.version)
    if args.rerun:
        ctx["rerun_target"] = args.rerun

    single = args.step is not None
    steps_to_run = [args.step] if single else ctx["steps"]
    paused_at = None
    for s in steps_to_run:
        if s not in STEPS:
            print(f"  跳过未实现的 step: {s}")
            continue
        # 暂停态：跳过后续 agent 步（其前置 agent 步还没回填完）
        if paused_at and s in AGENT_STEPS:
            print(f"  跳过 agent 步 {s}（前置 {paused_at} 仍待回填）")
            break
        # 全量跑时：自动步输出已存在则跳过（快速续跑）；Agent 步总执行 prep/check
        if not single and s not in AGENT_STEPS and not args.rerun:
            out = PRODUCT_FILE.get(s)
            if out and (ctx["data_dir"] / out).exists():
                print(f"{args.nf}@{args.version} {s}: 跳过（{out} 已存在）")
                continue

        result = STEPS[s](ctx)

        if result == "PAUSE":
            paused_at = s
            bar = "=" * 64
            print(f"\n{bar}")
            print(f"[PAUSE] @{s}：仍有 Agent 输出待回填（交接清单见上）")
            print(f"   尾随自动步(finalize/verify)仍会跑；下一个 agent 步前停。")
            print(f"   → 调 Agent 写 data/agent_outputs/{s}/<key>.json，再重跑续。")
            print(f"{bar}")
            # 不 break：让尾随自动步继续跑
        else:
            print(f"{args.nf}@{args.version} {s}: {result}")


if __name__ == "__main__":
    main()
