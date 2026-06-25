"""派生字段 command_category：verb → 命令分类。

从旧 enrich_mmlcommand.command_category 移植；_VERB_CATEGORY 一并搬来。
"""
import re

from .registry import register

# verb → command_category 映射（自拟，待校准，标 needs_review）
_VERB_CATEGORY = [
    ('配置类', {'ADD', 'MOD', 'DEL', 'SET', 'RMV'}),
    ('查询类', {'LST', 'DSP'}),
    ('动作类', {'SWP', 'RST', 'SWAP', 'ACT', 'DEACT', 'STR', 'STP', 'CLR', 'LOD',
              'SYN', 'DEA', 'EXP', 'RBL', 'LCK', 'ULK', 'UPL', 'SAV', 'OPR', 'UPD', 'RTR'}),
]


def command_category(verb):
    for cat, verbs in _VERB_CATEGORY:
        if verb in verbs:
            return cat
    return '调测类'


@register('command_category')
def extract(cmd: dict):
    """cmd.command_name 拆出的 verb → 分类；未命中归'调测类'。"""
    return command_category(cmd.get('verb', ''))
