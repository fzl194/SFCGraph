"""core/categorize.py 测试。"""
from builder.core.categorize import batch_key, build_agent_input, parse_agent_output


def test_batch_key_order_independent_and_stable():
    assert batch_key(["GWFD-020301", "GWFD-020302"]) == batch_key(["GWFD-020302", "GWFD-020301"])
    assert batch_key(["GWFD-020301"]).startswith("batch_")


def test_build_agent_input_includes_context_and_legacy():
    feats = [{"feature_code": "GWFD-020301", "name": "内容计费", "catalog_section": "计费",
              "definition_raw": "内容计费是...", "has_activation_doc": True,
              "feature_category": "enhanced", "config_relevance": "required"}]
    legacy = {"GWFD-020301": {"feature_type": "config_enable", "config_required": "true"}}
    out = build_agent_input(feats, legacy)
    assert out[0]["feature_code"] == "GWFD-020301"
    assert out[0]["legacy_feature_type"] == "config_enable"
    assert out[0]["rule_initial_category"] == "enhanced"
    assert out[0]["has_activation_doc"] is True


def test_parse_agent_output_dict_and_text():
    batch = [{"feature_code": "GWFD-020301"}, {"feature_code": "GWFD-020302"}]
    d = parse_agent_output({"GWFD-020301": {"feature_category": "enhanced"}}, batch)
    assert d["GWFD-020301"]["feature_category"] == "enhanced"
    t = parse_agent_output('{"GWFD-020302": {"feature_category": "base", "config_relevance": "none"}}', batch)
    assert t["GWFD-020302"]["feature_category"] == "base"


def test_parse_agent_output_empty_text():
    batch = [{"feature_code": "GWFD-020301"}]
    assert parse_agent_output("not json", batch) == {}
