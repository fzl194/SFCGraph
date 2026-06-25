"""派生字段 initial_values：notes 里'系统初始记录'表的 参数名→初始值。

从旧 enrich_mmlcommand.initial_values 移植。
"""
import re

from .registry import register


def _as_text(v):
    return '\n'.join(v) if isinstance(v, list) else (v or '')


def initial_values(notes):
    """系统初始记录（参数名→初始值），解析 notes 里的初始值表。"""
    t = _as_text(notes)
    if '系统初始记录' not in t and '初始设置值' not in t:
        return {}
    m = re.search(r'参数标识\s*\|([^\n]+)\n\|[^\n]+\n\|\s*初始值\s*\|([^\n]+)', t)
    if not m:
        return {}
    keys = [k.strip() for k in m.group(1).split('|') if k.strip()]
    vals = [v.strip() for v in m.group(2).split('|') if v.strip()]
    return dict(zip(keys, vals))


@register('initial_values')
def extract(cmd: dict):
    """cmd.notes → {参数名: 初始值}；无表返回 {}。"""
    return initial_values(cmd.get('notes', []))
