"""core/dependency.py 测试。"""
from builder.core.dependency import extract_dependencies, classify_edges

INTERACTION = """| 交互类型 | 相关特性 | 控制项名称 | 交互说明 |
| --- | --- | --- | --- |
| 依赖 | [GWFD-110101 SA-Basic](../GWFD-110101_x.md) | 82209749 SA-Basic | 必须先开启SA。 |
| 互斥 | [GWFD-020302 基于业务时长](../GWFD-020302_y.md) | 无 | 不能同时使用。 |
"""


def test_extract_dependencies_depends_and_conflict():
    raws = {"feature_interaction_raw": INTERACTION}
    deps = extract_dependencies("GWFD-020301", raws, feature_lookup={})
    assert any(d["target_feature_code"] == "GWFD-110101" and d["raw_type"] == "depends_on" for d in deps)
    assert any(d["target_feature_code"] == "GWFD-020302" and d["raw_type"] == "conflicts_with" for d in deps)


def test_classify_edges_splits_and_pair_id_and_evidence():
    raws = {"feature_interaction_raw": INTERACTION}
    deps = extract_dependencies("GWFD-020301", raws, feature_lookup={})
    ev = {"GWFD-020301": ["a/b.md"]}
    edges = classify_edges(deps, nf="UDG", version="20.15.2", evidence_lookup=ev)
    assert len(edges["depends_on"]) == 1 and len(edges["conflicts_with"]) == 1
    assert edges["conflicts_with"][0]["conflict_pair_id"].startswith("conflict:")
    assert edges["depends_on"][0]["source_evidence_ids"] == ["a/b.md"]
    assert edges["depends_on"][0]["source_id"] == "UDG@20.15.2@Feature@GWFD-020301"
    assert edges["depends_on"][0]["target_id"] == "UDG@20.15.2@Feature@GWFD-110101"


def test_self_reference_filtered():
    raws = {"feature_interaction_raw": "| 依赖 | [GWFD-020301 自身](../GWFD-020301.md) | 无 | x |"}
    deps = extract_dependencies("GWFD-020301", raws, feature_lookup={})
    assert deps == []


def test_url_typo_corrected():
    # 链接文本 GWFD-020808（笔误）但 URL 是 GWFD-010108 → 取 URL
    raws = {"feature_interaction_raw": "| 依赖 | [GWFD-020808 用户面地址自动检测](../GWFD-010108_xxx.md) | 无 | x |"}
    deps = extract_dependencies("GWFD-020301", raws, feature_lookup={})
    assert deps and deps[0]["target_feature_code"] == "GWFD-010108"
