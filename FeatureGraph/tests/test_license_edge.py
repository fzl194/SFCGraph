"""core/license_edge.py 测试。"""
from builder.core.license_edge import extract_license_edges_from_feature

AVAIL_QUOTED = """**License** **支持**

本特性对应的License控制项为 "82209822 LKV3G5BCBC01 内容计费基本功能 "。
"""
AVAIL_TABLE = """**License** **支持**

| 适用NF | License控制项 |
| --- | --- |
| SGW-U/PGW-U/UPF | 82209822 LKV3G5BCBC01 内容计费基本功能 |
"""


def test_extract_license_edge_quoted():
    edges = extract_license_edges_from_feature("GWFD-020301", {"availability_raw": AVAIL_QUOTED},
                                               nf="UDG", version="20.15.2")
    assert len(edges) == 1
    e = edges[0]
    assert e["license_code"] == "LKV3G5BCBC01"
    assert e["source_id"] == "UDG@20.15.2@Feature@GWFD-020301"
    assert e["target_id"] == "UDG@20.15.2@License@LKV3G5BCBC01"
    assert e["control_item_id"] == "82209822"
    assert e["source_type"] == "feature_overview"


def test_extract_license_edge_table_format():
    edges = extract_license_edges_from_feature("GWFD-020301", {"availability_raw": AVAIL_TABLE},
                                               nf="UDG", version="20.15.2")
    assert len(edges) == 1 and edges[0]["license_code"] == "LKV3G5BCBC01"


def test_hardcoded_transpose_table_wsfd_106201():
    edges = extract_license_edges_from_feature("WSFD-106201", {"availability_raw": ""},
                                               nf="UNC", version="20.15.2")
    assert len(edges) == 4
    codes = {e["license_code"] for e in edges}
    assert "LKV2CBS02" in codes and "LKV2PWSR01" in codes


def test_no_license_returns_empty():
    edges = extract_license_edges_from_feature("GWFD-X", {"availability_raw": "本特性无需获得License。"},
                                               nf="UDG", version="20.15.2")
    assert edges == []
