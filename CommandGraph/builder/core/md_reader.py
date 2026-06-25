"""MML 命令 md 读取器（章节级解析，正道）。

从旧 command-graph/builder/md_reader.py 移植；唯一差异：
  map_section 不再读硬编码 _SECTION_TO_FIELD，改为加载同包 sections.yaml
  （启动读一次缓存）。匹配逻辑（精确 + 前缀两段）与 _FIELDS 推导保持一致。

按标题把 md 切成章节，归一化为 RawCommand 中间表示：
- H1（#）= 命令主标题，解析"中文（英文命令码）"；解析失败 = 非命令文件，返回 None
- H2/H4（##/####）= 章节标题，按文本匹配（不按层级，因实测 H2/H4 混用）
- 跳过 H1 后的 TOC（- [文字](#anchor) 行）
- "参数说明"章节归入 parameter_description（属 CommandParameter 对象，下游再用）
"""
import functools
import os
import re
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError as exc:  # pragma: no cover - 环境问题
    raise ImportError("CommandGraph 需要 PyYAML：pip install pyyaml") from exc

_H1_RE = re.compile(r'^(.+?)[（(]\s*([A-Za-z0-9][A-Za-z0-9 _\-]*?)\s*[）)]\s*$')
_HEAD_RE = re.compile(r'^(#{1,6})\s+(.*)')
_LINK_RE = re.compile(r'\[([^\]]*)\]\([^)]*\)')
_TOC_RE = re.compile(r'^\s*-\s+\[[^\]]*\]\([^)]*\)')

_SECTIONS_YAML = Path(__file__).resolve().parent.parent / "sections.yaml"


@functools.lru_cache(maxsize=1)
def _load_section_mappings():
    """读 sections.yaml 一次，返回 (exact_list, fields_tuple)。

    exact_list 保持声明顺序，供 map_section 做精确→前缀两段匹配。
    fields_tuple 为去重后的字段集合（保持首次出现顺序），供 _FIELDS 使用。
    """
    data = yaml.safe_load(_SECTIONS_YAML.read_text(encoding="utf-8"))
    seen = []
    fields = []
    for item in data["mappings"]:
        pair = (item["section"], item["field"])
        seen.append(pair)
        if item["field"] not in fields:
            fields.append(item["field"])
    return tuple(seen), tuple(fields)


# 需要收集的章节字段（从 sections.yaml 推导，保持顺序）
def _fields():
    return _load_section_mappings()[1]


def _clean_link(title):
    return _LINK_RE.sub(r'\1', title).strip()


def map_section(title):
    """章节标题 → 字段名；未映射返回 None。

    先精确匹配，再前缀匹配（前缀用于脏数据如"操作用户权限DSP RU"）。
    """
    title = _clean_link(title)
    exact_list, _ = _load_section_mappings()
    for name, field in exact_list:
        if title == name:
            return field
    for name, field in exact_list:
        if title.startswith(name):
            return field
    return None


def parse_md(path, root):
    """解析单个 md → RawCommand dict；非命令文件返回 None。

    root: 计算 category_path / source_path 的基准目录（通常为 MML命令目录的更上一级，
          即 project_root，使 source_path 为相对 SFCGraph 根的路径）。
    """
    try:
        with open(path, encoding='utf-8') as f:
            lines = f.read().split('\n')
    except Exception:
        return None

    # 1. H1 命令名
    h1 = None
    for line in lines:
        if line.startswith('# ') and not line.startswith('## '):
            h1 = line[2:].strip()
            break
    if not h1:
        return None
    h1 = _clean_link(h1)
    m = _H1_RE.match(h1)
    if not m:
        return None                       # 非命令文件（申明/目录页）
    command_code = m.group(2).strip()
    command_name_zh = m.group(1).strip()

    # 2. 扫章节（按文本，不按层级）
    sections = defaultdict(list)
    cur_field = None
    cur_lines = []

    def flush():
        if cur_field and cur_lines:
            sections[cur_field].append('\n'.join(cur_lines).strip())

    for line in lines:
        if line.startswith('# ') and not line.startswith('## '):
            continue                      # H1 跳过
        hm = _HEAD_RE.match(line)
        if hm:                            # H2~H6 章节标题
            flush()
            cur_field = map_section(hm.group(2).strip())
            cur_lines = []
            continue
        if _TOC_RE.match(line):
            continue                      # 跳过 TOC 链接行
        if cur_field is not None:
            cur_lines.append(line)
    flush()

    # 3. category_path（相对 root 的目录链）
    rel = os.path.relpath(path, root)
    category_path = [p for p in os.path.dirname(rel).replace('\\', '/').split('/')
                     if p and p != '.'] if root else []

    raw = {
        'command_code': command_code,
        'command_name_zh': command_name_zh,
        'category_path': category_path,
        'source_path': rel.replace('\\', '/') if root else path,
    }
    for fld in _fields():
        raw[fld] = '\n'.join(sections.get(fld, [])).strip()
    return raw
