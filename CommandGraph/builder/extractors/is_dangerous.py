"""派生字段 is_dangerous：notes/function 含'高危命令'等 → True。

从旧 enrich_mmlcommand.is_dangerous 移植。
"""
import re

from .registry import register

_DANGER_RE = re.compile(r'高危命令|属于高危')


def _as_text(v):
    return '\n'.join(v) if isinstance(v, list) else (v or '')


def is_dangerous(notes, func):
    txt = _as_text(notes) + ' ' + (func or '')
    return bool(_DANGER_RE.search(txt))


@register('is_dangerous')
def extract(cmd: dict):
    """cmd.notes + cmd.command_function → bool。"""
    return is_dangerous(cmd.get('notes', []), cmd.get('command_function', ''))
