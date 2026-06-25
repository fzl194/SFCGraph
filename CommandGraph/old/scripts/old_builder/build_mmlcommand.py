"""从产品文档构建 MMLCommand 图谱节点（通用程序）。

输入：产品文档数据源（UDG kgdata CSV；UNC MD reader 后续同接口接入）
输出：符合 COMMAND_GRAPH_SCHEMA.md §3.3 的 MMLCommand 节点（JSONL）

通用性：网元、版本由 --nf / --version 传入，不硬编码；实例键 = 网元@版本:命令名。
当前实现：kgdata 基础字段（命令码/名称/功能/注意事项/实例/权限/输出说明）。
后续扩展：notes 结构化字段提取（effect_mode/max_records/spec_threshold/...）、
        category_path（从 MD 目录补）、UNC md_reader。
"""
import argparse
import json
import re
from pathlib import Path

from kgdata_reader import read_kgdata

# verb → command_category 分类
_CONFIG_VERBS = {'ADD', 'MOD', 'DEL', 'SET', 'RMV'}
_QUERY_VERBS = {'LST', 'DSP'}
_ACTION_VERBS = {'SWP', 'RST', 'CLR', 'SYN', 'ACT', 'DEACT', 'SWAP'}

_NF_RE = re.compile(r'适用NF[：:]\s*([^。<\n]+)')
_PERM_RE = re.compile(r'G_\d+')


def split_command_code(code: str):
    """命令码 'DSP FABRICSUBHEALTHYLINK' → (verb='DSP', keyword='FABRICSUBHEALTHYLINK')。"""
    code = code.strip()
    parts = code.split(None, 1)
    verb = parts[0] if parts else ''
    keyword = parts[1] if len(parts) > 1 else ''
    return verb, keyword


def classify_category(verb: str) -> str:
    if verb in _CONFIG_VERBS:
        return '配置类'
    if verb in _QUERY_VERBS:
        return '查询类'
    if verb in _ACTION_VERBS:
        return '动作类'
    return '调测类'


def extract_nf(func_text: str):
    """从命令功能文本提取 '适用NF：PGW-U、UPF'。"""
    if not func_text:
        return []
    m = _NF_RE.search(func_text)
    if not m:
        return []
    return [x.strip() for x in re.split(r'[、,，;；]', m.group(1)) if x.strip()]


def parse_permission_groups(s: str):
    return _PERM_RE.findall(s) if s else []


def notes_to_list(notes_text: str):
    if not notes_text:
        return []
    return [ln for ln in notes_text.split('\n') if ln.strip()]


def build_one(name: str, attrs: dict, nf: str, version: str) -> dict:
    code = attrs.get('命令码', '')              # 已 decode：'DSP FABRICSUBHEALTHYLINK'
    verb, keyword = split_command_code(code)
    func_text = attrs.get('命令功能', '')
    return {
        'command_id': f'{nf}@{version}:{code}' if code else '',
        'command_name': code,
        'command_name_zh': attrs.get('命令名称', ''),
        'verb': verb,
        'object_keyword': keyword,
        'command_category': classify_category(verb),
        'applicable_nf': extract_nf(func_text),
        'command_function': func_text,
        'notes': notes_to_list(attrs.get('注意事项', '')),
        'usage_examples': attrs.get('使用实例', ''),
        'permission_groups': parse_permission_groups(attrs.get('操作用户权限', '')),
        'output_description': attrs.get('输出结果说明', ''),   # 原文，后续解析 output_fields/output_ref_command
        'source_evidence_ids': [v for v in (attrs.get('_topic_id', ''),
                                            attrs.get('_topic_path', '')) if v],
        'status': 'active',
        '_kgdata_name': name,
    }


def main():
    ap = argparse.ArgumentParser(description='构建 MMLCommand 图谱节点')
    ap.add_argument('--input-dir', default='command-graph/data/kgdata',
                    help='kgdata CSV 所在目录')
    ap.add_argument('--input-glob', default='UDG_MML命令_*.csv',
                    help='kgdata CSV 文件通配（按产品调整）')
    ap.add_argument('--output', default='command-graph/data/output/mml_commands.jsonl')
    ap.add_argument('--nf', required=True, help='网元类型，如 UDG / UNC')
    ap.add_argument('--version', required=True, help='版本，如 20.15.2')
    args = ap.parse_args()

    csv_paths = sorted(Path(args.input_dir).glob(args.input_glob))
    if not csv_paths:
        raise SystemExit(f'未找到 kgdata CSV: {args.input_dir}/{args.input_glob}')

    commands = read_kgdata(csv_paths)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)

    seen = set()
    n = 0
    with out.open('w', encoding='utf-8') as f:
        for name, attrs in commands.items():
            obj = build_one(name, attrs, args.nf, args.version)
            cid = obj['command_id']
            if not cid or cid in seen:
                continue
            seen.add(cid)
            f.write(json.dumps(obj, ensure_ascii=False) + '\n')
            n += 1
    print(f'built {n} MMLCommands → {out}')


if __name__ == '__main__':
    main()
