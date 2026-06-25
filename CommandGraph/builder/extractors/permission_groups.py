"""派生字段 permission_groups：从 permission_text 提 G_xxx 权限组。

从旧 enrich_mmlcommand.permission_groups 移植。
"""
import re

from .registry import register

_PERM_RE = re.compile(r'G_\d+')


def permission_groups(perm_text):
    return _PERM_RE.findall(perm_text or '')


@register('permission_groups')
def extract(cmd: dict):
    """cmd.permission_text → ['G_1', ...]；未提及返回 []。"""
    return permission_groups(cmd.get('permission_text', ''))
