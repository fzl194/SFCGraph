"""core/overview.py 测试。"""
from builder.core.overview import (
    parse_sections, collect_raw_fields, SECTION_KEYS,
    extract_applicable_nf, extract_first_release, extract_standards, classify_doc_type,
)

SAMPLE = """# GWFD-020301 概述

#### [适用NF](#x)

SGW-U、PGW-U、UPF

#### [定义](#x)

内容计费是包过滤和分析技术。

#### [原理概述](#x)

简单来讲，内容计费就是对不同业务类型使用不同计费策略。

#### [计费与话单](#x)

本特性不涉及计费与话单。

#### [遵循标准](#x)

| 标准类别 | 标准编号 | 标准名称 |
| --- | --- | --- |
| 3GPP | 23.502 | Procedures for the 5G System |

#### [发布历史](#x)

| 特性版本 | 发布版本 | 发布说明 |
| --- | --- | --- |
| 01 | 20.0.0 | 首次发布。 |
"""


def test_parse_sections_keeps_all_13_keys_including_principle_charging():
    sections = parse_sections(SAMPLE)
    assert "适用NF" in sections and "定义" in sections
    assert "原理概述" in sections          # 旧版漏抽，已补
    assert "计费与话单" in sections         # 旧版漏抽，已补


def test_collect_raw_fields_covers_13_raw():
    sections = parse_sections(SAMPLE)
    raws = collect_raw_fields(sections)
    assert set(raws.keys()) == set(SECTION_KEYS.values())
    assert raws["principle_raw"].startswith("简单来讲")
    assert raws["charging_raw"] == "本特性不涉及计费与话单。"


def test_extract_applicable_nf_normalizes():
    assert extract_applicable_nf(parse_sections(SAMPLE)) == ["SGW-U", "PGW-U", "UPF"]


def test_extract_first_release_from_history():
    assert extract_first_release(parse_sections(SAMPLE)) == "20.0.0"


def test_extract_standards_three_col():
    std = extract_standards(parse_sections(SAMPLE))
    assert len(std) == 1
    assert std[0] == {"category": "3GPP", "number": "23.502", "name": "Procedures for the 5G System"}


def test_classify_doc_type_by_filename_and_h1():
    assert classify_doc_type("GWFD-020301 特性概述.md", "# x") == "overview"
    assert classify_doc_type("激活.md", "# 激活配置\n") == "activation"
    assert classify_doc_type("调测.md", "# 调测指南\n") == "debug"
    assert classify_doc_type("x.md", "# 参考信息\n") == "reference"
