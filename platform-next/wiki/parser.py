"""wiki md 解析器（纯函数，无 IO）。

链接约定（assets/CLAUDE.md §5.5）：
- 标准 markdown 链接 [text](path.md) → assets 根相对路径，目标存在则 resolved。
- [[对象ID]] 占位 → 双方括号，目标通常未建，resolved=False。
"""
from __future__ import annotations
import re
import posixpath
from dataclasses import dataclass

import yaml

_FM_RE = re.compile(r"^---\s*\n(.*?\n)---\s*\n?(.*)$", re.S)
_MD_LINK_RE = re.compile(r'(?<!\!)\[([^\]]+)\]\(([^)\s]+?)(?:\s+"[^"]*")?\)')
_PLACEHOLDER_RE = re.compile(r"\[\[([^\]]+)\]\]")
_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\([^)]*\)")

# 小节标题关键词 -> 关系类型（小写包含匹配）
# 顺序敏感：小写包含首次匹配命中（更具体的关键词放前面，如"关联命令"在"命令"前）
_HEADING_RULES: list[tuple[str, str]] = [
    ("操作的配置对象", "operates_on"),
    ("操作本对象的命令", "operated_by"),
    ("关联任务", "has_task"),
    ("关联命令", "ref_command"),
    ("命令", "ref_command"),
    ("所属目录", "parent"),
    ("子特性", "child"),
    ("所需", "requires_license"),       # 所需 License / 所需的License
    ("控制的能力", "controls_feature"),
    ("关联对象", "relates_to"),
    ("证据", "evidenced_by"),
    ("depends_on", "depends_on"),
    ("conflicts_with", "conflicts_with"),
    ("interacts_with", "interacts_with"),
    ("affects", "affects"),
    ("supports", "supports"),
]
_DEFAULT_RELATION = "related"


@dataclass(frozen=True)
class RawLink:
    dst: str
    relation_type: str
    resolved: bool


def split_front_matter(text: str) -> tuple[str, str]:
    m = _FM_RE.match(text)
    if not m:
        return "", text
    return m.group(1), m.group(2)


def parse_front_matter(fm: str) -> dict:
    if not fm.strip():
        return {}
    data = yaml.safe_load(fm)
    return data or {}


def relation_for_heading(heading: str) -> str:
    h = heading.strip().lower()
    for kw, rel in _HEADING_RULES:
        if kw.lower() in h:
            return rel
    return _DEFAULT_RELATION


def object_type_of(obj_id: str) -> str:
    parts = obj_id.split("@")
    # 四段式 {nf}@{version}@{ObjectType}@{local} 或 两段式 {ObjectType}@{slug}
    if len(parts) >= 4:
        return parts[2]
    if len(parts) == 2:
        return parts[0]
    return ""


def _normalize_href(href: str) -> str:
    """assets 根相对规范化（容忍偶发 ../）。"""
    if href.startswith(("http://", "https://", "data:", "#", "mailto:")):
        return href
    return posixpath.normpath(href).replace("\\", "/")


def extract_links(body: str) -> list[RawLink]:
    """逐行扫描正文，按当前 ## 小节推断关系类型，抽 markdown 链接 + [[ID]] 占位。"""
    # 先移除图片，避免图片 alt 被当成链接
    body_no_img = _IMAGE_RE.sub("", body)
    current_relation = _DEFAULT_RELATION
    out: list[RawLink] = []
    for line in body_no_img.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("#"):
            heading = stripped.lstrip("#").strip()
            current_relation = relation_for_heading(heading)
            continue
        for _text, raw_href in _MD_LINK_RE.findall(line):
            href = _normalize_href(raw_href)
            if not href.endswith(".md"):
                continue
            out.append(RawLink(dst=href, relation_type=current_relation, resolved=True))
        for pid in _PLACEHOLDER_RE.findall(line):
            out.append(RawLink(dst=pid, relation_type=current_relation, resolved=False))
    # 去重（同 dst+relation）
    seen: set[tuple[str, str]] = set()
    dedup: list[RawLink] = []
    for lk in out:
        key = (lk.dst, lk.relation_type)
        if key in seen:
            continue
        seen.add(key)
        dedup.append(lk)
    return dedup
