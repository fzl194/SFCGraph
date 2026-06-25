"""MMLCommand 基本身份推导（17 基本字段）。

从旧 command-graph/builder/build_mmlcommand.py 移植 to_mmlcommand / split_code，
逻辑不变；只搬不改。status 用 builder.constants.ACTIVE_STATUS。
"""
from ..constants import ACTIVE_STATUS


def split_code(code):
    """命令码 → (verb, object_keyword)，按首个空白切分。"""
    parts = code.split(None, 1)
    return (parts[0] if parts else ''), (parts[1] if len(parts) > 1 else '')


def to_mmlcommand(raw, nf, version, md_path):
    """RawCommand → MMLCommand 节点（17 基本字段，含 nf 不改名）。

    raw:        md_reader.parse_md 的返回
    nf/version: 网元类型 / 版本（如 UDG / 20.15.2）
    md_path:    md 相对 SFCGraph 根的路径，写入 source_evidence_ids
    """
    code = raw['command_code']
    verb, keyword = split_code(code)
    notes = raw['notes_text']
    examples = raw['examples_text']
    return {
        'nf': nf,
        'version': version,
        'command_id': f'{nf}@{version}@MMLCommand@{code}',
        'command_name': code,
        'command_name_zh': raw['command_name_zh'],
        'verb': verb,
        'object_keyword': keyword,
        'command_function': raw['function_text'],
        'notes': [notes] if notes else [],
        'permission_text': raw['permission_text'],
        'parameter_description': raw['parameter_description'],
        'usage_examples': [examples] if examples else [],
        'output_description': raw['output_text'],
        'reference_info': raw['reference_text'],
        'category_path': raw['category_path'],
        'status': ACTIVE_STATUS,
        'source_evidence_ids': [md_path],
    }
