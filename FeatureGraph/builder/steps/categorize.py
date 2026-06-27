"""Step categorize (代码步): feature_category / config_relevance 规则推断。

从 Agent 步降级为纯代码步（catalog_section 查表 + config_relevance 多规则），
一次性跑完全量，不再需要 PAUSE 断点。

agent/prompts.py + parse_agent_output 保留作为后续弱依赖 candidates 升级等
真正需要语义判断的步骤备用。
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path

from ..core.categorize import build_categorize_results
from ..core.io import load_jsonl, write_jsonl
from ..core.legacy import load_legacy_attributes
from .registry import step


@step("categorize", output_file="features.jsonl")
def run(ctx):
    nf, version = ctx["nf"], ctx["version"]
    data_dir = Path(ctx["data_dir"])
    features = load_jsonl(data_dir / "features.jsonl")
    depends = load_jsonl(data_dir / "feature_depends_on.jsonl") \
        if (data_dir / "feature_depends_on.jsonl").exists() else []

    legacy_dir = ctx.get("legacy_dir")
    legacy_attrs = load_legacy_attributes(ctx["project_root"] / legacy_dir, nf) \
        if legacy_dir else {}

    sample = ctx.get("sample")
    rerun = ctx.get("rerun_target")

    results = build_categorize_results(features, depends, legacy_attrs, nf=nf)
    by_code = {r["feature_code"]: r for r in results}

    ingested = 0
    for f in features:
        code = f["feature_code"]
        if sample and code not in sample:
            continue
        if rerun and rerun not in code:
            continue
        r = by_code.get(code)
        if not r:
            continue
        f["feature_category"] = r["feature_category"]
        f["config_relevance"] = r["config_relevance"]
        f["category_reason"] = r["category_reason"]
        ingested += 1

    write_jsonl(data_dir / "features.jsonl", features)

    cat_dist = Counter(r["feature_category"] for r in results)
    rel_dist = Counter(r["config_relevance"] for r in results)
    print(f"[categorize:{nf}/{version}] {ingested} 特性分类完成 | "
          f"category={dict(cat_dist)} | relevance={dict(rel_dist)} → {data_dir}/features.jsonl")
    return ingested
