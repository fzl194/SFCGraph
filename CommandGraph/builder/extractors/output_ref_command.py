"""派生字段 output_ref_command：从 output_description 提'参见 XXX 的输出说明'。

从旧 enrich_mmlcommand.output_ref_command 移植。
"""
import re

from .registry import register


def output_ref_command(output_desc):
    if not output_desc:
        return ''
    text = re.sub(r'\*\*', '', output_desc)
    text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text)
    m = re.search(r'参见[的命令\s]*([A-Z][A-Z0-9_]*(?:\s+[A-Z0-9_]+)*)', text)
    return m.group(1).strip() if m else ''


@register('output_ref_command')
def extract(cmd: dict):
    """cmd.output_description → 参见的目标命令码字符串；无则 ''。"""
    return output_ref_command(cmd.get('output_description', ''))
