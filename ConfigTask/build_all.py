# ConfigTask/build_all.py
"""ConfigTask pipeline 编排入口。

用法:
  python build_all.py UDG 20.15.2                    # 全量
  python build_all.py UDG 20.15.2 scan               # 只跑某步
  python build_all.py UDG 20.15.2 split_tasks --rerun GWFD-020301  # 重跑某文档
"""
import argparse
import pathlib
import yaml

from builder.steps.registry import STEPS


def make_ctx(config, nf, version):
    """构造 step 上下文。"""
    here = pathlib.Path(__file__).parent
    ne = config["ne"][nf][version]
    project_root = (here / config["project_root"]).resolve()
    command_graph_dir = ne.get("command_graph_dir")
    if command_graph_dir:
        command_graph_dir = str((here / command_graph_dir).resolve())
    return {
        "nf": nf,
        "version": version,
        "project_root": project_root,
        "data_dir": here / "data",
        "assets_root": here / config["assets_root"],
        "command_graph_dir": command_graph_dir,
        **ne,
    }


def main():
    ap = argparse.ArgumentParser(description="ConfigTask pipeline")
    ap.add_argument("nf", help="网元 (UDG/UNC)")
    ap.add_argument("version", help="版本 (20.15.2)")
    ap.add_argument("step", nargs="?", default=None, help="只跑某步")
    ap.add_argument("--rerun", default=None, help="重跑指定文档/簇")
    args = ap.parse_args()

    config = yaml.safe_load(
        open(pathlib.Path(__file__).parent / "pipeline.yaml", encoding="utf-8")
    )
    ctx = make_ctx(config, args.nf, args.version)
    if args.rerun:
        ctx["rerun_target"] = args.rerun

    steps_to_run = [args.step] if args.step else ctx["steps"]
    for s in steps_to_run:
        if s not in STEPS:
            print(f"  跳过未实现的 step: {s}")
            continue
        n = STEPS[s](ctx)
        print(f"{args.nf}@{args.version} {s}: {n}")


if __name__ == "__main__":
    main()
