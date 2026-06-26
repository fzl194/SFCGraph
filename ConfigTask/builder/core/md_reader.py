# ConfigTask/builder/core/md_reader.py
"""配置 md → 4 段（操作流程/操作步骤/任务示例/数据规划表）。

数据规划表在"必备事项→数据"下（跨文档一致），所以 SECTION_DATA 取整个"必备事项"段，
后续 params 步在段内解析 *表N* 表格（前提条件文字自动忽略）。
缺失的段（如部分激活文档无"操作流程"）不在结果里，由 cut_boundaries 步处理。
"""
import re

from builder.constants import SECTION_FLOW, SECTION_STEPS, SECTION_EXAMPLE, SECTION_DATA

# H2 标题行：## [title](anchor) 或 ## title
_H2_RE = re.compile(r'^##\s+(.+)$', re.MULTILINE)

# 标题文本 → 规范段名
_TITLE_MAP = [
    (SECTION_FLOW, ("操作流程",)),
    (SECTION_STEPS, ("操作步骤",)),
    (SECTION_EXAMPLE, ("任务示例",)),
    (SECTION_DATA, ("必备事项", "数据规划表")),  # 数据规划表在必备事项下
]


def _clean_title(raw: str) -> str:
    """清理标题：去 [ ] 和 (anchor)。"""
    t = re.sub(r'\[([^\]]*)\]', r'\1', raw.strip())  # [操作流程] → 操作流程
    t = re.sub(r'\([^)]*\)', '', t)                   # 去 (anchor)
    return t.strip()


def read_sections(md_text: str) -> dict:
    """切 4 段。返回 {规范段名: 段体文本}，缺失段不在结果里。"""
    matches = list(_H2_RE.finditer(md_text))
    sections = {}
    for i, m in enumerate(matches):
        title = _clean_title(m.group(1))
        body_end = matches[i + 1].start() if i + 1 < len(matches) else len(md_text)
        body = md_text[m.end():body_end].strip()
        for canon, aliases in _TITLE_MAP:
            if any(a in title for a in aliases):
                sections[canon] = body
                break
    return sections
