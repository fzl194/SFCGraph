"""概述md识别 + 13 节解析（移植 step4，补 原理概述/计费与话单 节）。

概述md固定 13 节：适用NF/定义/客户价值/应用场景/可获得性/与其他特性的交互/
对系统的影响/应用限制/原理概述/计费与话单/特性规格/遵循标准/发布历史。
全部按 #### [节名](anchor) 锚点拆分，原文保留为 *_raw。
"""
from __future__ import annotations

import os
import re
from pathlib import Path

SECTION_ANCHOR_RE = re.compile(r"^####\s*\[([^\]]+)\]")
OVERVIEW_SECTIONS = {"定义", "可获得性", "应用场景"}
FEATURE_ID_RE = re.compile(r"^((?:GWFD|WSFD|IPFD|NPFD|SFFD)-\d{3,6})")

# schema 13 节 → *_raw 字段名
SECTION_KEYS = {
    "适用NF": "applicable_nf_raw",
    "定义": "definition_raw",
    "客户价值": "customer_value_raw",
    "应用场景": "application_scenario_raw",
    "可获得性": "availability_raw",
    "与其他特性的交互": "feature_interaction_raw",
    "对系统的影响": "system_impact_raw",
    "应用限制": "restrictions_raw",
    "原理概述": "principle_raw",
    "计费与话单": "charging_raw",
    "特性规格": "spec_raw",
    "遵循标准": "standards_raw",
    "发布历史": "release_history_raw",
}


def parse_sections(content: str) -> dict[str, str]:
    """按 #### [节名] 拆分 → {节名: 节正文}。"""
    sections: dict[str, str] = {}
    current, lines = None, []
    for line in content.split("\n"):
        m = SECTION_ANCHOR_RE.match(line)
        if m:
            if current:
                sections[current] = "\n".join(lines).strip()
            current, lines = m.group(1), []
        elif current:
            lines.append(line)
    if current:
        sections[current] = "\n".join(lines).strip()
    return sections


def collect_raw_fields(sections: dict[str, str]) -> dict[str, str]:
    """13 节 → *_raw 字段，缺节给空串。"""
    return {field: sections.get(name, "") for name, field in SECTION_KEYS.items()}


def is_overview_by_structure(content: str) -> bool:
    found = OVERVIEW_SECTIONS.intersection(set(SECTION_ANCHOR_RE.findall(content)))
    return len(found) >= 2


def classify_doc_type(filename: str, content: str, dir_path: str = "") -> str:
    """根据文件名/H1/目录推断 doc_type（移植 step4，简洁写法）。"""
    h1_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    h1 = h1_match.group(1).strip() if h1_match else ""
    if "概述" in filename:
        return "overview"
    if h1:
        if "激活" in h1 or re.search(r"^配置", h1):
            return "activation"
        if "调测" in h1:
            return "debug"
        if "参考信息" in h1:
            return "reference"
        if "原理" in h1:
            return "principle"
        if "流程" in h1:
            return "flow"
    if "实现原理" in (os.path.basename(dir_path) if dir_path else ""):
        return "principle"
    return "other"


def is_direct_child(file_path: str, feature_id: str) -> bool:
    """文件是否直接在特性目录下（移植 step4）。"""
    parent_name = os.path.basename(os.path.dirname(file_path))
    filename = os.path.basename(file_path)
    if filename.startswith(feature_id) and FEATURE_ID_RE.match(parent_name) \
            and FEATURE_ID_RE.match(parent_name).group(1) == feature_id:
        return True
    m = FEATURE_ID_RE.match(parent_name)
    if m and m.group(1) == feature_id:
        return True
    return filename.startswith(feature_id)


def find_overview_md(feature_id: str, file_paths: list[str], project_root: Path) -> tuple[list[str], list[tuple[str, str]]]:
    """为特性找概述md（支持多概述：代际 SubFeature 场景）+ 构建全部 doc_assets。

    返回 (overview_paths: list[str], doc_assets: [(file_path, doc_type)])。
    多概述时 overview_paths 含全部候选（按优先级排序）。

    概述识别优先级（互斥：上一级命中则不再走下一级，避免非概述混入）：
      1. 文件名以 fid 开头 + 含"概述"  （避免子文档文件名碰巧含"概述"被误判）
      2. 仅在 priority 1 未命中时启用：文件名以 fid 开头 + 直接子目录 + 不含非概述关键词
         （排除"参考信息/激活/调测/原理/部署/流程/需求/规划/实现"等子文档名）
      3. 仅1文件
      4. 内容结构验证（定义/可获得性/应用场景 三锚点 ≥2）
    """
    # 子文档关键词（这些不是特性概述，是补充文档）
    NON_OVERVIEW_KEYWORDS = ("参考信息", "激活", "调测", "原理", "部署", "流程", "需求",
                              "规划", "实现", "应用", "操作", "参考", "描述")

    def _is_real_overview(fp: str) -> bool:
        """文件名以 fid 开头 + 含"概述"——避免子文档（如"规划概述"）误判。"""
        return os.path.basename(fp).startswith(feature_id) and "概述" in os.path.basename(fp)

    def _is_priority2_overview(fp: str) -> bool:
        """priority 2 兜底：文件名以 fid 开头 + 直接子目录 + 不是子文档。"""
        fn = os.path.basename(fp)
        if not (fn.startswith(feature_id) and is_direct_child(fp, feature_id)):
            return False
        return not any(kw in fn for kw in NON_OVERVIEW_KEYWORDS)

    overview_candidates: list[tuple[int, str]] = []
    for fp in file_paths:
        if _is_real_overview(fp):
            overview_candidates.append((1, fp))
    # priority 2 兜底：仅当 priority 1 未命中时启用
    if not overview_candidates:
        for fp in file_paths:
            if _is_priority2_overview(fp):
                overview_candidates.append((2, fp))
    if not overview_candidates and len(file_paths) == 1:
        overview_candidates.append((3, file_paths[0]))
    if not overview_candidates:
        for fp in file_paths:
            abs_fp = Path(fp) if Path(fp).is_absolute() else project_root / fp
            if abs_fp.exists() and is_overview_by_structure(abs_fp.read_text(encoding="utf-8", errors="ignore")):
                overview_candidates.append((4, fp))

    overview_candidates.sort(key=lambda x: (x[0], x[1]))
    overview_paths = [fp for _, fp in overview_candidates]

    doc_assets: list[tuple[str, str]] = []
    for fp in overview_paths:
        doc_assets.append((fp, "overview"))
    for fp in file_paths:
        if fp in overview_paths:
            continue
        abs_fp = Path(fp) if Path(fp).is_absolute() else project_root / fp
        content = abs_fp.read_text(encoding="utf-8", errors="ignore") if abs_fp.exists() else ""
        doc_assets.append((fp, classify_doc_type(os.path.basename(fp), content, os.path.dirname(fp))))
    return overview_paths, doc_assets


def detect_variant_dimensions(overview_paths: list[str], feature_id: str) -> list[dict]:
    """从多概述路径检测 variant_dimensions（schema §4.3：差异留在 variant_dimensions）。

    当前识别"代际"维度。匹配模式（按优先级）：
      - 目录前缀 /{gen}/ 或 /{gen}_ （如 /2_3G会话管理/、/4G_xxx）
      - 文件名 / 路径片段 _{gen}_ （如 GWFD_X_4G_yyy.md）
      - 中文括号（{gen}部分）：（4G部分）/（5G部分）等
      - 英文括号 ({gen}): (4G)/5G)
    返回 [{name: "代际", values: [...], overview_paths: {gen: path}}] 或 []。
    """
    if len(overview_paths) <= 1:
        return []
    generation_to_path: dict[str, str] = {}
    for p in overview_paths:
        for gen in ("2_3G", "4G", "5G"):
            # 多种代际标记形式
            if (f"/{gen}" in p) or (f"_{gen}_" in p) or \
               (f"（{gen}" in p) or (f"({gen}" in p):
                if gen not in generation_to_path:
                    generation_to_path[gen] = p
                break
    if len(generation_to_path) >= 2:
        return [{"name": "代际", "values": sorted(generation_to_path.keys()),
                 "overview_paths": generation_to_path}]
    return []


def _pick_primary_overview(overview_paths: list[str], feature_id: str) -> str:
    """多概述时选主概述（用于节点的 source_path）：优先级最高（find_overview_md 已排序）。"""
    return overview_paths[0] if overview_paths else ""


def extract_applicable_nf(sections: dict[str, str]) -> list[str]:
    """从 适用NF 节归一化；空则回退 可获得性 的涉及NF表。"""
    for key in sections:
        if re.match(r"适\s*用\s*N\s*F", key) and sections[key]:
            return [nf.strip() for nf in re.split(r"[、，,\n]", sections[key]) if nf.strip()]
    avail = sections.get("可获得性", "")
    in_nf_table = False
    for line in avail.split("\n"):
        parts = [p.strip() for p in line.strip().split("|")]
        parts = [re.sub(r"^\*\*(.+?)\*\*$", r"\1", p) for p in parts if p and p != "---"]
        if not parts:
            continue
        first = parts[0]
        if first in ("涉及NF", "适用NF", "涉及网元", "适用网元"):
            in_nf_table = True
            continue
        if in_nf_table and parts:
            result = [nf.strip() for nf in re.split(r"[、，,\n]", parts[0]) if nf.strip()]
            if result and any("-" in nf or "U" in nf.upper() for nf in result):
                return result
            in_nf_table = False
    return []


def extract_first_release(sections: dict[str, str]) -> str:
    text = sections.get("发布历史", "")
    for line in text.split("\n"):
        if "首次发布" in line:
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) >= 2:
                v = re.sub(r"<[^>]+>", "", parts[1])
                v = re.sub(r"^(UDG|UNC)\s*", "", v)
                v = re.sub(r"\s*及后续版本.*$", "", v)
                return v.strip()
    return ""


def extract_standards(sections: dict[str, str]) -> list[dict]:
    """从 遵循标准 节解析标准列表（移植 step4，3 种表格格式）。

    格式1: | 标准类别 | 标准编号 | 标准名称 |  (3列)
    格式2: | 标准类别 | 标准名称 |  (2列, 名称含编号)
    格式3: | 文档 | 描述 |  (2列, RFC格式)
    返回 [{category, number, name}]。
    """
    text = sections.get("遵循标准", "")
    if not text:
        return []
    category_words = {"3GPP", "RFC", "IETF", "ITU-T", "IEEE", "ISO"}
    standards: list[dict] = []
    table_type: str | None = None
    for line in text.split("\n"):
        parts = [p.strip() for p in line.strip().split("|")]
        parts = [p for p in parts if p and p != "---"]
        parts = [re.sub(r"^\*\*(.+?)\*\*$", r"\1", p) for p in parts]
        if len(parts) >= 3 and parts[0] == "标准类别":
            table_type = "three_col"
            continue
        elif len(parts) == 2 and parts[0] == "标准类别" and parts[1] == "标准名称":
            table_type = "category_name"
            continue
        elif len(parts) == 2 and parts[0] == "文档" and parts[1] == "描述":
            table_type = "doc_desc"
            continue
        elif parts and parts[0] in ("标准类别", "标准编号", "标准名称", "文档", "描述"):
            continue
        if not parts:
            continue
        if table_type == "three_col" and len(parts) >= 3:
            standards.append({"category": parts[0], "number": parts[1], "name": parts[2]})
        elif table_type == "category_name" and len(parts) >= 2:
            category, full_name = parts[0], parts[1]
            num_match = re.match(
                r"(?:3GPP\s+)?(TS\s+\d+\.\d+|TS\s+\d+)"
                r"|(?:ITU-T\s+)?(Recommendation\s+\S+)"
                r"|(RFC\s+\d+)", full_name)
            number = ""
            if num_match:
                number = num_match.group(1) or num_match.group(2) or num_match.group(3) or ""
            standards.append({"category": category, "number": number.strip(), "name": full_name})
        elif table_type == "doc_desc" and len(parts) >= 2:
            raw_num = parts[0].strip()
            if raw_num.upper().startswith("RFC"):
                category, number = "RFC", raw_num
            else:
                category, number = "RFC", f"RFC {raw_num}"
            standards.append({"category": category, "number": number, "name": parts[1]})
        elif not table_type and len(parts) >= 3:
            if parts[0] not in category_words or (parts[1] and parts[1][0].isdigit()):
                standards.append({"category": parts[0], "number": parts[1], "name": parts[2]})
    return standards
