"""ConfigObject 聚合逻辑：mml_commands + command_parameters + 内网规则表
（MOD/重复/RMV）→ ConfigObject 节点 + 命令→对象关系边。

对齐 COMMAND_GRAPH_SCHEMA.md §3.2（ConfigObject 终版字段）。
字段来源：
  - object_id/object_name/object_name_zh/object_kind/applicable_nf/description/
    status/source_evidence_ids ← mml_commands（命令层，全量）
  - attribute_names             ← command_parameters（ADD/MOD/SET 参数）∪ output_fields
  - identifier_parameters       ← MOD 规则"索引参数"（RMV 规则补充）
  - uniqueness_keys             ← 重复规则"重复检查"
"""
import csv
import json
from pathlib import Path

from ..params import load_rows as load_table_rows  # csv/xlsx(第一个 sheet) 通用 reader

# ---- verb 分类（object_kind 判定 + command_object_edges relation_type）----
CRUD_VERBS = {"ADD", "MOD", "DEL", "RMV"}
QUERY_VERBS = {"LST", "DSP"}
ACTION_VERBS = {
    "SWP", "RST", "CLR", "STP", "LOD", "SYN", "RTR", "EXP", "IMP", "ACT",
    "BKP", "CHK", "COL", "RBL", "FTR", "OPR", "STR", "CLB", "TST", "SND",
    "RUN", "CVT", "GEN", "SRT", "PWR", "LCK", "CMD", "DEA", "SAV", "ULD",
    "REQ", "EXC",
}

# object_name_zh 去动词前缀（最长匹配）
ZH_VERB_PREFIXES = [
    "去激活", "去活", "增加", "添加", "修改", "删除", "查询", "显示",
    "设置", "配置", "激活", "清除", "刷新", "加载", "卸载", "启动",
    "停止", "导出", "导入", "备份", "恢复", "执行", "重置",
]

# verb → command_object_edge relation_type（对齐 schema §4.3）
VERB_TO_RELATION = {
    "ADD": "creates",
    "MOD": "modifies",
    "DEL": "deletes",
    "RMV": "deletes",
    "SET": "sets",
    "LST": "queries",
    "DSP": "queries",
}


def split_command(command_name):
    """命令全名 → (verb, object_name)，按首个空白切。"""
    parts = (command_name or "").split(None, 1)
    verb = parts[0] if parts else ""
    obj = parts[1] if len(parts) > 1 else ""
    return verb, obj


def classify_kind(object_name, verbs):
    """按命令族 verb 画像 + 命名判定 object_kind（5 类，优先级从上到下，命中即停）。"""
    vs = {v for v in verbs if v}
    upper = (object_name or "").upper()
    has_crud = bool(vs & CRUD_VERBS)
    has_set = "SET" in vs
    qry_only = bool(vs) and vs <= QUERY_VERBS
    non_query = vs - QUERY_VERBS
    act_only = bool(non_query) and non_query <= ACTION_VERBS

    if "BIND" in upper and ({"ADD", "RMV"} & vs):
        return "binding"
    if qry_only:
        return "query_target"
    if act_only and not has_crud and not has_set:
        return "action"
    if has_set and not has_crud:
        return "global_setting"
    if has_crud:
        return "entity"
    return "action"  # 兜底


def strip_verb_prefix(command_name_zh):
    """command_name_zh 去最长匹配的中文动词前缀，得 object_name_zh 初值。"""
    zh = (command_name_zh or "").strip()
    if not zh:
        return ""
    for v in sorted(ZH_VERB_PREFIXES, key=len, reverse=True):
        if zh.startswith(v):
            return zh[len(v):]
    return zh


def _split_param_list(text):
    """'APN,SWITCH' → ['APN', 'SWITCH']。"""
    if not text:
        return []
    return [p.strip() for p in text.split(",") if p.strip()]


# ---- 规则表加载（按 object_name 关联）----

def load_mod_rules(path):
    """MOD规则（csv/xlsx）→ {object_name: [索引参数]}。MOD命令='MOD XXX'，XXX=object_name。"""
    rules = {}
    if not path or not Path(path).exists():
        return rules
    for row in load_table_rows(path):
        _, obj = split_command((row.get("MOD 命令") or "").strip())
        if not obj:
            continue
        idx = _split_param_list(row.get("索引参数"))
        if obj not in rules and idx:
            rules[obj] = idx
    return rules


def load_rmv_rules(path):
    """RMV规则（csv/xlsx）→ {object_name: [索引参数]}。RMV命令='RMV XXX'。"""
    rules = {}
    if not path or not Path(path).exists():
        return rules
    for row in load_table_rows(path):
        _, obj = split_command((row.get("RMV 命令") or "").strip())
        if not obj:
            continue
        idx = _split_param_list(row.get("索引参数"))
        if obj not in rules and idx:
            rules[obj] = idx
    return rules


def load_uniqueness_rules(path):
    """重复规则（csv/xlsx）→ {object_name: [[唯一键参数]]}。命令名称='ADD XXX'，XXX=object_name。"""
    rules = {}
    if not path or not Path(path).exists():
        return rules
    for row in load_table_rows(path):
        _, obj = split_command((row.get("命令名称") or "").strip())
        if not obj:
            continue
        check = _split_param_list(row.get("重复检查"))
        if obj not in rules and check:
            rules[obj] = [check]  # list[list[str]]，预留多组
    return rules


# ---- jsonl ----

def load_jsonl(path):
    """读 jsonl → list[dict]。文件不存在返回 []。"""
    records = []
    if not path or not Path(path).exists():
        return records
    with Path(path).open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def write_jsonl(path, items):
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        for item in items:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")


# ---- 聚合 ----

def build_config_objects(nf, version, mml_commands, command_parameters,
                         mod_rules, rmv_rules, uniq_rules):
    """聚合 ConfigObject + 命令→对象边。

    返回 {"objects": [...], "edges": [...]}。
    """
    families = {}  # object_name → list[command]
    for cmd in mml_commands:
        obj = (cmd.get("object_keyword") or "").strip()
        if not obj:
            continue
        families.setdefault(obj, []).append(cmd)

    params_by_cmd = {}  # command_id → list[parameter]
    for p in command_parameters:
        params_by_cmd.setdefault(p.get("command_id") or "", []).append(p)

    objects = []
    edges = []
    for object_name, cmds in sorted(families.items()):
        obj = _build_one_object(nf, version, object_name, cmds, params_by_cmd,
                                mod_rules, rmv_rules, uniq_rules)
        objects.append(obj)
        for cmd in cmds:
            edges.append(_build_edge(cmd, obj["object_id"]))
    return {"objects": objects, "edges": edges}


def _build_one_object(nf, version, object_name, cmds, params_by_cmd,
                      mod_rules, rmv_rules, uniq_rules):
    verbs = [c.get("verb") or "" for c in cmds]
    zh_raw = next((c.get("command_name_zh") for c in cmds if c.get("command_name_zh")), "")
    return {
        "object_id": f"{nf}@{version}@ConfigObject@{object_name}",
        "nf": nf,
        "version": version,
        "object_name": object_name,
        "object_name_zh": strip_verb_prefix(zh_raw),
        "object_kind": classify_kind(object_name, verbs),
        "applicable_nf": _union(cmds, "applicable_nf"),
        "identifier_parameters": mod_rules.get(object_name) or rmv_rules.get(object_name) or [],
        "uniqueness_keys": uniq_rules.get(object_name) or [],
        "attribute_names": _collect_attributes(cmds, params_by_cmd),
        "description": _pick_description(cmds),
        "status": "active",
        "source_evidence_ids": _union(cmds, "source_evidence_ids"),
    }


def _union(cmds, field):
    """族命令某 list 字段并集，保序去重。"""
    out = []
    for c in cmds:
        for item in (c.get(field) or []):
            if item and item not in out:
                out.append(item)
    return out


def _pick_description(cmds):
    """族内 ADD 命令 command_function 优先（无 ADD → MOD → SET → 任意）。"""
    for prefer in ("ADD", "MOD", "SET", "DEL", "RMV"):
        for c in cmds:
            if c.get("verb") == prefer and c.get("command_function"):
                return c["command_function"]
    return next((c.get("command_function") for c in cmds if c.get("command_function")), "")


def _collect_attributes(cmds, params_by_cmd):
    """族内 ADD/MOD/SET 命令参数名（可配置属性），去重保序。

    不含 LST/DSP 输出字段——output_fields 是查询输出结构，不是配置属性，
    留在 MMLCommand.output_fields。
    """
    attrs = []
    for c in cmds:
        if c.get("verb") in {"ADD", "MOD", "SET"}:
            for p in params_by_cmd.get(c.get("command_id") or "", []):
                pname = p.get("parameter_name")
                if pname and pname not in attrs:
                    attrs.append(pname)
    return attrs


def _build_edge(cmd, object_id):
    """一条命令 → 其 ConfigObject 的关系边。verb→relation_type。"""
    verb = cmd.get("verb") or ""
    relation = VERB_TO_RELATION.get(verb, "operates_on")
    return {
        "edge_type": relation,
        "from_command_ref": cmd.get("command_id") or "",
        "to_object_ref": object_id,
    }
