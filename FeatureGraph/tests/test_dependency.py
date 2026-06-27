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


def test_classify_edges_merged_single_file_minimal_fields():
    raws = {"feature_interaction_raw": INTERACTION}
    deps = extract_dependencies("GWFD-020301", raws, feature_lookup={})
    ev = {"GWFD-020301": ["a/b.md"]}
    edges = classify_edges(deps, nf="UDG", version="20.15.2", evidence_lookup=ev)
    assert len(edges) == 2
    # 字段精简验证
    expected_keys = {"source_id", "target_id", "relation_type", "interaction_note",
                     "source_evidence_ids", "source_type", "nf", "version"}
    for e in edges:
        assert set(e.keys()) == expected_keys
    # 四段式 source_id/target_id
    assert edges[0]["source_id"] == "UDG@20.15.2@Feature@GWFD-020301"
    assert edges[0]["target_id"] == "UDG@20.15.2@Feature@GWFD-110101"
    assert edges[1]["target_id"] == "UDG@20.15.2@Feature@GWFD-020302"
    # description 改名 interaction_note
    assert edges[0]["interaction_note"] == "必须先开启SA。"
    assert edges[1]["interaction_note"] == "不能同时使用。"
    # evidence 合并
    assert edges[0]["source_evidence_ids"] == ["a/b.md"]


def test_classify_edges_includes_candidates():
    """弱语义（affects/interacts_with/supports/other/cooperates_with）也进同一文件。"""
    raws = {"feature_interaction_raw": "| 影响 | [GWFD-020301 自身](../GWFD-020301.md) | 无 | 测试 |\n| 协同 | [GWFD-020302 X](../x.md) | 无 | 测试2 |"}
    deps = extract_dependencies("GWFD-020301", raws, feature_lookup={})
    # 自引用过滤后剩 协同
    edges = classify_edges(deps, nf="UDG", version="20.15.2")
    assert len(edges) == 1 and edges[0]["relation_type"] == "cooperates_with"


def test_self_reference_filtered():
    raws = {"feature_interaction_raw": "| 依赖 | [GWFD-020301 自身](../GWFD-020301.md) | 无 | x |"}
    deps = extract_dependencies("GWFD-020301", raws, feature_lookup={})
    assert deps == []


def test_url_typo_corrected():
    raws = {"feature_interaction_raw": "| 依赖 | [GWFD-020808 用户面地址自动检测](../GWFD-010108_xxx.md) | 无 | x |"}
    deps = extract_dependencies("GWFD-020301", raws, feature_lookup={})
    assert deps and deps[0]["target_feature_code"] == "GWFD-010108"
