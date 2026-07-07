#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BusinessGraph YAML 生成器
========================
从 business-graph/{计费,带宽控制,访问限制}场景/three-layer-graph/01-business-graph.md
解析业务层对象（BD / NS / CS / DP），按 ConfigTask assert yaml 的风格输出到
BusinessGraph/{business_domains, scenarios/<dir>/...}。

设计约束（与用户对齐结果）：
- 业务层只产 3 类对象 yaml: BusinessDomain / NetworkScenario / ConfigurationSolution
- 一个 yaml = 一个对象；关系承载在字段里
- 特性(Feature) 作为 CS 的 uses_feature 字段（仅引用 ID，不展开，已有 jsonl）
- 决策点(DecisionPoint) 嵌套字段，不单独建 yaml
  * 落位规则（权威信号 = 关系边 has_decision，而非 DP 表 owner_ref）：
    - 单 CS 独占且无 NS 归属 → 全量嵌在该 CS yaml
    - 多 CS 共享 / NS 归属 / NS-CS 冲突 → 全量嵌在 NS yaml
  * CS 侧带 applies_decision_refs 回指"影响本 CS 但嵌在别处"的 DP
- BR / SO / constrained_by / uses_semantic_object 一律不输出（用户要求不考虑）

重跑: python BusinessGraph/scripts/gen_from_business_graph.py
"""
from __future__ import annotations
import re
import sys
from pathlib import Path
import yaml

REPO = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO / "business-graph"
OUT_ROOT = REPO / "BusinessGraph"

# 源数据中三场景各自用不同 BD ID 指向同一根对象「业务感知」，统一为一个 ID
UNIFIED_BD_ID = "BD-BSA-01"

SCENARIOS = [
    {
        "key": "charging", "dir": "charging", "slug_zh": "计费场景",
        "src": SRC_ROOT / "计费场景" / "three-layer-graph" / "01-business-graph.md",
        "ns_id": "NS-CH-01", "cs_prefix": "CH", "dp_prefix": "DP-CH",
    },
    {
        "key": "bandwidth", "dir": "bandwidth", "slug_zh": "带宽控制场景",
        "src": SRC_ROOT / "带宽控制场景" / "three-layer-graph" / "01-business-graph.md",
        "ns_id": "NS-BW-01", "cs_prefix": "BW", "dp_prefix": "DP-BW",
    },
    {
        "key": "access-control", "dir": "access-control", "slug_zh": "访问限制场景",
        "src": SRC_ROOT / "访问限制场景" / "three-layer-graph" / "01-business-graph.md",
        "ns_id": "NS-AC-01", "cs_prefix": "AC", "dp_prefix": "DP-AC",
    },
]


# ----------------- 文本 / 表格解析工具 -----------------

def strip_bt(s: str) -> str:
    """去首尾反引号与空白。"""
    return s.strip().strip("`").strip()


def _clean_tok(t: str) -> str:
    """剥掉 token 内全部 markdown 反引号/引号（在这类 ID/选项 token 里反引号纯属格式，非语义）。"""
    return t.strip().replace("`", "").strip("'\"").strip()


def split_top(s: str, seps="、,，;；") -> list[str]:
    """按分隔符切分，但不在括号 (（）<>) 内切；每段剥外层反引号/引号。"""
    out, buf, depth = [], [], 0
    for ch in s:
        if ch in "（(<[":
            depth += 1; buf.append(ch)
        elif ch in "）)>]" and depth > 0:
            depth -= 1; buf.append(ch)
        elif depth == 0 and ch in seps:
            t = _clean_tok("".join(buf))
            if t:
                out.append(t)
            buf = []
        else:
            buf.append(ch)
    t = _clean_tok("".join(buf))
    if t:
        out.append(t)
    return out


def parse_field_table(block: str) -> dict[str, str]:
    """
    解析形如
        | 字段 | 值 |
        |------|---|
        | `key` | `value` |
    的两列字段表 → {key: value}（value 去反引号）。
    跳过表头/分隔行；value 保留括号内细节。
    """
    fields: dict[str, str] = {}
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|") or "---" in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        key = strip_bt(cells[0])
        val = strip_bt(cells[1])
        if key in ("字段", "field", ""):
            continue
        # 跳过 wide-table 的纯列头（被当作 key 时通常含中文列名且 value 也是列名）
        fields[key] = val
    return fields


def parse_wide_table(block: str, header_keys: list[str]) -> list[dict[str, str]]:
    """
    解析多列表格（如 DP 表 / 关系边表），按表头列名映射。
    header_keys: 期望的列名（按顺序），用于匹配表头行；表头里出现的反引号字段名优先。
    """
    rows_raw = [l.strip() for l in block.splitlines()
                if l.strip().startswith("|") and "---" not in l]
    if not rows_raw:
        return []
    header = [strip_bt(c) for c in rows_raw[0].strip("|").split("|")]
    # 建立列名→index，兼容反引号原值
    colidx: dict[str, int] = {}
    for i, h in enumerate(header):
        if h:
            colidx.setdefault(h, i)
    out = []
    for line in rows_raw[1:]:
        cells = [c.strip() for c in line.strip("|").split("|")]
        row = {}
        for key in header_keys:
            # 尝试多种匹配：原名 / 去反引号 / 中文等价
            idx = None
            for cand in (key, key.strip("`")):
                if cand in colidx:
                    idx = colidx[cand]; break
            if idx is None:
                continue
            if idx < len(cells):
                row[key] = strip_bt(cells[idx])
        if row:
            out.append(row)
    return out


def find_section(md: str, title_pattern: str) -> tuple[int, int]:
    """定位一个 ## 段落（标题行匹配 title_pattern），返回 (start_line_idx, end_line_idx)。end 为下一个同级或更高级标题前。"""
    lines = md.splitlines()
    start = None
    for i, ln in enumerate(lines):
        if ln.startswith("## ") and re.search(title_pattern, ln):
            start = i; break
    if start is None:
        return -1, -1
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("## "):
            end = j; break
    return start, end


def find_subsection(block: str, title_pattern: str) -> tuple[int, int]:
    """在给定 block 文本内定位 ### 子段。"""
    lines = block.splitlines()
    start = None
    for i, ln in enumerate(lines):
        if ln.startswith("### ") and re.search(title_pattern, ln):
            start = i; break
    if start is None:
        return -1, -1
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("### "):
            end = j; break
    return start, end


def slice_section(md: str, title_pattern: str) -> str:
    s, e = find_section(md, title_pattern)
    if s < 0:
        return ""
    return "\n".join(md.splitlines()[s:e])


def slice_subsection(parent_block: str, title_pattern: str) -> str:
    s, e = find_subsection(parent_block, title_pattern)
    if s < 0:
        return ""
    return "\n".join(parent_block.splitlines()[s:e])


# ----------------- 各对象解析 -----------------

def parse_business_domain(md: str) -> dict:
    block = slice_section(md, r"BusinessDomain")
    # 取该段内第一个字段表
    tbl = parse_field_table(block)
    return {
        "domain_id": tbl.get("domain_id", ""),
        "domain_name": tbl.get("domain_name", ""),
        "domain_summary": tbl.get("domain_summary", ""),
        "status": tbl.get("status", "active"),
        "source_evidence_ids": split_top(tbl.get("source_evidence_ids", "")),
    }


def parse_network_scenario(md: str) -> dict:
    block = slice_section(md, r"NetworkScenario")
    tbl = parse_field_table(block)

    # 场景边界：覆盖范围 / 不覆盖范围（项目符号列表）
    coverage: dict[str, list[str]] = {}
    non_coverage: list[str] = []
    lines = block.splitlines()
    mode = None
    for ln in lines:
        raw = ln.strip()
        # 水平线 / 空行 / 标题 → 结束当前收集
        if not raw or re.match(r"^[-*_]{3,}\s*$", raw) or raw.startswith("#"):
            mode = None if raw.startswith("#") else mode
            continue
        # 进入新的粗体字段
        if raw.startswith("**"):
            if "不覆盖范围" in raw:
                mode = "non"; continue
            elif "覆盖范围" in raw:
                mode = "coverage"; continue
            else:
                mode = None; continue
        if mode == "coverage":
            # 支持 - 产品：... / - **产品**：... 两种写法
            m = re.match(r"-\s*\*{0,2}\s*([^：:：]+?)\s*\*{0,2}\s*[：:]\s*(.+)", raw)
            if m:
                k = m.group(1).strip()
                v = [x.strip() for x in re.split(r"[、,，]", m.group(2)) if x.strip()]
                coverage[k] = v
        elif mode == "non":
            m = re.match(r"-\s*(.+)", raw)
            if m:
                non_coverage.append(m.group(1).strip())

    return {
        "scenario_id": tbl.get("scenario_id", ""),
        "scenario_name": tbl.get("scenario_name", ""),
        "scenario_summary": tbl.get("scenario_summary", ""),
        "judgment_basis": tbl.get("judgment_basis", ""),
        "typical_outcome": tbl.get("typical_outcome", ""),
        "status": tbl.get("status", "active"),
        "source_evidence_ids": split_top(tbl.get("source_evidence_ids", "")),
        "coverage": coverage,
        "non_coverage": non_coverage,
    }


CS_FIELD_KEYS = [
    "solution_id", "solution_name", "solution_summary", "design_intent",
    "core_mechanism_combo", "status", "source_evidence_ids",
]


def parse_configuration_solutions(md: str) -> list[dict]:
    """
    解析 §2 ConfigurationSolution 段。
    每个 CS 以 `### 2.N CS-XX-YY 名称` 开头，紧跟一个字段表 + 若干 **inline** 字段。
    """
    block = slice_section(md, r"ConfigurationSolution")
    lines = block.splitlines()
    solutions: list[dict] = []

    # 切分每个 ### 子段
    sub_starts = [i for i, ln in enumerate(lines) if re.match(r"###\s+\d", ln)]
    sub_starts.append(len(lines))
    for a, b in zip(sub_starts[:-1], sub_starts[1:]):
        chunk = "\n".join(lines[a:b])
        header = lines[a]
        # 从表里拿 solution_id（兜底用 header）
        tbl = parse_field_table(chunk)
        sid = tbl.get("solution_id", "")
        if not sid:
            m = re.search(r"(CS-\w+-\d+)", header)
            if not m:
                continue
            sid = m.group(1)
        # 解析 inline 字段
        scopes = _parse_scopes(chunk)
        participants = _parse_participants(chunk)
        uses_feature_inline = _parse_id_list(chunk, "uses_feature")
        solutions.append({
            "solution_id": sid,
            "solution_name": tbl.get("solution_name", ""),
            "solution_summary": tbl.get("solution_summary", ""),
            "design_intent": tbl.get("design_intent", ""),
            "core_mechanism_combo": tbl.get("core_mechanism_combo", ""),
            "status": tbl.get("status", "active"),
            "source_evidence_ids": split_top(tbl.get("source_evidence_ids", "")),
            "scopes": scopes,
            "participants": participants,
            "uses_feature_inline": uses_feature_inline,
            "_header": header.strip(),
        })
    return solutions


def _parse_scopes(chunk: str) -> list[dict]:
    m = re.search(r"\*\*scopes?\*\*\s*:\s*(.+)", chunk)
    if not m:
        return []
    rest = m.group(1)
    # 可能跨行后续跟列表，但通常单行；取到下一个 ** 字段为止
    stop = re.search(r"\*\*", rest[1:])  # 下一个粗体
    if stop:
        rest = rest[: stop.start() + 1]
    out = []
    for tok in split_top(rest):
        mm = re.match(r"([^\(（]+)[\(（]([^)）]*)[)）]?", tok)
        if mm:
            out.append({"scope": mm.group(1).strip(), "desc": mm.group(2).strip()})
        else:
            out.append({"scope": tok.strip(), "desc": ""})
    return out


def _parse_participants(chunk: str) -> list[dict]:
    out = []
    m = re.search(r"\*\*participants?\*\*\s*:(.+?)(?:\*\*(?:uses_feature|uses_semantic_object|constrained_by|scopes)\*\*|$)",
                  chunk, flags=re.S)
    if not m:
        return out
    body = m.group(1)
    for line in body.splitlines():
        s = line.strip()
        mm = re.match(r"-\s*([^\(（]+)[\(（]([^)）]*)[)）]?", s)
        if mm:
            name = mm.group(1).strip()
            inner = mm.group(2).strip()
            layer = ""
            for L in ("user_plane", "control_plane", "external_system"):
                if L in inner:
                    layer = L; break
            role = inner
            if layer:
                role = re.sub(r"[,，]?\s*" + layer + r"\s*", "", inner).strip(" ,，")
            out.append({"name": name, "role": role, "layer": layer})
    return out


def _parse_id_list(chunk: str, field: str) -> list[str]:
    m = re.search(rf"\*\*{field}\*\*\s*:\s*(.+)", chunk)
    if not m:
        return []
    rest = m.group(1)
    out = []
    for tok in split_top(rest):
        mm = re.search(r"((?:GWFD|WSFD|IPFD|NPFD|CS|NS|BD|SO|BR|DP)-[\w-]+)", tok)
        if mm:
            out.append(mm.group(1))
        else:
            # 可能是裸特性号兜底
            t = tok.strip().strip("`")
            if re.match(r"^[A-Z]+FD-\d+$|^[A-Z]+-\d+$", t):
                out.append(t)
    return out


def parse_decision_points(md: str) -> list[dict]:
    block = slice_section(md, r"DecisionPoint")
    rows = parse_wide_table(block, [
        "decision_id", "owner_layer", "owner_ref_type", "owner_ref",
        "decision_name", "decision_question", "option_set", "trigger_condition",
        "impact_summary", "status", "source_evidence_ids",
    ])
    dps = []
    for r in rows:
        if not r.get("decision_id"):
            continue
        opt = r.get("option_set", "")
        # option_set 形如 ["a","b","c"] 或 a、b、c
        opts = []
        if opt.startswith("["):
            inner = opt.strip("[]")
            for o in re.split(r"[、,，]", inner):
                o = o.strip().strip('"').strip("'").strip()
                if o:
                    opts.append(o)
        else:
            opts = split_top(opt)
        dps.append({
            "decision_id": r.get("decision_id", ""),
            "owner_layer": r.get("owner_layer", ""),
            "owner_ref_type": r.get("owner_ref_type", ""),
            "owner_ref": r.get("owner_ref", ""),
            "decision_name": r.get("decision_name", ""),
            "decision_question": r.get("decision_question", ""),
            "option_set": opts,
            "trigger_condition": r.get("trigger_condition", ""),
            "impact_summary": r.get("impact_summary", ""),
            "status": r.get("status", "active"),
            "source_evidence_ids": split_top(r.get("source_evidence_ids", "")),
        })
    return dps


def parse_edges(md: str) -> dict:
    """
    解析「业务图谱关系边」段下的三类边：
      方案使用特性(uses_feature) / 决策点归属(has_decision) / 决策点影响(selects)
    """
    edges_block = slice_section(md, r"关系边")
    out = {"uses_feature": {}, "has_decision": {}, "selects": {}}

    uf = slice_subsection(edges_block, r"方案使用特性|uses_feature")
    for r in parse_wide_table(uf, ["起点", "关系", "终点"]):
        k = r.get("起点", "")
        if not k:
            continue
        ends = r.get("终点", "")
        ids = re.findall(r"((?:GWFD|WSFD|IPFD|NPFD)-\d+)", ends)
        if ids:
            out["uses_feature"].setdefault(k, []).extend(ids)

    hd = slice_subsection(edges_block, r"决策点归属|has_decision")
    # owner (NS/CS) → [DP]；同时反建 DP → owners
    owner_to_dps: dict[str, list[str]] = {}
    for r in parse_wide_table(hd, ["起点", "关系", "终点"]):
        owners = r.get("起点", "")
        dps = r.get("终点", "")
        owner_list = re.findall(r"((?:NS|CS)-\w+-\d+)", owners)
        dp_list = re.findall(r"(DP-\w+-\d+)", dps)
        for o in owner_list:
            owner_to_dps.setdefault(o, []).extend(dp_list)
    out["has_decision"] = owner_to_dps

    sel = slice_subsection(edges_block, r"决策点影响|selects")
    for r in parse_wide_table(sel, ["起点", "关系", "终点", "说明"]):
        dp = r.get("起点", "")
        rel = r.get("关系", "")
        end = r.get("终点", "")
        note = r.get("说明", "")
        dp_m = re.search(r"(DP-\w+-\d+)", dp)
        if not dp_m:
            continue
        dp_id = dp_m.group(1)
        if "select" in rel.lower():
            cs = re.findall(r"(CS-\w+-\d+)", end)
            if cs:
                out["selects"].setdefault(dp_id, {"solutions": [], "note": note})
                out["selects"][dp_id]["solutions"] = list(dict.fromkeys(cs))
                out["selects"][dp_id]["note"] = note
    return out


# ----------------- 落位规则 -----------------

def compute_dp_placement(dps: list[dict], has_decision: dict, ns_id: str) -> dict:
    """
    返回:
      dp_home: {dp_id: 'NS' or 'CS-XX-NN'}  全量嵌在哪
      cs_applies: {cs_id: [dp_id,...]}      影响 CS 但嵌在别处的 DP（回指）
    规则:
      - 反向收集 dp -> set(owners)
      - owners 恰好 1 个且为 CS → home = that CS
      - 否则（含 NS / 多 CS / 冲突）→ home = NS
    """
    dp_owners: dict[str, set[str]] = {d["decision_id"]: set() for d in dps}
    for owner, dlist in has_decision.items():
        is_ns = owner == ns_id or owner.startswith("NS-")
        for dp in dlist:
            if dp in dp_owners:
                dp_owners[dp].add(owner)

    dp_home: dict[str, str] = {}
    for dp, owners in dp_owners.items():
        cs_owners = {o for o in owners if o.startswith("CS-")}
        ns_owners = {o for o in owners if o.startswith("NS-")}
        if len(cs_owners) == 1 and not ns_owners:
            dp_home[dp] = next(iter(cs_owners))
        else:
            dp_home[dp] = "NS"

    # CS 回指：影响该 CS 但 home 不是该 CS 的 DP
    cs_applies: dict[str, list[str]] = {}
    for owner, dlist in has_decision.items():
        if not owner.startswith("CS-"):
            continue
        for dp in dlist:
            if dp_home.get(dp) != owner:
                cs_applies.setdefault(owner, []).append(dp)
    return {"dp_home": dp_home, "cs_applies": cs_applies}


# ----------------- YAML 输出 -----------------

class LiteralFolder(str):
    pass


def _str_presenter(dumper, data):
    text = str(data)
    if "\n" in text:
        return dumper.represent_scalar("tag:yaml.org,2002:str", text, style=">")
    if text == "":
        return dumper.represent_scalar("tag:yaml.org,2002:str", "")
    return dumper.represent_scalar("tag:yaml.org,2002:str", text)


yaml.add_representer(str, _str_presenter)
yaml.add_representer(LiteralFolder, _str_presenter)


def write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = clean_dict(data)
    with path.open("w", encoding="utf-8") as f:
        f.write("# 由 BusinessGraph/scripts/gen_from_business_graph.py 自动生成；请勿手改，改源 md 后重跑。\n")
        yaml.dump(data, f, allow_unicode=True, sort_keys=False,
                  default_flow_style=False, width=10000)


def clean_dict(d: dict) -> dict:
    """递归丢弃值为 None/''/[]/{} 的键。"""
    out = {}
    for k, v in d.items():
        if isinstance(v, dict):
            v = clean_dict(v)
        elif isinstance(v, list):
            v = [clean_dict(x) if isinstance(x, dict) else x for x in v]
        if v in (None, "", [], {}):
            continue
        out[k] = v
    return out


def slugify(name: str, sid: str) -> str:
    """CS 文件名: cs-<prefix-lower>-<NN>-<slug>.yaml"""
    m = re.search(r"CS-(\w+)-(\d+)", sid)
    if m:
        prefix = m.group(1).lower()
        nn = m.group(2)
    else:
        prefix = "x"; nn = "00"
    # 中文名 → 拼音太重，这里用可读英文映射表，缺失则用 id 兜底（无 slug）
    slug = CS_SLUGS.get(sid, "")
    return f"cs-{prefix}-{nn}{ '-' + slug if slug else ''}.yaml"


# CS id → 英文 slug（可读文件名）；缺失的回退到纯 id
CS_SLUGS = {
    # charging
    "CS-CH-01": "offline", "CS-CH-02": "online", "CS-CH-03": "converged",
    "CS-CH-04": "content-basic", "CS-CH-05": "meter-enhanced",
    "CS-CH-06": "quota-throttle", "CS-CH-07": "fallback-default",
    # bandwidth
    "CS-BW-01": "sa-bwm", "CS-BW-02": "fup-throttle", "CS-BW-03": "gbr-guarantee",
    "CS-BW-04": "adc-aware", "CS-BW-05": "cell-load", "CS-BW-06": "location-area",
    "CS-BW-07": "radio-optim-mark",
    # access-control
    "CS-AC-01": "pcc-block", "CS-AC-02": "header-enhancement", "CS-AC-03": "http-redirect",
    "CS-AC-04": "dns-redirect", "CS-AC-05": "portal-webproxy-redirect",
    "CS-AC-06": "url-filter", "CS-AC-07": "access-control-unc",
    "CS-AC-08": "quota-exhaust-redirect", "CS-AC-09": "area-guide-redirect",
}


# ----------------- 主流程 -----------------

def build_one_scenario(scn: dict) -> dict:
    md = scn["src"].read_text(encoding="utf-8")
    ns = parse_network_scenario(md)
    bd = parse_business_domain(md)
    css = parse_configuration_solutions(md)
    dps = parse_decision_points(md)
    edges = parse_edges(md)

    placement = compute_dp_placement(dps, edges["has_decision"], scn["ns_id"])
    dp_home = placement["dp_home"]
    cs_applies = placement["cs_applies"]

    # uses_feature：优先用关系边 §x.2，回退 inline
    uf = edges["uses_feature"]

    # NS 嵌套 DP（home == NS）
    ns_dps = []
    for d in dps:
        if dp_home.get(d["decision_id"]) == "NS":
            entry = {
                "decision_id": d["decision_id"],
                "decision_name": d["decision_name"],
                "decision_question": d["decision_question"],
                "trigger_condition": d["trigger_condition"],
                "option_set": d["option_set"],
                "impact_summary": d["impact_summary"],
                "selects_solutions": edges["selects"].get(d["decision_id"], {}).get("solutions", []),
                "selection_note": edges["selects"].get(d["decision_id"], {}).get("note", ""),
                "owner_solutions": sorted({o for o in edges["has_decision"] if o.startswith("CS-")
                                           for dp in edges["has_decision"][o] if dp == d["decision_id"]}),
                "status": d["status"],
                "source_evidence_ids": d["source_evidence_ids"],
            }
            ns_dps.append(clean_dict(entry))

    ns_yaml = {
        "scenario_id": ns["scenario_id"],
        "scenario_name": ns["scenario_name"],
        "belongs_to_domain": UNIFIED_BD_ID,
        "scenario_summary": ns["scenario_summary"],
        "judgment_basis": ns["judgment_basis"],
        "typical_outcome": ns["typical_outcome"],
        "status": ns["status"],
        "source_evidence_ids": ns["source_evidence_ids"],
        "coverage": ns["coverage"] or None,
        "non_coverage": ns["non_coverage"] or None,
        "contains_solutions": [c["solution_id"] for c in css],
        "decision_points": ns_dps or None,
    }
    # 删空值键，保持干净
    ns_yaml = {k: v for k, v in ns_yaml.items() if v not in (None, "", [], {})}

    cs_yamls = []
    for c in css:
        sid = c["solution_id"]
        features = uf.get(sid) or c["uses_feature_inline"]
        # 去重保序
        seen = set(); feats = []
        for f in features:
            if f not in seen:
                seen.add(f); feats.append(f)
        # 嵌在该 CS 的 DP（home == sid）
        nested_dps = []
        for d in dps:
            if dp_home.get(d["decision_id"]) == sid:
                nested_dps.append({
                    "decision_id": d["decision_id"],
                    "decision_name": d["decision_name"],
                    "decision_question": d["decision_question"],
                    "trigger_condition": d["trigger_condition"],
                    "option_set": d["option_set"],
                    "impact_summary": d["impact_summary"],
                    "selects_solutions": edges["selects"].get(d["decision_id"], {}).get("solutions", []),
                    "selection_note": edges["selects"].get(d["decision_id"], {}).get("note", ""),
                    "status": d["status"],
                    "source_evidence_ids": d["source_evidence_ids"],
                })
                nested_dps = [clean_dict(x) for x in nested_dps]
        # selected_by_decision: 选出本 CS 的 DP（来自 selects 边）
        selected_by = [dp for dp, info in edges["selects"].items() if sid in info["solutions"]]
        entry = {
            "solution_id": sid,
            "solution_name": c["solution_name"],
            "belongs_to_scenario": scn["ns_id"],
            "solution_summary": c["solution_summary"],
            "design_intent": c["design_intent"],
            "core_mechanism_combo": c["core_mechanism_combo"],
            "status": c["status"],
            "source_evidence_ids": c["source_evidence_ids"],
            "scopes": c["scopes"] or None,
            "participants": c["participants"] or None,
            "uses_feature": feats or None,
            "selected_by_decision": selected_by or None,
            "decision_points": nested_dps or None,
            "applies_decision_refs": sorted(set(cs_applies.get(sid, []))) or None,
        }
        entry = {k: v for k, v in entry.items() if v not in (None, "", [], {})}
        cs_yamls.append((sid, c["solution_name"], entry))

    return {
        "bd": bd,
        "ns_yaml": ns_yaml,
        "cs_yamls": cs_yamls,
        "stats": {
            "cs_count": len(css),
            "dp_total": len(dps),
            "dp_in_ns": len(ns_dps),
            "dp_in_cs": sum(1 for d in dps if dp_home.get(d["decision_id"]) != "NS"),
        },
    }


def main():
    OUT_ROOT.mkdir(exist_ok=True)
    (OUT_ROOT / "scripts").mkdir(exist_ok=True)

    bd_collected = None
    bd_seen_ids = set()
    all_scenarios_meta = []

    for scn in SCENARIOS:
        if not scn["src"].exists():
            print(f"[WARN] 源文件缺失: {scn['src']}", file=sys.stderr)
            continue
        res = build_one_scenario(scn)
        bd = res["bd"]

        # 统一 BD：合并三场景的别名 + 证据
        if bd_collected is None:
            bd_collected = {
                "domain_id": UNIFIED_BD_ID,
                "domain_name": bd["domain_name"],
                "domain_summary": bd["domain_summary"],
                "status": bd["status"],
                "source_evidence_ids": list(bd["source_evidence_ids"]),
                "alias_ids": [],
                "contains_scenarios": [],
            }
        # 收集别名（源里三场景的 BD id 不同）
        if bd["domain_id"] and bd["domain_id"] != UNIFIED_BD_ID and bd["domain_id"] not in bd_seen_ids:
            bd_collected["alias_ids"].append(bd["domain_id"])
            bd_seen_ids.add(bd["domain_id"])
        for ev in bd["source_evidence_ids"]:
            if ev not in bd_collected["source_evidence_ids"]:
                bd_collected["source_evidence_ids"].append(ev)
        bd_collected["contains_scenarios"].append(scn["ns_id"])

        # NS
        ns_path = OUT_ROOT / "scenarios" / scn["dir"] / f"ns-{scn['key'].replace('-', '_')}.yaml"
        write_yaml(ns_path, res["ns_yaml"])

        # CS
        sol_dir = OUT_ROOT / "scenarios" / scn["dir"] / "solutions"
        for sid, name, entry in res["cs_yamls"]:
            fname = slugify(name, sid)
            write_yaml(sol_dir / fname, entry)

        all_scenarios_meta.append((scn, res["stats"]))
        print(f"[OK] {scn['slug_zh']}: NS={scn['ns_id']} | CS={res['stats']['cs_count']} "
              f"| DP 总{res['stats']['dp_total']}(NS={res['stats']['dp_in_ns']}, CS={res['stats']['dp_in_cs']})")

    # 写 BD（统一一个）
    bd_collected["alias_ids"] = sorted(set(bd_collected["alias_ids"]))
    bd_collected["contains_scenarios"] = sorted(set(bd_collected["contains_scenarios"]))
    bd_collected["notes"] = (
        "源数据中 BD-CH-01 / BD-BW-01 / BD-AC-01 三者指同一根对象「业务感知」"
        "（计费/带宽控制/访问限制三场景共享 SA 基础设施），此处统一为单一业务域对象。"
    )
    # 字段顺序
    bd_ordered = {
        "domain_id": bd_collected["domain_id"],
        "domain_name": bd_collected["domain_name"],
        "domain_summary": bd_collected["domain_summary"],
        "status": bd_collected["status"],
        "alias_ids": bd_collected["alias_ids"],
        "contains_scenarios": bd_collected["contains_scenarios"],
        "source_evidence_ids": bd_collected["source_evidence_ids"],
        "notes": bd_collected["notes"],
    }
    write_yaml(OUT_ROOT / "business_domains" / "bd-business-awareness.yaml", bd_ordered)

    total_cs = sum(s[1]["cs_count"] for s in all_scenarios_meta)
    print(f"\n[DONE] BD=1, NS={len(all_scenarios_meta)}, CS={total_cs}, 共 {1 + len(all_scenarios_meta) + total_cs} 个 yaml")
    print(f"       输出目录: {OUT_ROOT}")


if __name__ == "__main__":
    main()
