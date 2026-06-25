"""派生字段 max_records：从 notes 提'最大记录数为 N'。

从旧 enrich_mmlcommand.max_records 移植。
"""
import re

from .registry import register

_MAXREC_RE = re.compile(r'最大记录数[为是]?\s*(\d+)')


def _as_text(v):
    return '\n'.join(v) if isinstance(v, list) else (v or '')


def max_records(notes):
    m = _MAXREC_RE.search(_as_text(notes))
    return int(m.group(1)) if m else None


@register('max_records')
def extract(cmd: dict):
    """cmd.notes → int 或 None。"""
    return max_records(cmd.get('notes', []))
