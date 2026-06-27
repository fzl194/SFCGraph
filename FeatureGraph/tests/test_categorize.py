"""core/categorize.py 测试（纯函数 build_categorize_results）。"""
from builder.core.categorize import build_categorize_results


def _feat(code, section="", definition="", availability="", has_activation=False):
    return {"feature_code": code, "catalog_section": section,
            "definition_raw": definition, "availability_raw": availability,
            "has_activation_doc": has_activation}


def test_build_categorize_results_charging():
    feats = [_feat("GWFD-020301", "年费基本包-智能策略控制&计费基本包",
                   definition="内容计费...")]
    out = build_categorize_results(feats, nf="UDG")
    assert out[0]["feature_category"] == "enhanced"
    assert out[0]["config_relevance"] == "required"  # 默认 has_activation=False，但无 no_config 也无 dep
    assert "section=" in out[0]["category_reason"]


def test_no_config_needed_yields_none():
    feats = [_feat("GWFD-IP1", "IP基本特性", definition="", availability="本特性无需配置")]
    out = build_categorize_results(feats, nf="UDG")
    assert out[0]["config_relevance"] == "none"


def test_no_activation_with_dep_yields_indirect():
    feats = [_feat("GWFD-MBB", "年费增值包-MBB可视化解决方案增值包")]
    deps = [{"source_feature_code": "GWFD-MBB", "target_feature_code": "GWFD-110101"}]
    out = build_categorize_results(feats, depends=deps, nf="UDG")
    assert out[0]["config_relevance"] == "indirect"


def test_ops_section_yields_ops_only():
    feats = [_feat("GWFD-NMS", "网管特性", has_activation=True)]
    out = build_categorize_results(feats, nf="UDG")
    assert out[0]["config_relevance"] == "ops_only"


def test_unc_fallback_section():
    # UNC 无分区表，走兜底
    feats = [_feat("WSFD-X", "计费功能", definition="计费策略")]
    out = build_categorize_results(feats, nf="UNC")
    assert out[0]["feature_category"] == "enhanced"


def test_legacy_attrs_in_reason():
    feats = [_feat("GWFD-020301", "年费基本包-智能策略控制&计费基本包")]
    legacy = {"GWFD-020301": {"feature_type": "config_enable"}}
    out = build_categorize_results(feats, legacy_attrs=legacy, nf="UDG")
    assert "legacy_type=config_enable" in out[0]["category_reason"]
