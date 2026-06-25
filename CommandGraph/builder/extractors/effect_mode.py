"""派生字段 effect_mode：notes 里的生效方式（对新用户/对新流/延迟/立即）。

从旧 enrich_mmlcommand.effect_mode 移植。
"""
import re

from .registry import register


def _as_text(v):
    return '\n'.join(v) if isinstance(v, list) else (v or '')


def effect_mode(notes):
    """生效方式：优先级 对新用户 > 对新流 > 延迟 > 立即（取最显著）。"""
    t = _as_text(notes)
    if not t:
        return ''
    if re.search(r'对新激活用户|对新用户', t):
        return '对新用户生效'
    if re.search(r'对新数据流|对流生效', t):
        return '对新流生效'
    if re.search(r'\d+\s*秒.*?生效|秒[内后]生效', t):
        return '延迟生效'
    if re.search(r'立即生效', t):
        return '立即生效'
    return ''


@register('effect_mode')
def extract(cmd: dict):
    """cmd.notes → 生效方式字符串；无则 ''。"""
    return effect_mode(cmd.get('notes', []))
