"""组装 Feature 节点 + feature_category/config_relevance 规则初值推断。

对齐 schema §2.1 三类字段：原始md字段(*_raw) + 抽取归一化字段 + 来源上下文字段。
feature_category/config_relevance 这里只给规则初值，精细化由 categorize Agent 步完成。
"""
from __future__ import annotations

# catalog_section 关键词 → feature_category（主锚点，categorize Agent 步校准）
_SECTION_CATEGORY = [
    (["计费", "策略控制"], "enhanced"),
    (["带宽", "shaping", "流量控制"], "enhanced"),
    (["QoS"], "enhanced"),
    (["接入", "会话"], "protocol"),
    (["地址", "IPv6", "双栈"], "protocol"),
    (["可靠性", "故障", "自愈", "扩容", "缩容"], "operations"),
    (["License"], "operations"),
    (["SFIP", "第三方", "集成"], "integration"),
    (["架构", "服务化", "NFV", "底座", "SA-Basic", "SA框架"], "base"),
]


def infer_feature_category(catalog_section: str, definition: str) -> str:
    """以 catalog_section 为主锚点 + 定义关键词辅助。未命中默认 enhanced。"""
    text = (catalog_section or "") + " " + (definition or "")
    for keywords, cat in _SECTION_CATEGORY:
        if any(kw.lower() in text.lower() for kw in keywords):
            return cat
    return "enhanced"


def infer_config_relevance(has_activation: bool, no_config_needed: bool) -> str:
    """有激活文档→required；无激活+声明无需配置→none；其余 required（保守初值）。"""
    if no_config_needed and not has_activation:
        return "none"
    return "required"


def build_feature_node(seed: dict, raw_fields: dict, *, applicable_nf: list,
                       first_release: str, standards: list, overview_path: str | None,
                       nf: str, version: str, has_overview: str = "yes",
                       config_relevance: str = "required") -> dict:
    """组装单个 Feature 节点（四段式 id + 全部 *_raw + 归一化 + 上下文，不可变合并）。"""
    code = seed["feature_code"]
    node = {
        "id": f"{nf}@{version}@Feature@{code}",
        "feature_code": code,
        "name": seed.get("name", ""),
        "is_directory": seed.get("is_directory", False),
        "catalog_section": seed.get("catalog_section", ""),
        "parent_feature_code": seed.get("parent_feature_code", ""),
        "applicable_nf": applicable_nf,
        "nf_support_map": seed.get("nf_support_map", ""),
        "first_release_version": first_release,
        "standards": standards,
        "feature_category": infer_feature_category(seed.get("catalog_section", ""), raw_fields.get("definition_raw", "")),
        "config_relevance": config_relevance,
        "nf": nf,
        "version": version,
        "source_path": overview_path or "",
        "has_overview": has_overview,
    }
    return {**node, **raw_fields}
