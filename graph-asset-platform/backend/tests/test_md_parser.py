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
