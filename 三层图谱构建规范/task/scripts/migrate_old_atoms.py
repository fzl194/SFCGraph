#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
迁移脚本：旧 atom (0-XXXXX.md) → 新版 AtomTask ({NF}@AtomTask@{COMMAND}.md)

严格按 三层图谱构建规范/task/迁移指南-旧atom到AtomTask.md 执行。

输入: assets/task/{NF}/{VERSION}/0-XXXXX.md  (UDG 237 个 / UNC 280 个)
输出: 三层图谱资产/AtomTask/{NF}/{VERSION}/{NF}@AtomTask@{COMMAND}.md

命令行:
    默认: NF=UDG, VERSION=20.15.2 (向后兼容 v0.11.0 行为)
    --nf UNC     处理 UNC 资产
    --version X  指定产品版本
    [filename]   只迁指定编号, 用于 dry-run

设计:
- 命令名查表: 直接读每个 0-*.md YAML 的 ref 字段末段（避免依赖附录 A 静态表，
  附录 A 只是缓存；现场读 ref 才是 single source of truth）。
- 转换顺序: 先做"段落级重构"（关联段整段拆解、决策点段标题去 DP 编号、约束段去 rule 编号），
  再做"全文链接替换"（markdown 链接 + 旧 wiki4 占位），最后做"正文括号去编号"。
- 不重写：业务正文原样保留。YAML 8 字段按 §3 表换。
- code block 保护: 围栏代码块和行内代码不在 strip 函数作用范围内（§4.3 硬约束）。
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

# ───────────────────────── 路径常量 ─────────────────────────
DEFAULT_NF = "UDG"
DEFAULT_VERSION = "20.15.2"

ROOT = Path(__file__).resolve().parents[3]  # D:/mywork/KnowledgeBase/SFCGraph
# 这些常量在 main() 里被 CLI 参数覆盖
NF = DEFAULT_NF
VERSION = DEFAULT_VERSION
SRC_DIR = ROOT / "assets" / "task" / NF / VERSION          # 旧资产
DST_DIR = ROOT / "三层图谱资产" / "AtomTask" / NF / VERSION  # 新资产

# 5 位流水 atom 编号 → 命令名  (现场读 ref 末段填充)
ATOM_NUM_RE = re.compile(r"^0-(\d{5})\.md$")
ATOM_NUM_BARE_RE = re.compile(r"(?<![\w/.-])0-\d{5}(?![a-zA-Z0-9])")

# ───────────────────────── YAML 解析（最小，自包含） ─────────────────────────
# 旧文件 YAML 简单（纯 key: value / 嵌套 source_evidence_ids 列表），
# 不引外部库，自己写个轻量解析。

def parse_yaml(blob: str) -> Tuple[Dict, Dict]:
    """返回 (scalar, list_block) 两份；list_block key -> List[str]。"""
    scalar: Dict[str, str] = {}
    lists: Dict[str, List[str]] = {}
    cur_key = None
    cur_list: List[str] = None
    for raw in blob.splitlines():
        line = raw.rstrip()
        if not line:
            continue
        if line.startswith("  - ") or line.startswith("    - "):
            # 列表项
            item = line.lstrip().lstrip("-").strip()
            if cur_list is not None:
                cur_list.append(item)
            continue
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val == "":
            # 列表开始
            cur_key = key
            cur_list = []
            lists[key] = cur_list
        else:
            cur_key = None
            cur_list = None
            scalar[key] = val
    return scalar, lists


def extract_yaml_and_body(text: str) -> Tuple[Dict, Dict, str, str]:
    """返回 (scalar, lists, yaml_blob, body)；body 含正文（YAML 之后的部分）。"""
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        raise ValueError("no YAML frontmatter found")
    yaml_blob = m.group(1)
    body = m.group(2)
    scalar, lists = parse_yaml(yaml_blob)
    return scalar, lists, yaml_blob, body


# ───────────────────────── 命令名查找 ─────────────────────────

def build_command_map(src_dir: Path) -> Dict[str, str]:
    """{0-XXXXX -> COMMAND}，从每个 0-*.md 的 ref 末段取。"""
    table: Dict[str, str] = {}
    for f in sorted(src_dir.iterdir()):
        m = ATOM_NUM_RE.match(f.name)
        if not m:
            continue
        text = f.read_text(encoding="utf-8")
        scalar, _ = extract_yaml_and_body(text)[:2]
        ref = scalar.get("ref", "")
        # ref 形如 UDG@20.15.2@MMLCommand@ADD FLOWFILTER
        cmd = ref.split("@")[-1].strip()
        table[f"0-{m.group(1)}"] = cmd
    return table


# ───────────────────────── 段落级转换 ─────────────────────────

def strip_assoc_section(body: str) -> str:
    """§4.6 关联段整段重构：保留 ## 关联 之前的所有内容；删 ## 关联 段；
    在正文末尾追加 ## 边（占位，后面再插入"对应命令"）。"""
    # 找到 ## 关联 开始
    m = re.search(r"^##\s+关联\s*$", body, re.M)
    if not m:
        # 没 ## 关联 段就原样返回
        return body
    head = body[: m.start()].rstrip() + "\n"
    # 关联段直到下一个 ## 或文件末尾
    tail_match = re.search(r"^##\s+", body[m.end():], re.M)
    if tail_match:
        tail = body[m.end() + tail_match.start():]
    else:
        tail = ""
    return head + "\n" + tail.lstrip("\n")


def transform_decision_title(body: str) -> str:
    """§4.4 决策点段标题去 DP 编号：'## 决策点：xxx（DP 0-XXXXX）' -> '## 决策点：xxx'。"""
    # 多种写法：'（DP 0-XXXXX）' / '（DP 0-XXXXX-NN）' / 行内 '（DP 0-XXXXX）'
    return re.sub(r"（DP\s+0-\d{5}(?:-\d+)?\s*）", "", body)


def strip_dp_inline_refs(body: str) -> str:
    """§4.4 正文里 'DP 0-XXXXX' 引用删编号、留语义。
    迁移指南 7.1 范例对应改写:
        '另存演进 DP 0-00019（xxx）' -> '另存一个演进决策（xxx）'
        '仅在 DP 0-00019 标注'       -> '仅在决策点标注'
        '决策点 DP 0-00281 驱动'     -> '决策点驱动'
        '见 DP 0-00019'              -> '见决策点'
        '由 atom-级决策点 DP 0-00283 编排' -> '由 atom-级决策点编排'
    处理顺序: 先吃高频模板, 再通用兜底。
    """
    # 1) '另存演进 DP 0-NNNNN' → '另存一个演进决策'
    body = re.sub(
        r"另存演进\s*DP\s+0-\d{5}(?:-\d+)?",
        "另存一个演进决策",
        body,
    )
    # 2) '（DP 0-NNNNN）' / '（DP 0-NNNNN，xxx）' -> '（决策点，xxx）'
    body = re.sub(
        r"（DP\s+0-\d{5}(?:-\d+)?\s*[,，]?\s*([^）)]*?)）",
        r"（决策点，\1）",
        body,
    )
    # 3) '仅在 DP 0-NNNNN 标注' → '仅在决策点标注'
    body = re.sub(r"仅在\s*DP\s+0-\d{5}(?:-\d+)?\s*标注", "仅在决策点标注", body)
    # 4) '决策点 DP 0-NNNNN' 前后 → '决策点' 居中
    body = re.sub(r"决策点\s*DP\s+0-\d{5}(?:-\d+)?", "决策点", body)
    # 5) 'DP 0-NNNNN 标注' 居中留字
    body = re.sub(r"DP\s+0-\d{5}(?:-\d+)?\s*标注", "决策点标注", body)
    # 6) '见 DP 0-NNNNN' / '参见 DP 0-NNNNN' → '见决策点'
    body = re.sub(r"(?:参见|见|参)\s+DP\s+0-\d{5}(?:-\d+)?", "见决策点", body)
    # 7) 'DP 0-NNNNN 驱动' → '决策点驱动'
    body = re.sub(r"DP\s+0-\d{5}(?:-\d+)?\s*驱动", "决策点驱动", body)
    # 8) '由 ... DP 0-NNNNN 编排' → '由该决策点编排' / '由 atom-级决策点编排' (前缀保留)
    body = re.sub(r"(由[^，。,；;]{0,20}?)\s*DP\s+0-\d{5}(?:-\d+)?\s*编排", r"\1编排", body)
    body = re.sub(r"由\s*DP\s+0-\d{5}(?:-\d+)?\s*编排", "由该决策点编排", body)
    # 9) 兜底：删残留的 'DP 0-XXXXX' 字面, 前补空格防止连字
    body = re.sub(r"\s*DP\s+0-\d{5}(?:-\d+)?", "", body)
    return body


def strip_rule_refs(body: str) -> str:
    """§4.5 约束段去 rule 编号 + 去来源标记，只留 severity。
    例: '（critical，rule-0-00123）' -> '（critical）'
        '（critical，rule-0-00281-01）' -> '（critical）'
        '（critical，隐含）' -> '（critical）'
        '（warning，rule-0-00334）' -> '（warning）'
        '（warning，命令 notes）' -> '（warning）'
        '(critical,rule-0-00300)' (半角) -> '(critical)'
        '**xxx**(critical,rule-0-00300)' (行内末尾) -> '**xxx**(critical)'
        '（warning，rule-0-00110 同族）'   -> '（warning，同族）'
        '（critical，rule-0-00443，命令 notes）' -> '（critical）'
        '（critical，rule-0-00443-impl）'  -> '（critical）'
        '（rule-0-00270）'                  -> '（）' -> 后被 strip_paren_atom_num 清空括号
        '见约束 rule-0-00130。'              -> '见约束。'
        '**rule-0-00178-impl**'             -> '**rule-impl**' (留 impl 标记)
    全角/半角括号 + 全角/半角逗号都要吃。
    """
    # 1) 紧跟 severity 的可选尾巴（rule- / 隐含 / 命令 notes 等）一律删
    #    全角: （critical，rule-0-XXXXX） / （critical，rule-0-XXXXX，命令 notes）/ etc.
    body = re.sub(
        r"（\s*(critical|warning|info)\s*[,，]\s*"
        r"(?:"
        r"rule-0-\d{5}(?:-\d+)?(?:-impl)?\s*(?:[,，]\s*(?:隐含|命令\s+notes|命令\s+真相|命令\s+notes\s*推论|命令\s+真相\s*推论|对端协商要求|APN\s+名规范|系统资源|同族))*"
        r"|隐含"
        r"|命令\s+notes"
        r"|同族"
        r")"
        r"\s*）",
        r"（\1）",
        body,
    )
    # 2) 半角括号 + 半角逗号: (critical,rule-0-XXXXX)
    body = re.sub(
        r"\(\s*(critical|warning|info)\s*,\s*"
        r"(?:"
        r"rule-0-\d{5}(?:-\d+)?(?:-impl)?\s*(?:,\s*(?:隐含|命令\s+notes|命令\s+真相|命令\s+notes\s*推论|命令\s+真相\s*推论|对端协商要求|APN\s+名规范|系统资源|同族))*"
        r"|隐含"
        r"|命令\s+notes"
        r"|同族"
        r")"
        r"\)",
        r"(\1)",
        body,
    )
    # 3) 裸 'rule-0-XXXXX[-impl]?' 不在括号里, 前后跟非路径字符: 删
    body = re.sub(r"(?<![\w/.-])rule-0-\d{5}(?:-\d+)?(?:-impl)?", "", body)
    return body


def strip_orphan_bold_dp_marker(body: str) -> str:
    """占位符删除后, 周围残留的双重粗体 '****' 或孤立 '**' 兜底清理。
    例: '**[[UDG@20.15.2@DecisionPoint@0-00281]]**（xxx）' 经 wiki4 删占位后
         -> '****（xxx）', 修成 '（xxx）'。
    """
    # '****' 任意位置 -> ''
    body = body.replace("****", "")
    # 行内 '**' 孤立出现(前后都非字母数字) -> ''
    body = re.sub(r"\*\*\s*\*\*", "", body)
    return body


def strip_standalone_rule_marker(body: str) -> str:
    """§4.5 + §0 总原则 2: '**rule-0-XXXXX**' 单独成粗体标题时删。
    例: '- **rule-0-00338**（critical）xxx' -> '- （critical）xxx'
    这种写法全 237 个里仅 0-00214 出现一次, 按总原则删旧编号。
    """
    body = re.sub(
        r"\*\*\s*rule-0-\d{5}(?:-\d+)?\s*\*\*",
        "",
        body,
    )
    return body


# ───────────────────────── 链接转换（最关键） ─────────────────────────

# markdown 链接正则: 接受中文路径, 但拒绝目标含 '*' (避免误吃破损链接)
# 源文件里的破损 markdown: '[ADD CHGTARI](task/UNC/20.15**（warning, ...)' 
# 会让旧 regex 把整个 'task/UNC/20.15**（warning，rule-0-03168）' 当 URL
MD_LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)\s*][^)\s]*)\)")

# 旧 wiki4 占位（带 version 段）
# 既匹配 [[UDG@20.15.2@Type@Local]] (双层), 也匹配 [UDG@20.15.2@Type@Local] (单层, CONTCATE系列变体)
WIKI4_RE = re.compile(r"\[+UDG@20\.15\.2@([\w]+)@([^\]]+)\]+")


def _resolve_atom(num: str, cmdmap: Dict[str, str]) -> str:
    """'0-00007' -> 'UDG@AtomTask@ADD FLOWFILTER'；未找到则原样保留。"""
    cmd = cmdmap.get(num)
    if not cmd:
        return num
    return f"{NF}@AtomTask@{cmd}"


def convert_markdown_links(text: str, cmdmap: Dict[str, str]) -> str:
    """§5 表：按目标路径分流。
    - (command/UDG/20.15.2/ADD-FLOWFILTER.md) -> [[UDG@MMLCommand@ADD FLOWFILTER]]
    - (configobject/UDG/.../*.md) -> 删
    - (task/UDG/20.15.2/0-XXXXX.md) -> [[UDG@AtomTask@{cmd}]]
    - (0-XXXXX.md) 裸相对路径 -> [[UDG@AtomTask@{cmd}]]
    - (task/UDG/20.15.2/1-XXXXX.md) / (2-XXXXX.md) -> 删
    - (evidence/UDG/.../*.md) -> 删
    - (#) 伪链接 [0-XXXXX](#) -> 删整条 (0-00210 系列特殊写法)
    """
    def repl(m: re.Match) -> str:
        label = m.group(1)
        href = m.group(2)
        # 命令层
        if href.startswith("command/"):
            # command/UDG/20.15.2/ADD-FLOWFILTER.md
            base = href.rsplit("/", 1)[-1]               # ADD-FLOWFILTER.md
            name = re.sub(r"\.md$", "", base)            # ADD-FLOWFILTER
            # 转回命令名（连字符→空格）
            cmd = name.replace("-", " ")
            return f"[[{NF}@MMLCommand@{cmd}]]"
        # 配置对象
        if href.startswith("configobject/"):
            return ""
        # 证据
        if href.startswith("evidence/"):
            return ""
        # 伪链接 [0-XXXXX](#): 删整条
        if href == "#":
            return ""
        # task 链接：按目标文件名分流（不靠 task/ 前缀，因有裸相对路径）
        fname = href.rsplit("/", 1)[-1]
        # atom 0-XXXXX.md
        m_atom = re.match(r"^(0-\d{5})\.md$", fname)
        if m_atom:
            target = _resolve_atom(m_atom.group(1), cmdmap)
            return f"[[{target}]]"
        # atom 占位 0-00XXX.md (★未建对象的占位符): 用显示文字当命令名
        m_placeholder = re.match(r"^0-0?0?XXX\.md$", fname)
        if m_placeholder:
            # 显示文字如 'ADD CPNODEID' / 'SET DEACTIVERATE（★R1.5 atom 待补）'
            clean_label = re.sub(r"[（(★].*?[）)★]", "", label).strip()
            if clean_label:
                return f"[[{NF}@AtomTask@{clean_label}]]"
            return label
        # command-evidence/0-XXXXX (NTPSVR 自引用 evidence 字段, 罕见): 转 [[]]
        if "command-evidence" in href:
            m_ce = re.search(r"0-\d{5}", href)
            if m_ce:
                cmd = cmdmap.get(m_ce.group(0))
                if cmd:
                    return f"[[{NF}@AtomTask@{cmd}]]"
            return label
        # compound 1-XXXXX / feature 2-XXXXX：删链接
        if re.match(r"^[12]-\d{5}\.md$", fname):
            # 若显示文字是中文动作名，留文字；是裸编号，删整条
            if re.match(r"^\d+-\d{5}$", label):
                return ""
            return label
        # 其他（以防万一）：原样
        return m.group(0)

    return MD_LINK_RE.sub(repl, text)


def replace_bare_atom_refs(text: str, cmdmap: Dict[str, str]) -> str:
    """§5: 正文中'裸'出现的 0-XXXXX (不在 markdown 链接/wiki 占位/括号里) 也按编号转。
    例: 'License 0-00019 之后' -> 'License [[UDG@AtomTask@SET LICENSESWITCH]] 之后'
        '须 0-00144 先生效'      -> '须 [[UDG@AtomTask@ADD AUTOSCALINGSRBFD]] 先生效'
        '引用 0-00215 产出'      -> '引用 [[UDG@AtomTask@ADD IPSECPOLICY]] 产出'
        '由 feature-rule 0-00082 表达' -> '由 feature-rule 表达'
        '§0-00003'                -> ''
        'selection_rule 0-00006'  -> 'selection_rule'
        '0-00316/0-00312'         -> '原编号段保留为引文'  # 太复杂, 整体替换 -> 各查各的
    """
    # 1) '§0-XXXXX' / '§ 0-XXXXX' 引用 -> 删
    text = re.sub(r"§\s*0-\d{5}(?:-\d+)?", "", text)
    # 2) 'feature-rule 0-XXXXX' / 'selection_rule 0-XXXXX' -> 删编号 (rule-0 删法一致)
    text = re.sub(
        r"(feature-rule|selection_rule)\s*0-\d{5}(?:-\d+)?",
        r"\1",
        text,
    )
    # 3) '0-XXXXX/0-YYYYY' 多个并列 -> 各查各的转 [[...]]
    def repl_multi(m: re.Match) -> str:
        nums = m.group(0)
        out = []
        for n in re.findall(r"0-\d{5}", nums):
            cmd = cmdmap.get(n)
            if cmd:
                out.append(f"[[{NF}@AtomTask@{cmd}]]")
            else:
                out.append(n)
        return "/".join(out)
    text = re.sub(r"(?:0-\d{5}(?:/0-\d{5})+)", repl_multi, text)

    # 4) 裸的 0-XXXXX (前后非路径/数字字符): 转 [[UDG@AtomTask@{cmd}]]
    def repl_one(m: re.Match) -> str:
        n = m.group(0)
        cmd = cmdmap.get(n)
        if cmd:
            return f"[[{NF}@AtomTask@{cmd}]]"
        return n
    text = re.sub(r"(?<![\w/.-])0-\d{5}(?![a-zA-Z0-9/])", repl_one, text)
    return text


def convert_wiki4_placeholders(text: str, cmdmap: Dict[str, str]) -> str:
    """§5.1 旧 wiki4 占位：去 20.15.2 段；按 Type 分流。
    - @MMLCommand@ADD URR -> [[UDG@MMLCommand@ADD URR]]
    - @Task@0-XXXXX -> [[UDG@AtomTask@{cmd}]]
    - @Feature@GWFD-110311 -> [[UDG@Feature@GWFD-110311]]
    - @DecisionPoint@0-XXXXX -> 删占位，留周围语义
    - @ConfigObject@XXX -> 删
    """
    def repl(m: re.Match) -> str:
        typ, local = m.group(1), m.group(2)
        if typ == "MMLCommand":
            return f"[[{NF}@MMLCommand@{local}]]"
        if typ == "Task":
            # local 是 0-XXXXX
            return f"[[{_resolve_atom(local, cmdmap)}]]"
        if typ == "Feature":
            return f"[[{NF}@Feature@{local}]]"
        if typ == "DecisionPoint":
            return ""  # 删占位，留周围文字
        if typ == "ConfigObject":
            return ""
        # 兜底
        return m.group(0)
    return WIKI4_RE.sub(repl, text)


# ───────────────────────── 正文括号去编号 ─────────────────────────

def strip_paren_atom_num(text: str) -> str:
    """§4.3 括号内纯 0-XXXXX 编号注释删。
    - '(0-00037)' -> 整括号删
    - '（0-00285 切片绑逻辑接口）' -> '（切片绑逻辑接口）'
    - '（见 0-00032）' -> 删
    - '（引用 0-00071.VRFNAME）' -> '（引用 ）' (0-XXXXX.XXX 形式, 删编号段, 留前后字)
    - '（0-00213:PROPOSALNUMBER）' -> '（）' (0-XXXXX:XXX 形式)
    - '<0-00215 产出>' -> '< 产出>' (尖括号形式, 0-XXXXX 也按编号注释删)
    - 不动 (默认)/(critical)/(GWFD-110311) 等
    """
    # 0) '0-XXXXX.XXX' / '0-XXXXX:XXX' 编号+点/冒号+参数引用形式: 删编号段, 保留前后
    text = re.sub(
        r"(0-\d{5})\s*[.:]\s*[A-Za-z_][\w]*",
        "",
        text,
    )
    # 0.05) 'command-evidence/0-XXXXX' (NTPSVR 自引用) 整段删 (旧业务交叉引用格式, 已废)
    text = re.sub(r"command-evidence/0-\d{5}", "", text)
    # 0.1) 兜底: '（）' 空括号 -> 删整括号 (避免留空)
    text = re.sub(r"[（(]\s*[)）]", "", text)
    # 0.15) 括号内空白+助词尾随 -> 删整括号 ('（ 强约束）' / '（   ）')
    text = re.sub(r"[（(]\s{1,}(?:强约束|约束|建议|可选|必选|默认|备注|提示|注|说明)\s*[)）]", "", text)
    # 0.2) 括号内只剩空白 -> 删整括号
    text = re.sub(r"[（(]\s{2,}[)）]", "", text)
    # 0.6) '（引用 ）' / '（slice  ）' 等括号内只剩介词+空格 -> 兜底删整括号
    text = re.sub(r"[（(]\s*(?:引用|参引|参见|引自|详见|见|为|指|指向|即|表示|参)\s*[)）]", "", text)
    # 1) 整括号里只有 0-XXXXX（可带空白）：删整括号（连同括号字符）
    text = re.sub(r"[（(]\s*0-\d{5}\s*[)）]", "", text)
    # 2) 括号里 0-XXXXX 后跟其他文字：删编号 + 删多余空白
    text = re.sub(r"[（(]\s*0-\d{5}\s+", "（", text)
    # 3) 行尾 '见 0-XXXXX' / '参见 0-XXXXX' / '（见 0-XXXXX）' 残留：
    text = re.sub(r"(?:参见|见|参)\s+0-\d{5}\b", "", text)
    # 4) 尖括号 ' <0-XXXXX ...>' / '<...0-XXXXX...>' -> 删 0-XXXXX 编号
    #    例: '<0-00215 产出>' -> '< 产出>'
    text = re.sub(r"<([^<>]{0,30})0-\d{5}([^<>]{0,30})>", r"<\1\2>", text)
    return text


# ───────────────────────── 段落切分（为了 §4.6 优先级） ─────────────────────────

def _protect_code_blocks(body: str) -> Tuple[str, List[str]]:
    """§4.3 硬约束: 代码块（围栏 + 行内）不被任何 strip 函数修改。
    把 ```...``` 围栏代码块和 `...` 行内代码替换为占位符, 跑完所有 strip 后还原。

    返回 (protected_body, placeholders) —— placeholders[i] 是第 i 个占位符对应的原文。
    """
    placeholders: List[str] = []

    # 1) 围栏代码块 ```...``` (含可选语言标识). re.DOTALL 让 . 跨行.
    def repl_fence(m: re.Match) -> str:
        placeholders.append(m.group(0))
        return f"\x00CODEBLOCK{len(placeholders)-1}\x00"
    body = re.sub(r"```.*?```", repl_fence, body, flags=re.S)

    # 2) 行内代码 `...` (非贪婪, 不跨行, 不允许嵌套反引号)
    def repl_inline(m: re.Match) -> str:
        placeholders.append(m.group(0))
        return f"\x00CODEINLINE{len(placeholders)-1}\x00"
    body = re.sub(r"`[^`\n]+`", repl_inline, body)

    return body, placeholders


def _restore_code_blocks(body: str, placeholders: List[str]) -> str:
    """把占位符还原成原文 code block。"""
    for i, orig in enumerate(placeholders):
        body = body.replace(f"\x00CODEBLOCK{i}\x00", orig)
        body = body.replace(f"\x00CODEINLINE{i}\x00", orig)
    return body


def process_body(body: str, cmdmap: Dict[str, str]) -> str:
    """按迁移指南的优先级顺序处理正文：
    1. §4.6 关联段整段拆解（最优先）
    2. §4.4 决策点标题去 DP 编号
    3. §4.5 约束段去 rule 编号
    4. §5 markdown 链接转换
    5. §5.1 旧 wiki4 占位转换
    6. §4.4 正文 DP 编号语义改写（**必须早于** replace_bare_atom_refs,
       否则 DP 0-XXXXX 中的 0-XXXXX 被替换成 [[UDG@AtomTask@CMD]],
       后续 strip_dp_inline_refs 的 "仅在 DP 0-XXXXX 标注" 等模板都失效）
    7. §5.2 正文裸 0-XXXXX -> [[UDG@AtomTask@{cmd}]]
    8. §4.3 正文括号去编号
    9. 兜底: 清理占位删除后残留的双重粗体 '****'
    10. 兜底: '**rule-0-XXXXX**' 单独成粗体标题时删
    """
    # 0) §4.3 硬约束: 保护 code block, strip 完再还原
    body, placeholders = _protect_code_blocks(body)

    # 1) 关联段整段重构
    body = strip_assoc_section(body)
    # 2) 决策点标题去 DP
    body = transform_decision_title(body)
    # 3) 约束段去 rule
    body = strip_rule_refs(body)
    # 4) markdown 链接
    body = convert_markdown_links(body, cmdmap)
    # 5) wiki4 占位
    body = convert_wiki4_placeholders(body, cmdmap)
    # 6) DP 编号语义改写 (先于 replace_bare_atom_refs!)
    body = strip_dp_inline_refs(body)
    # 7) 正文中裸 0-XXXXX -> [[UDG@AtomTask@{cmd}]]
    body = replace_bare_atom_refs(body, cmdmap)
    # 8) 括号去编号
    body = strip_paren_atom_num(body)
    # 9) 兜底: 清理占位删除后残留的双重粗体 '****'
    body = strip_orphan_bold_dp_marker(body)
    # 10) 兜底: '**rule-0-XXXXX**' 单独成粗体标题时删 (0-00214 等)
    body = strip_standalone_rule_marker(body)

    # 最后: 还原 code block
    body = _restore_code_blocks(body, placeholders)
    return body


# ───────────────────────── YAML 输出（§3 字段映射） ─────────────────────────

def render_yaml(scalar: Dict[str, str]) -> str:
    """输出新 YAML 8 字段，固定顺序：id / type / name / name_zh / nf / version / ref / status
    name  = 命令名（= id 的 local 段）
    name_zh = 旧 task_logical_name（= H1 的配置动作名）
    ref  = UDG@MMLCommand@{命令} （去 version）
    """
    name = scalar["ref"].split("@")[-1].strip()
    name_zh = scalar.get("task_logical_name", "").strip()
    return "\n".join([
        "---",
        f'id: "{NF}@AtomTask@{name}"',
        f'type: "AtomTask"',
        f'name: "{name}"',
        f'name_zh: "{name_zh}"',
        f'nf: "{NF}"',
        f'version: "{VERSION}"',
        f'ref: "{NF}@MMLCommand@{name}"',
        f'status: "draft"',
        "---",
        "",
    ])


# ───────────────────────── 单文件迁移 ─────────────────────────

def migrate_one(src_path: Path, cmdmap: Dict[str, str]) -> Tuple[Path, str]:
    text = src_path.read_text(encoding="utf-8")
    scalar, _, _, body = extract_yaml_and_body(text)
    cmd = scalar["ref"].split("@")[-1].strip()

    # 正文转换
    new_body = process_body(body, cmdmap)

    # 拼接: YAML + 正文 + ## 边 段
    new_yaml = render_yaml(scalar)
    new_text = new_yaml + new_body.rstrip() + "\n\n" + "## 边\n" + f"- 对应命令: [[{NF}@MMLCommand@{cmd}]]\n"

    # 输出文件名 = 完整 ID
    out_name = f"{NF}@AtomTask@{cmd}.md"
    out_path = DST_DIR / out_name
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(new_text, encoding="utf-8")
    return out_path, cmd


# ───────────────────────── 主入口 ─────────────────────────

def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(
        prog="migrate_old_atoms",
        description="迁移旧 atom (0-XXXXX.md) → 新版 AtomTask ({NF}@AtomTask@{COMMAND}.md)",
    )
    parser.add_argument("--nf", default=DEFAULT_NF,
                        help=f"网元 (default: {DEFAULT_NF})")
    parser.add_argument("--version", default=DEFAULT_VERSION,
                        help=f"产品版本 (default: {DEFAULT_VERSION})")
    parser.add_argument("filename", nargs="?", default=None,
                        help="只迁指定编号 (用于 dry-run), e.g. 0-00007.md")
    args = parser.parse_args(argv[1:])

    # 根据参数覆盖全局路径
    global NF, VERSION, SRC_DIR, DST_DIR
    NF = args.nf
    VERSION = args.version
    SRC_DIR = ROOT / "assets" / "task" / NF / VERSION
    DST_DIR = ROOT / "三层图谱资产" / "AtomTask" / NF / VERSION

    if not SRC_DIR.is_dir():
        print(f"ERR: src dir not found: {SRC_DIR}", file=sys.stderr)
        return 2

    cmdmap = build_command_map(SRC_DIR)
    print(f"[build_command_map] {len(cmdmap)} entries (NF={NF}, VERSION={VERSION})",
          file=sys.stderr)

    targets: List[Path] = []
    if args.filename:
        p = SRC_DIR / args.filename
        if not p.is_file():
            print(f"ERR: {p} not found", file=sys.stderr)
            return 2
        targets.append(p)
    else:
        for f in sorted(SRC_DIR.iterdir()):
            if ATOM_NUM_RE.match(f.name):
                targets.append(f)

    print(f"[migrate] {len(targets)} files", file=sys.stderr)
    written = 0
    for p in targets:
        out_path, cmd = migrate_one(p, cmdmap)
        written += 1
        if args.filename:
            print(f"[dry-run] {p.name} -> {out_path.name}", file=sys.stderr)
            print("=" * 60, file=sys.stderr)
            print(out_path.read_text(encoding="utf-8"))
    print(f"[done] {written} migrated", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
