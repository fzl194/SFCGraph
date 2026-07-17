import yaml
import re

_FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?(.*)\Z", re.S)
_EDGE_HEADER_RE = re.compile(r"\n##\s*边\s*\n", re.M)

def parse_md(text: str) -> tuple:
    """→ (frontmatter_dict, body_md, edge_section_text)。无 frontmatter→空dict；无##边→''。"""
    # 归一化换行：源 md 可能是 CRLF 甚至 \r\r\n（产品文档导出遗留的双回车）。
    # 不归一化的话，残留 \r 会让 markdown-it 把 \r\r\n 错当成 \n\n（多出空行），
    # 导致表头与分隔符之间被插入空行 → GFM 表格整表判废（只渲染成段落）。
    text = re.sub(r"\r+\n", "\n", text)   # 任意 \r 串 + \n → 单个 \n
    text = text.replace("\r", "\n")        # 残留的裸 \r（老 Mac 换行）→ \n
    fm: dict = {}
    body = text
    m = _FM_RE.match(text)
    if m:
        fm = yaml.safe_load(m.group(1)) or {}
        body = m.group(2)
    # 切出 ## 边 章节（取该标题到文末）
    em = _EDGE_HEADER_RE.search("\n" + body)
    edge_section = ""
    if em:
        # em.start() 指向 "\n## 边\n" 的开头 \n（body 前补了一个 \n）
        cut = em.start()  # 相对 prefixed body
        edge_section = ("\n" + body)[cut:].lstrip("\n")
        body = ("\n" + body)[:cut].rstrip("\n")
    return fm, body, edge_section
