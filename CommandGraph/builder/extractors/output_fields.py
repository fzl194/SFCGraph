"""派生字段 output_fields：output_description 里'输出项名称|输出项解释'表。

从旧 enrich_mmlcommand.output_fields 移植。
"""
import re

from .registry import register


def output_fields(output_desc):
    """输出字段表 [{field, description}]，只解析"输出项名称|输出项解释"表头的表。"""
    if not output_desc:
        return []
    m = re.search(r'输出项名称\s*\|\s*输出项(?:解释|说明|描述)', output_desc)
    if not m:
        return []
    after = output_desc[m.end():]
    rows = re.findall(r'^\|\s*([^|\n]+?)\s*\|\s*([^|\n]+?)\s*\|', after, re.M)
    result = []
    for field, desc in rows:
        f = field.strip()
        if set(f) <= set('-: '):
            continue
        result.append({'field': f, 'description': desc.strip()})
    return result


@register('output_fields')
def extract(cmd: dict):
    """cmd.output_description → [{field, description}, ...]；无表返回 []。"""
    return output_fields(cmd.get('output_description', ''))
