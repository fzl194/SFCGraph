"""派生字段 applicable_nf：从 command_function 提适用 NF 列表。

从旧 enrich_mmlcommand.applicable_nf 移植。
"""
import re

from .registry import register

_NF_RE = re.compile(r'适用(?:NF|网元|设备)[：:]\s*([^。<\n]+)')


def applicable_nf(func):
    if not func:
        return []
    m = _NF_RE.search(func)
    if not m:
        return []
    items = [re.sub(r'[*_`]+', '', x).strip() for x in re.split(r'[、,，;；]', m.group(1))]
    return [x for x in items if x]


@register('applicable_nf')
def extract(cmd: dict):
    """cmd.command_function → ['UDG', ...]；未提及返回 []。"""
    return applicable_nf(cmd.get('command_function', ''))
