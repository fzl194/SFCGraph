"""core/feature.py 测试。"""
from builder.core.feature import (
    build_feature_node, infer_feature_category, infer_config_relevance, UDG_SECTION_CATEGORY,
)


def _seed(code="GWFD-020301", name="内容计费基本功能",
          section="年费基本包-智能策略控制&计费基本包"):
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
    assert node["feature_category"] == "enhanced"   # 查表命中：智能策略控制&计费基本包
    assert node["config_relevance"] == "required"
    assert node["parent_feature_code"] == "GWFD-020300"


def test_infer_feature_category_table_hit():
    assert infer_feature_category("2/3/4G/5G业务基本特性", "") == "base"
    assert infer_feature_category("IP基本特性", "") == "base"
    assert infer_feature_category("网管特性", "") == "operations"
    assert infer_feature_category("年费增值包-5G高速承载增值包", "") == "protocol"
    assert infer_feature_category("年费增值包-eMTC解决方案增值包", "") == "protocol"
    assert infer_feature_category("年费基本包-智能策略控制&计费基本包", "") == "enhanced"


def test_infer_feature_category_fallback_for_unc_or_new_section():
    # UNC section 未在 UDG 表 → 走兜底关键词
    assert infer_feature_category("计费功能", "这是计费场景", nf="UNC") == "enhanced"
    assert infer_feature_category("协议接入", "接入协议", nf="UNC") == "protocol"
    assert infer_feature_category("可靠性", "故障恢复", nf="UNC") == "operations"
    # 完全无信号 → 默认 enhanced
    assert infer_feature_category("未知section", "", nf="UNC") == "enhanced"


def test_udg_section_table_covers_all_real_sections():
    """UDG_SECTION_CATEGORY 表覆盖 35 分区（保证全量 UD 规则化分类）。"""
    assert len(UDG_SECTION_CATEGORY) >= 35


def test_infer_config_relevance():
    # ops section → ops_only
    assert infer_config_relevance(True, False, "网管特性", 0) == "ops_only"
    assert infer_config_relevance(False, False, "灰度升级解决方案增值包", 0) == "ops_only"
    # 无激活 + 无需配置声明 → none
    assert infer_config_relevance(False, True, "IP基本特性", 0) == "none"
    # 无激活 + 有依赖 → indirect
    assert infer_config_relevance(False, False, "年费增值包-MBB可视化解决方案增值包", 2) == "indirect"
    # 有激活 → required
    assert infer_config_relevance(True, False, "年费基本包-智能策略控制&计费基本包", 0) == "required"
    # 兜底
    assert infer_config_relevance(False, False, "未知section", 0) == "required"
