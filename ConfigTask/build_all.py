# ConfigTask/build_all.py
"""编排入口。CLI: [nf] [version] [feature_id]，可选过滤。"""
import argparse
import pathlib

from builder.steps.registry import STEPS, validate_order


def make_ctx(cfg, nf, version, feature_id):
    """构造步骤上下文。skeleton 在 ctx 内增量累积（enrichment）。"""
    ne = cfg["ne"][nf][version]
    here = pathlib.Path(__file__).parent
    return {
        "nf": nf,
        "version": version,
        "feature_id": feature_id,            # None=不过滤；指定=单特性
        "assets_root": here / cfg["assets_root"],
        "project_root": (here / cfg["project_root"]).resolve(),
        "skeleton": [],                       # 增量累积 task 骨架
        **ne,                                 # feature_csv / steps 等
    }


def main():
    ap = argparse.ArgumentParser(description="ConfigTask 抽取 pipeline")
    ap.add_argument("nf", nargs="?", help="网元，如 UDG；省略=全部")
    ap.add_argument("version", nargs="?", help="版本，如 20.15.2；省略=全部")
    ap.add_argument("feature_id", nargs="?", help="特性ID，单特性过滤；省略=全部")
    a = ap.parse_args()

    import yaml  # lazy import，便于 make_ctx 单元测试（无需 pyyaml）
    cfg = yaml.safe_load(open(pathlib.Path(__file__).parent / "pipeline.yaml", encoding="utf-8"))

    nfs = [a.nf] if a.nf else list(cfg["ne"])
    for nf in nfs:
        versions = [a.version] if a.version else list(cfg["ne"][nf])
        for version in versions:
            ctx = make_ctx(cfg, nf, version, a.feature_id)
            validate_order(ctx["steps"])
            for s in ctx["steps"]:
                n = STEPS[s](ctx)
                print(f"{nf}@{version} {s}: {n}")


if __name__ == "__main__":
    main()
