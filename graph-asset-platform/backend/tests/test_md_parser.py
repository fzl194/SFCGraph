from app.md_parser import parse_md

MD = """---
id: UDG@MMLCommand@ADD URR
type: MMLCommand
nf: UDG
version: 20.15.2
---
# ADD URR
正文行。

## 边
- 操作配置对象: [[UDG@ConfigObject@URR]]
- 参见: [[UDG@MMLCommand@MOD URR]]
"""

def test_frontmatter():
    fm, body, edge_section = parse_md(MD)
    assert fm["id"] == "UDG@MMLCommand@ADD URR"
    assert fm["type"] == "MMLCommand"

def test_body_strips_edge_section():
    fm, body, edge_section = parse_md(MD)
    assert "# ADD URR" in body
    assert "## 边" not in body          # body 不含边章节
    assert "操作配置对象" in edge_section  # 边章节单独切出

def test_no_edges():
    md = "---\nid: X@T@y\ntype: T\n---\n正文\n"
    fm, body, edge_section = parse_md(md)
    assert edge_section == ""


def test_crlf_normalized():
    # CRLF 换行：body 不应残留 \r，表格表头与分隔符仍紧邻
    md = "---\r\nid: x\r\ntype: T\r\n---\r\n| a | b |\r\n| --- | --- |\r\n| 1 | 2 |\r\n"
    fm, body, edge_section = parse_md(md)
    assert "\r" not in body
    assert "| a | b |\n| --- | --- |" in body


def test_double_cr_normalized():
    # \r\r\n（产品文档导出遗留的双回车）：不应变成空行撑开表格
    md = "---\r\r\nid: x\r\r\ntype: T\r\r\n---\r\r\n| a | b |\r\r\n| --- | --- |\r\r\n| 1 | 2 |\r\r\n"
    fm, body, edge_section = parse_md(md)
    assert "\r" not in body
    assert "| a | b |\n| --- | --- |" in body
