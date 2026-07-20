#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
迁移脚本：旧 compound (1-XXXXX.md) → 新版 CompoundTask ({NF}@CompoundTask@{slug}.md)

严格按 三层图谱构建规范/task/迁移指南-旧compound到CompoundTask.md 执行。

输入: assets/task/{NF}/{VERSION}/1-XXXXX.md  (UDG 34 个)
输出: 三层图谱资产/CompoundTask/{NF}/{VERSION}/{NF}@CompoundTask@{slug}.md

与 atom 迁移的关键差异:
  1. compound 无命令名锚 → ID 用英文语义 slug（SLUG_MAP 硬编码，附录 A）
  2. YAML 7 字段（无 ref）；name=slug, name_zh=旧 task_logical_name
  3. 关联段不整段删，而是逐行解析提取多边（含 atom / 上游 / 下游 / 平行）
  4. 链接转换: 1-XXXXX → CompoundTask@{slug}（本批迁）；2-XXXXX → 删链接留文字（feature 未迁）
  5. 0-XXXXX → AtomTask@{cmd}（现场读 assets/task/.../0-*.md ref）
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

# ───────────────────────── 路径常量 ─────────────────────────
DEFAULT_NF = "UDG"
DEFAULT_VERSION = "20.15.2"

ROOT = Path(__file__).resolve().parents[3]  # D:/mywork/KnowledgeBase/SFCGraph
NF = DEFAULT_NF
VERSION = DEFAULT_VERSION
SRC_DIR = ROOT / "assets" / "task" / NF / VERSION           # 旧资产（含 0- 与 1-）
DST_DIR = ROOT / "三层图谱资产" / "CompoundTask" / NF / VERSION

# ───────────────────────── slug 表（附录 A，定稿） ─────────────────────────
SLUG_MAP: Dict[str, str] = {
    "1-00001": "license-access-prep",
    "1-00002": "bwm-service-controller",
    "1-00003": "bwm-usergroup-rule-bind",
    "1-00004": "pcc-predefined-rule-chain",
    "1-00005": "slice-bind",
    "1-00006": "timerange-control",
    "1-00007": "icap-server-interconnect",
    "1-00008": "cf-content-filter",
    "1-00009": "filter-chain",
    "1-00010": "charging-core-trio",
    "1-00011": "rule-userprofile-bind",
    "1-00012": "charging-tail",
    "1-00013": "header-enrich",
    "1-00014": "ipfarm-redirect-chain",
    "1-00015": "smart-redirect-action-chain",
    "1-00016": "sa-protocol-identify-chain",
    "1-00017": "qos-dedicated-bearer-chain",
    "1-00018": "session-addr-alloc",
    "1-00019": "session-pcc-policy",
    "1-00020": "session-n4-interface",
    "1-00021": "addr-alloc-rule",
    "1-00022": "addr-pool-hierarchy",
    "1-00023": "smf-addr-alloc-mode",
    "1-00024": "downlink-route-export",
    "1-00025": "dualstack-apn-poolgroup",
    "1-00026": "ipv6-bearer-ospfv3-wlr",
    "1-00027": "ipv6-bearer-infra",
    "1-00028": "ipv6pd-prefix-flag",
    "1-00029": "apn-access-infra",
    "1-00030": "mpls-vpn-infra",
    "1-00031": "gre-redundancy-master-standby",
    "1-00032": "gre-tunnel-setup",
    "1-00033": "ipsec-tunnel-setup",
    "1-00034": "l2tp-lns-setup",
}

# UNC compound slug 表（38 条）。计费/PCRF/会话族 UNC 独有（不带前缀）；
# 基础设施族与 UDG 同类，带 unc- 前缀避免撞名（如 unc-gre-tunnel-family vs UDG gre-tunnel-setup）。
SLUG_MAP_UNC: Dict[str, str] = {
    "1-00001": "offline-charging-template",
    "1-00002": "ofctemplate-bind-userprofile",
    "1-00003": "ofctemplate-bind-apn",
    "1-00004": "ofctemplate-bind-cc",
    "1-00005": "converged-charging-template",
    "1-00006": "cct-bind-cc",
    "1-00007": "chf-selection",
    "1-00008": "smf-chf-trigger-rg-aging",
    "1-00009": "converged-charging-rate-id-chain",
    "1-00010": "converged-charging-exception",
    "1-00011": "charging-msg-cache",
    "1-00012": "pcrf-diameter-chain",
    "1-00013": "pcrf-selection-grouping",
    "1-00014": "pcc-switch-template",
    "1-00015": "adc-app-detection",
    "1-00016": "adc-predefined-rule-bind",
    "1-00017": "qos-attr-rule-bind-chain",
    "1-00018": "bwm-local-rule-bind",
    "1-00019": "user-location-template-bind",
    "1-00020": "session-addr-alloc-skeleton",
    "1-00021": "session-pcc-chf-skeleton",
    "1-00022": "session-n4-pfcp-skeleton",
    "1-00023": "unc-smf-addrpool-hierarchy",
    "1-00024": "unc-apn-access-infra",
    "1-00025": "unc-radius-chain",
    "1-00026": "unc-radius-vsa",
    "1-00027": "unc-gre-tunnel-family",
    "1-00028": "unc-dhcp-server-chain",
    "1-00029": "unc-downlink-route-export",
    "1-00030": "unc-ipsec-suite",
    "1-00031": "unc-mpls-vpn-infra",
    "1-00032": "unc-ospfv3-route-export",
    "1-00033": "unc-dualstack-global-switch",
    "1-00034": "unc-ctrl-addr-alloc-rule",
    "1-00035": "unc-l2tp-ctrl-family",
    "1-00036": "unc-upf-selection-family",
    "1-00037": "unc-access-control-family",
    "1-00038": "unc-location-dns-family",
}

COMPOUND_NUM_RE = re.compile(r"^1-(\d{5})\.md$")
ATOM_NUM_RE = re.compile(r"^0-(\d{5})\.md$")

# markdown 链接：href 允许空格（中文 evidence 文件名常含空格），但排除 ) 和 *
# （排除 * 防 atom 脚本注释提到的破损链接 task/UNC/20.15**（warning...） 被误吃）
MD_LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)*]+)\)")
# 旧 wiki4 占位（带 version）
WIKI4_RE = re.compile(r"\[+UDG@20\.15\.2@([\w]+)@([^\]]+)\]+")


# ───────────────────────── YAML 解析（复用 atom） ─────────────────────────

def parse_yaml(blob: str) -> Tuple[Dict, Dict]:
    scalar: Dict[str, str] = {}
    lists: Dict[str, List[str]] = {}
    cur_list: List[str] = None
    for raw in blob.splitlines():
        line = raw.rstrip()
        if not line:
            continue
        if line.startswith("  - ") or line.startswith("    - "):
            item = line.lstrip().lstrip("-").strip()
            if cur_list is not None:
                cur_list.append(item)
            continue
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val == "":
            cur_list = []
            lists[key] = cur_list
        else:
            cur_list = None
            scalar[key] = val
    return scalar, lists


def extract_yaml_and_body(text: str) -> Tuple[Dict, Dict, str, str]:
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        raise ValueError("no YAML frontmatter found")
    yaml_blob = m.group(1)
    body = m.group(2)
    scalar, lists = parse_yaml(yaml_blob)
    return scalar, lists, yaml_blob, body


def build_command_map(src_dir: Path) -> Dict[str, str]:
    """{0-XXXXX -> COMMAND}，从每个 0-*.md 的 ref 末段取（用于关联段/正文 0- 引用）。"""
    table: Dict[str, str] = {}
    for f in sorted(src_dir.iterdir()):
        if not ATOM_NUM_RE.match(f.name):
            continue
        try:
            text = f.read_text(encoding="utf-8")
        except Exception:
            continue
        scalar, _ = extract_yaml_and_body(text)[:2]
        ref = scalar.get("ref", "")
        cmd = ref.split("@")[-1].strip()
        if cmd and cmd != "null":
            table[f.stem] = cmd  # f.stem = 0-00007
    return table


# ───────────────────────── code block 保护（复用 atom） ─────────────────────────

def _protect_code_blocks(body: str) -> Tuple[str, List[str]]:
    placeholders: List[str] = []

    def repl_fence(m: re.Match) -> str:
        placeholders.append(m.group(0))
        return f"\x00CODEBLOCK{len(placeholders) - 1}\x00"
    body = re.sub(r"```.*?```", repl_fence, body, flags=re.S)

    def repl_inline(m: re.Match) -> str:
        placeholders.append(m.group(0))
        return f"\x00CODEINLINE{len(placeholders) - 1}\x00"
    body = re.sub(r"`[^`\n]+`", repl_inline, body)
    return body, placeholders


def _restore_code_blocks(body: str, placeholders: List[str]) -> str:
    for i, orig in enumerate(placeholders):
        body = body.replace(f"\x00CODEBLOCK{i}\x00", orig)
        body = body.replace(f"\x00CODEINLINE{i}\x00", orig)
    return body


# ───────────────────────── 段落级转换（复用 atom） ─────────────────────────

def transform_decision_title(body: str) -> str:
    return re.sub(r"（DP\s+0-\d{5}(?:-\d+)?\s*）", "", body)


def strip_dp_inline_refs(body: str) -> str:
    body = re.sub(r"另存演进\s*DP\s+0-\d{5}(?:-\d+)?", "另存一个演进决策", body)
    body = re.sub(r"（DP\s+0-\d{5}(?:-\d+)?\s*[,，]?\s*([^）)]*?)）", r"（决策点，\1）", body)
    body = re.sub(r"仅在\s*DP\s+0-\d{5}(?:-\d+)?\s*标注", "仅在决策点标注", body)
    body = re.sub(r"决策点\s*DP\s+0-\d{5}(?:-\d+)?", "决策点", body)
    body = re.sub(r"DP\s+0-\d{5}(?:-\d+)?\s*标注", "决策点标注", body)
    body = re.sub(r"(?:参见|见|参)\s+DP\s+0-\d{5}(?:-\d+)?", "见决策点", body)
    body = re.sub(r"DP\s+0-\d{5}(?:-\d+)?\s*驱动", "决策点驱动", body)
    body = re.sub(r"(由[^，。,；;]{0,20}?)\s*DP\s+0-\d{5}(?:-\d+)?\s*编排", r"\1编排", body)
    body = re.sub(r"由\s*DP\s+0-\d{5}(?:-\d+)?\s*编排", "由该决策点编排", body)
    body = re.sub(r"\s*DP\s+0-\d{5}(?:-\d+)?", "", body)
    return body


def strip_rule_refs(body: str) -> str:
    body = re.sub(
        r"（\s*(critical|warning|info)\s*[,，]\s*"
        r"(?:"
        r"rule-0-\d{5}(?:-\d+)?(?:-impl)?\s*(?:[,，]\s*(?:隐含|命令\s+notes|命令\s+真相|命令\s+notes\s*推论|命令\s+真相\s*推论|对端协商要求|APN\s+名规范|系统资源|同族))*"
        r"|隐含|命令\s+notes|同族"
        r")"
        r"\s*）",
        r"（\1）", body,
    )
    body = re.sub(
        r"\(\s*(critical|warning|info)\s*,\s*"
        r"(?:"
        r"rule-0-\d{5}(?:-\d+)?(?:-impl)?\s*(?:,\s*(?:隐含|命令\s+notes|命令\s+真相|命令\s+notes\s*推论|命令\s+真相\s*推论|对端协商要求|APN\s+名规范|系统资源|同族))*"
        r"|隐含|命令\s+notes|同族"
        r")"
        r"\)",
        r"(\1)", body,
    )
    body = re.sub(r"(?<![\w/.-])rule-0-\d{5}(?:-\d+)?(?:-impl)?", "", body)
    return body


def strip_orphan_bold_dp_marker(body: str) -> str:
    body = body.replace("****", "")
    body = re.sub(r"\*\*\s*\*\*", "", body)
    return body


def strip_standalone_rule_marker(body: str) -> str:
    return re.sub(r"\*\*\s*rule-0-\d{5}(?:-\d+)?\s*\*\*", "", body)


def strip_paren_num(text: str) -> str:
    """括号内 0-/1- 编号注释删（compound 兼容 0- 与 1-）。"""
    text = re.sub(r"([01]-\d{5})\s*[.:]\s*[A-Za-z_][\w]*", "", text)
    text = re.sub(r"command-evidence/0-\d{5}", "", text)
    text = re.sub(r"[（(]\s*[)）]", "", text)
    text = re.sub(r"[（(]\s{1,}(?:强约束|约束|建议|可选|必选|默认|备注|提示|注|说明)\s*[)）]", "", text)
    text = re.sub(r"[（(]\s{2,}[)）]", "", text)
    text = re.sub(r"[（(]\s*(?:引用|参引|参见|引自|详见|见|为|指|指向|即|表示|参)\s*[)）]", "", text)
    text = re.sub(r"[（(]\s*[01]-\d{5}\s*[)）]", "", text)
    text = re.sub(r"[（(]\s*[01]-\d{5}\s+", "（", text)
    text = re.sub(r"(?:参见|见|参)\s+[01]-\d{5}\b", "", text)
    text = re.sub(r"<([^<>]{0,30})[01]-\d{5}([^<>]{0,30})>", r"<\1\2>", text)
    return text


# ───────────────────────── 链接转换（compound 版） ─────────────────────────

def convert_markdown_links(text: str, cmdmap: Dict[str, str], slugmap: Dict[str, str]) -> str:
    """§5 表（compound 版）：
      command/ → MMLCommand；configobject|evidence → 删；business/ → 留文字(CS)；
      feature/ → Feature；0-XXXXX.md → AtomTask；1-XXXXX.md → CompoundTask；
      2-XXXXX.md → 留文字(feature_task 未迁)。
    """
    def repl(m: re.Match) -> str:
        label, href = m.group(1), m.group(2)
        if href.startswith("command/"):
            base = re.sub(r"\.md$", "", href.rsplit("/", 1)[-1])
            return f"[[{NF}@MMLCommand@{base.replace('-', ' ')}]]"
        if href.startswith("configobject/"):
            return ""
        if href.startswith("evidence/"):
            return ""
        if href.startswith("business/"):
            return label  # CS 跨层，删链接留文字
        if href.startswith("feature/"):
            base = re.sub(r"\.md$", "", href.rsplit("/", 1)[-1])
            return f"[[{NF}@Feature@{base}]]"
        if href == "#":
            return ""
        fname = href.rsplit("/", 1)[-1]
        # business 层对象（CS@/NS@/BD@ 等两段式 ID，跨层未迁），删链接留文字
        if re.match(r"^(CS|NS|BD|ConfigurationSolution|NetworkScenario|BusinessDomain)@", fname):
            return label
        m_atom = re.match(r"^(0-\d{5})\.md$", fname)
        if m_atom:
            cmd = cmdmap.get(m_atom.group(1))
            return f"[[{NF}@AtomTask@{cmd}]]" if cmd else label
        m_comp = re.match(r"^(1-\d{5})\.md$", fname)
        if m_comp:
            slug = slugmap.get(m_comp.group(1))
            return f"[[{NF}@CompoundTask@{slug}]]" if slug else label
        m_feat = re.match(r"^(2-\d{5})\.md$", fname)
        if m_feat:
            return label  # feature_task 未迁，删链接留文字
        return m.group(0)
    return MD_LINK_RE.sub(repl, text)


def convert_wiki4_placeholders(text: str, cmdmap: Dict[str, str], slugmap: Dict[str, str]) -> str:
    def repl(m: re.Match) -> str:
        typ, local = m.group(1), m.group(2)
        if typ == "MMLCommand":
            return f"[[{NF}@MMLCommand@{local}]]"
        if typ == "Task":
            if local.startswith("0-"):
                cmd = cmdmap.get(local)
                return f"[[{NF}@AtomTask@{cmd}]]" if cmd else m.group(0)
            if local.startswith("1-"):
                slug = slugmap.get(local)
                return f"[[{NF}@CompoundTask@{slug}]]" if slug else m.group(0)
            return m.group(0)
        if typ == "Feature":
            return f"[[{NF}@Feature@{local}]]"
        if typ == "DecisionPoint":
            return ""
        if typ == "ConfigObject":
            return ""
        return m.group(0)
    return WIKI4_RE.sub(repl, text)


def replace_bare_refs(text: str, cmdmap: Dict[str, str], slugmap: Dict[str, str]) -> str:
    """正文裸 0-/1- 编号转双方括号；§/feature-rule/selection_rule 前缀删。"""
    text = re.sub(r"§\s*[01]-\d{5}(?:-\d+)?", "", text)
    text = re.sub(r"(feature-rule|selection_rule)\s*[01]-\d{5}(?:-\d+)?", r"\1", text)

    def repl_multi(m: re.Match) -> str:
        out = []
        for n in re.findall(r"[01]-\d{5}", m.group(0)):
            if n.startswith("0-") and cmdmap.get(n):
                out.append(f"[[{NF}@AtomTask@{cmdmap[n]}]]")
            elif n.startswith("1-") and slugmap.get(n):
                out.append(f"[[{NF}@CompoundTask@{slugmap[n]}]]")
            else:
                out.append(n)
        return "/".join(out)
    text = re.sub(r"(?:[01]-\d{5}(?:/[01]-\d{5})+)", repl_multi, text)

    def repl0(m: re.Match) -> str:
        cmd = cmdmap.get(m.group(0))
        return f"[[{NF}@AtomTask@{cmd}]]" if cmd else m.group(0)
    text = re.sub(r"(?<![\w/.-])0-\d{5}(?![a-zA-Z0-9/])", repl0, text)

    def repl1(m: re.Match) -> str:
        slug = slugmap.get(m.group(0))
        return f"[[{NF}@CompoundTask@{slug}]]" if slug else m.group(0)
    text = re.sub(r"(?<![\w/.-])1-\d{5}(?![a-zA-Z0-9/])", repl1, text)
    return text


# ───────────────────────── 关联段 → 边（compound 特有） ─────────────────────────

_EDGE_ORDER = {"含 atom": 0, "含 compound": 0, "上游": 1, "前置": 1, "下游": 2, "平行": 3, "关联": 4}


# 关联段行首标签白名单（只有这些行的编号才提取为边；其余标签整行删）
# raw 标签 → 规范化边标签
_LABEL_WHITELIST = {
    "含 atom": "含 atom", "含atom": "含 atom",
    "上游": "上游", "前置": "上游", "前置任务": "上游",
    "下游": "下游",
    "平行": "平行",
}


def parse_assoc_to_edges(body: str, cmdmap: Dict[str, str], slugmap: Dict[str, str]) -> Tuple[str, List[Tuple[str, str]]]:
    """§6 解析 ## 关联 段：只从白名单标签行（含 atom/上游/下游/平行/前置）提取边；
    其余标签行（配套/被引用于/证据/配置对象/父特性/被依赖/C-U 对应/命令 wiki）整行删，不提取。
    含 atom 行只扫 0-；上游/下游/平行/前置行扫 0- + 1-（方向由标签定，不固定 0-→含atom）。
    返回 (去掉关联段的 body, edges[(label, target_id), ...])。
    """
    m = re.search(r"^##\s+关联\s*$", body, re.M)
    if not m:
        return body, []
    head = body[: m.start()].rstrip() + "\n"
    after = body[m.end():]
    tail_m = re.search(r"^##\s+", after, re.M)
    assoc = after[: tail_m.start()] if tail_m else after
    tail = after[tail_m.start():] if tail_m else ""

    edges: List[Tuple[str, str]] = []
    seen = set()

    def add(label: str, target: str) -> None:
        if (label, target) not in seen:
            seen.add((label, target))
            edges.append((label, target))

    for line in assoc.splitlines():
        s = line.strip()
        ml = re.match(r"^-\s*([^：:]+)[：:]\s*(.*)$", s)
        if not ml:
            continue
        raw_label = ml.group(1).strip()
        rest = ml.group(2)
        edge_label = _LABEL_WHITELIST.get(raw_label)
        if not edge_label:
            continue  # 非白名单标签 → 整行删，不提取
        # 该行所有 0- → AtomTask，归 edge_label
        for num in re.findall(r"0-\d{5}", rest):
            cmd = cmdmap.get(num)
            if cmd:
                add(edge_label, f"{NF}@AtomTask@{cmd}")
        # 含 atom 行不扫 1-；上游/下游/平行行也扫 1- → CompoundTask
        if edge_label != "含 atom":
            for num in re.findall(r"1-\d{5}", rest):
                slug = slugmap.get(num)
                if slug:
                    add(edge_label, f"{NF}@CompoundTask@{slug}")
    new_body = head + "\n" + tail.lstrip("\n")
    return new_body, edges


def render_edges(edges: List[Tuple[str, str]]) -> str:
    if not edges:
        return "## 边\n"
    ordered = sorted(edges, key=lambda e: (_EDGE_ORDER.get(e[0], 9), e[0], e[1]))
    lines = ["## 边"] + [f"- {label}: [[{target}]]" for label, target in ordered]
    return "\n".join(lines) + "\n"


# ───────────────────────── 正文处理 ─────────────────────────

def process_body(body: str, cmdmap: Dict[str, str], slugmap: Dict[str, str]) -> str:
    """关联段已由 parse_assoc_to_edges 删除；这里处理其余正文转换。"""
    body, ph = _protect_code_blocks(body)
    body = transform_decision_title(body)
    body = strip_rule_refs(body)
    body = convert_markdown_links(body, cmdmap, slugmap)
    body = convert_wiki4_placeholders(body, cmdmap, slugmap)
    body = strip_dp_inline_refs(body)
    body = replace_bare_refs(body, cmdmap, slugmap)
    body = strip_paren_num(body)
    body = strip_orphan_bold_dp_marker(body)
    body = strip_standalone_rule_marker(body)
    body = _restore_code_blocks(body, ph)
    return body


# ───────────────────────── YAML 输出（7 字段） ─────────────────────────

def render_yaml(scalar: Dict[str, str], slug: str) -> str:
    name_zh = scalar.get("task_logical_name", "").strip()
    status = scalar.get("status", "").strip() or "draft"  # 原样保留源 status（如 foundation/draft/active）
    return "\n".join([
        "---",
        f'id: "{NF}@CompoundTask@{slug}"',
        f'type: "CompoundTask"',
        f'name: "{slug}"',
        f'name_zh: "{name_zh}"',
        f'nf: "{NF}"',
        f'version: "{VERSION}"',
        f'status: "{status}"',
        "---",
        "",
    ])


# ───────────────────────── 单文件迁移 ─────────────────────────

def migrate_one(src_path: Path, cmdmap: Dict[str, str], slugmap: Dict[str, str]) -> Tuple[Path, str, List[Tuple[str, str]]]:
    text = src_path.read_text(encoding="utf-8")
    scalar, _, _, body = extract_yaml_and_body(text)
    num = src_path.stem  # 1-00003
    slug = slugmap[num]

    # 1) 关联段 → 边（同时从 body 删关联段）
    body, edges = parse_assoc_to_edges(body, cmdmap, slugmap)
    # 2) 正文转换
    new_body = process_body(body, cmdmap, slugmap)
    # 3) 拼装
    new_yaml = render_yaml(scalar, slug)
    edge_section = render_edges(edges)
    new_text = new_yaml + new_body.rstrip() + "\n\n" + edge_section

    out_name = f"{NF}@CompoundTask@{slug}.md"
    out_path = DST_DIR / out_name
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(new_text, encoding="utf-8")
    return out_path, slug, edges


# ───────────────────────── 主入口 ─────────────────────────

def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(
        prog="migrate_old_compounds",
        description="迁移旧 compound (1-XXXXX.md) → 新版 CompoundTask ({NF}@CompoundTask@{slug}.md)",
    )
    parser.add_argument("--nf", default=DEFAULT_NF)
    parser.add_argument("--version", default=DEFAULT_VERSION)
    parser.add_argument("filename", nargs="?", default=None,
                        help="只迁指定编号 (dry-run), e.g. 1-00003.md")
    args = parser.parse_args(argv[1:])

    global NF, VERSION, SRC_DIR, DST_DIR
    NF = args.nf
    VERSION = args.version
    SRC_DIR = ROOT / "assets" / "task" / NF / VERSION
    DST_DIR = ROOT / "三层图谱资产" / "CompoundTask" / NF / VERSION

    if not SRC_DIR.is_dir():
        print(f"ERR: src dir not found: {SRC_DIR}", file=sys.stderr)
        return 2

    cmdmap = build_command_map(SRC_DIR)
    print(f"[build_command_map] {len(cmdmap)} atom entries", file=sys.stderr)
    slugmap = SLUG_MAP if NF == "UDG" else SLUG_MAP_UNC
    if NF not in ("UDG", "UNC"):
        print(f"ERR: no slug map for NF={NF}", file=sys.stderr)
        return 2
    print(f"[slug_map] {len(slugmap)} compound slugs ({NF})", file=sys.stderr)

    targets: List[Path] = []
    if args.filename:
        p = SRC_DIR / args.filename
        if not p.is_file():
            print(f"ERR: {p} not found", file=sys.stderr)
            return 2
        targets.append(p)
    else:
        for f in sorted(SRC_DIR.iterdir()):
            if COMPOUND_NUM_RE.match(f.name):
                targets.append(f)

    print(f"[migrate] {len(targets)} files", file=sys.stderr)
    written = 0
    for p in targets:
        out_path, slug, edges = migrate_one(p, cmdmap, slugmap)
        written += 1
        if args.filename:
            print(f"[dry-run] {p.name} -> {out_path.name}  (edges: {len(edges)})", file=sys.stderr)
            print("=" * 60, file=sys.stderr)
            print(out_path.read_text(encoding="utf-8"))
    print(f"[done] {written} migrated", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
