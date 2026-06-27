# ConfigTask/tests/test_enrich.py
"""enrich 解析器单测：从原始 md 三段（操作步骤/任务示例/数据规划表）按命令抽证据。

证据在拆分/聚类阶段一次性补进 candidate，merge_fields 不再回读 md。
"""
import json
import pathlib

import pytest

from builder.core.enrich import (
    extract_command_examples,
    extract_param_rows,
    extract_step_text,
)

# ---- extract_command_examples ----


def test_examples_filter_by_command():
    body = """前置说明
```
ADD URR:URRNAME="x", URRID=1;
ADD URRGROUP:URRGROUPNAME="g", UPURRNAME1="x";
ADD FILTER:NAME="f";
```
"""
    out = extract_command_examples(body, ["ADD URR", "ADD URRGROUP"])
    assert any(l.startswith("ADD URR:") and "URRNAME" in l for l in out)
    assert any(l.startswith("ADD URRGROUP:") for l in out)
    assert not any("ADD FILTER" in l for l in out)


def test_examples_dedup_identical_lines():
    body = (
        'ADD URR:URRNAME="a", URRID=1;\n'
        'ADD URR:URRNAME="a", URRID=1;\n'
        'ADD URR:URRNAME="b", URRID=2;'
    )
    out = extract_command_examples(body, ["ADD URR"])
    # 重复行去重，不同取值保留（变体是 decision_driven 的证据）
    assert len(out) == 2


def test_examples_ignore_comment_and_prose_lines():
    body = """// 这是注释，配置URR的说明
ADD URR:URRID=1;
配置规则属性。
"""
    out = extract_command_examples(body, ["ADD URR"])
    assert out == ["ADD URR:URRID=1;"]


def test_examples_cap_per_command():
    body = "\n".join(f'ADD URR:URRID={i};' for i in range(20))
    out = extract_command_examples(body, ["ADD URR"], max_per_cmd=6)
    assert len(out) == 6


# ---- extract_param_rows ----


def test_param_rows_filter_and_parse():
    body = """| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD URR** | 使用量上报规则名称（URRNAME） | URR_x | 本端规划 | 说明1 |
| **ADD URR** | URR标识（URRID） | 12500 | 全网规划 | 说明2 |
| **ADD FILTER** | 过滤器名称（NAME） | f1 | 本端规划 | 说明3 |
"""
    rows = extract_param_rows(body, ["ADD URR"])
    assert len(rows) == 2
    assert rows[0]["command"] == "ADD URR"
    assert rows[0]["param_code"] == "URRNAME"
    assert rows[0]["obtain_method"] == "本端规划"
    assert rows[1]["param_code"] == "URRID"
    assert rows[1]["obtain_method"] == "全网规划"
    assert all(r["command"] != "ADD FILTER" for r in rows)


def test_param_rows_handle_markdown_link_in_category():
    body = """| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD URR**](some-url) | URR标识（URRID） | 1 | 全网规划 | x |
"""
    rows = extract_param_rows(body, ["ADD URR"])
    assert len(rows) == 1
    assert rows[0]["command"] == "ADD URR"
    assert rows[0]["param_code"] == "URRID"


def test_param_rows_skip_separator_and_header():
    body = """| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD URR** | 标识（URRID） | 1 | 全网规划 | x |
"""
    rows = extract_param_rows(body, ["ADD URR"])
    assert len(rows) == 1  # 表头与分隔行不计


def test_param_rows_empty_when_no_match():
    body = """| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD FILTER** | 名称（NAME） | f | 本端规划 | x |
"""
    assert extract_param_rows(body, ["ADD URR"]) == []


# ---- extract_step_text ----


def test_step_text_filter_by_command_intersection():
    doc = {"steps": [
        {"commands": ["ADD URR"], "raw_text": "1. 配置URR。"},
        {"commands": ["ADD FILTER"], "raw_text": "2. 配置过滤器。"},
        {"commands": ["ADD URR", "ADD URRGROUP"], "raw_text": "3. 配置URR与组。"},
    ]}
    out = extract_step_text(doc, ["ADD URR", "ADD URRGROUP"])
    assert "配置URR" in out
    assert "配置URR与组" in out
    assert "配置过滤器" not in out


def test_step_text_empty_when_no_match():
    doc = {"steps": [{"commands": ["ADD FILTER"], "raw_text": "x"}]}
    assert extract_step_text(doc, ["ADD URR"]) == ""


# ---- 集成：真实文档（文档存在才跑）----

_REAL_DOC = (
    pathlib.Path(__file__).resolve().parent.parent.parent
    / "output"
    / "UDG_Product_Documentation_CH_20.15.2"
    / "特性部署"
    / "特性指南"
    / "UDG特性指南"
    / "计费功能"
    / "GWFD-020301 内容计费基本功能"
    / "部署UPF_28493406.md"
)


@pytest.mark.skipif(not _REAL_DOC.exists(), reason="真实文档不存在")
def test_integration_real_charging_doc():
    from builder.core.md_reader import read_sections

    secs = read_sections(_REAL_DOC.read_text(encoding="utf-8", errors="ignore"))
    cmds = ["ADD URR", "ADD URRGROUP", "ADD PCCPOLICYGRP"]

    examples = extract_command_examples(secs["任务示例"], cmds)
    rows = extract_param_rows(secs["数据规划表"], cmds)

    # 任务示例里有 ADD URR 的 MML 配置原文
    assert any(l.startswith("ADD URR:") for l in examples)
    # URRID 的获取方法为全网规划
    urrid = [r for r in rows if r["param_code"] == "URRID"]
    assert urrid and urrid[0]["obtain_method"] == "全网规划"
    # USAGERPTMODE 行存在（这是 decision_driven 的关键参数）
    assert any(r["param_code"] == "USAGERPTMODE" for r in rows)
