"""派生字段 spec_threshold：超阈值告警结构（alarm_id/ratio/recover_ratio/modify_command）。

从旧 enrich_mmlcommand.spec_threshold 移植。
"""
import re

from .registry import register


def _as_text(v):
    return '\n'.join(v) if isinstance(v, list) else (v or '')


def spec_threshold(notes):
    """超阈值告警 {alarm_id, ratio, recover_ratio, modify_command}，从 notes 提取。"""
    t = _as_text(notes)
    if 'ALM-' not in t:
        return None
    alarm = re.search(r'ALM-\d+', t)
    if not alarm:
        return None
    ratio = re.search(r'大于规格的?(\d+)%|规格的?(\d+)%', t)
    recover = re.search(r'小于等于(?:配置规格|规格)?\s*(\d+)%', t)
    modify = re.search(r'通过\s*([A-Z]+\s+[A-Z0-9_]+)\s*命令修改', t)
    return {
        'alarm_id': alarm.group(0),
        'ratio': (ratio.group(1) or ratio.group(2)) if ratio else '',
        'recover_ratio': recover.group(1) if recover else '',
        'modify_command': modify.group(1) if modify else '',
    }


@register('spec_threshold')
def extract(cmd: dict):
    """cmd.notes → 告警结构或 None。"""
    return spec_threshold(cmd.get('notes', []))
