"""core/feature.py 测试。"""
from builder.core.feature import build_feature_node, infer_feature_category, infer_config_relevance


def _seed(code="GWFD-020301", name="内容计费基本功能", section="年费基本包-智能策略控制&计费基本包"):
    return {"feature_code": code, "name": name, "is_directory": False,
            "catalog_section": section, "parent_feature_code": "GWFD-020300",
            "nf_support_map": "UPF(5G)=M", "product_version": "20.15.2"}


def test_build_feature_node_four_part_id_and_raw_fields():
    seed = _seed()
    raws = {"definition_raw": "内容计费...", "applicable_nf_raw": "SGW-U、PGW-U、UPF",
            "principle_raw": "", "charging_raw": "本特性不涉及计费与话单。"}
    node = build_feature_node(seed, raws, applicable_nf=["SGW-U", "PGW-U", "UPF"],
                              first_release="20.0.0", standards=[], overview_path="a/b.md",
                              nf="UDG", version="20.15.2")
    assert node["id"] == "UDG@20.15.2@Feature@GWFD-020301"
    assert node["applicable_nf"] == ["SGW-U", "PGW-U", "UPF"]
    assert node["definition_raw"] == "内容计费..."
    assert node["principle_raw"] == "" and node["charging_raw"] == "本特性不涉及计费与话单。"
    assert node["parent_feature_code"] == "GWFD-020300"
    assert node["has_overview"] == "yes"
    assert node["feature_category"] == "enhanced"   # 计费 section
    assert node["config_relevance"] == "required"   # 默认


def test_infer_category_by_section():
    assert infer_feature_category("年费基本包-智能策略控制&计费基本包", "计费") == "enhanced"
    assert infer_feature_category("服务化架构功能", "云化分布式软件架构") == "base"
    assert infer_feature_category("可靠性功能", "故障恢复") == "operations"
    assert infer_feature_category("SFIP功能", "第三方应用") == "integration"
    assert infer_feature_category("地址分配功能", "IPv6") == "protocol"


def test_infer_config_relevance():
    assert infer_config_relevance(has_activation=False, no_config_needed=True) == "none"
    assert infer_config_relevance(has_activation=True, no_config_needed=False) == "required"
    assert infer_config_relevance(has_activation=False, no_config_needed=False) == "required"
