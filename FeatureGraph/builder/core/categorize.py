"""categorize 纯函数（特征分类，已从 Agent 降级为代码规则）。

build_categorize_results: 给定 features + depends + legacy，返回每特性的
{feature_code, feature_category, config_relevance, category_reason}。

agent/prompts.py 保留作为弱依赖 candidates 升级等真正需要语义判断的步骤备用。
"""
from __future__ import annotations

from .feature import infer_config_relevance, infer_feature_category
from .legacy import load_legacy_attributes


def build_categorize_results(features: list[dict], depends: list[dict] | None = None,
                             legacy_attrs: dict | None = None, nf: str = "UDG") -> list[dict]:
    """纯函数：对每个 feature 计算 feature_category / config_relevance / category_reason。"""
    depends = depends or []
    legacy_attrs = legacy_attrs or {}

    dep_count: dict[str, int] = {}
    for e in depends:
        dep_count[e["source_feature_code"]] = dep_count.get(e["source_feature_code"], 0) + 1

    results: list[dict] = []
    for f in features:
        code = f["feature_code"]
        section = f.get("catalog_section", "")
        definition = f.get("definition_raw", "") or ""
        availability = f.get("availability_raw", "") or ""
        has_activation = bool(f.get("has_activation_doc", False))
        no_config_needed = "无需配置" in availability or "无需配置" in definition
        legacy = legacy_attrs.get(code, {})
        legacy_type = legacy.get("feature_type", "") or "none"

        category = infer_feature_category(section, definition, nf=nf)
        relevance = infer_config_relevance(has_activation, no_config_needed,
                                           section, dep_count.get(code, 0))
        results.append({
            "feature_code": code,
            "feature_category": category,
            "config_relevance": relevance,
            "category_reason": f"section={section or '(空)'} legacy_type={legacy_type} "
                               f"has_activation={has_activation} dep={dep_count.get(code,0)}",
        })
    return results
