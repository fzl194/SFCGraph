"""
step4_extract_l1.py

Step 4: L1 抽取 — 从概述md提取Feature结构化属性

前置:
  - data/UDG_features.csv / data/UNC_features.csv  (Step 1)
  - data/UDG_feature_files.csv / data/UNC_feature_files.csv  (Step 2)

输出:
  - data/l1_feature_attributes.csv  (全部特性的基础属性)
  - data/l1_feature_dependency.csv  (特性间依赖关系)
  - data/l1_feature_license.csv     (License映射)
  - data/l1_doc_assets.csv          (DocAsset分类)
  - data/l1_extraction_report.md    (抽取报告)

识别规则(从实际md文件内容总结):
  概述md有固定的13节目录索引:
    适用NF / 定义 / 客户价值 / 应用场景 / 可获得性 /
    与其他特性的交互 / 对系统的影响 / 应用限制 / 原理概述 /
    计费与话单 / 特性规格 / 遵循标准 / 发布历史

  识别优先级:
    1. 文件名含"概述" → 就是概述md
    2. 文件名以feature_id开头 + 直接在特性目录下(不在子目录中) → 概述md
    3. 特性只有1个md文件 → 它就是概述
    验证: 内容含 [定义] + [可获得性] + [应用场景] 三个锚点

  子文件doc_type通过H1/目录名识别:
    activation: H1含"激活"或"配置"
    debug: H1含"调测"
    reference: H1含"参考信息"
    principle: H1含"原理"或目录名含"实现原理"
    flow: H1含"流程"
    index: 仅H1无实质内容
    other: 以上都不匹配
"""

import csv
import hashlib
import os
import re
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent
DATA_DIR = BASE_DIR / "data"

# =====================================================================
# Section 解析用的标题锚点模式
# =====================================================================
SECTION_ANCHOR_RE = re.compile(r"####\s*\[([^\]]+)\]")
OVERVIEW_SECTIONS = {"定义", "可获得性", "应用场景"}
FEATURE_ID_RE = re.compile(r"^((?:GWFD|WSFD|IPFD|NPFD|SFFD)-\d{3,6})")
FEATURE_ID_SEARCH_RE = re.compile(r"((?:GWFD|WSFD|IPFD|NPFD|SFFD)-\d{3,6})")


# =====================================================================
# 1. 加载 Step 1 / Step 2 数据
# =====================================================================
def resolve_path(fp):
    """将相对路径转为绝对路径"""
    p = Path(fp)
    if p.is_absolute():
        return p
    return PROJECT_ROOT / fp


def load_features(product):
    """加载特性清单, 返回 dict[feature_id] -> row"""
    path = DATA_DIR / f"{product}_features.csv"
    features = {}
    with open(path, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            features[row["feature_id"]] = row
    return features


def load_file_mappings(product):
    """加载文件映射, 返回 dict[feature_id] -> [file_path, ...]"""
    path = DATA_DIR / f"{product}_feature_files.csv"
    mappings = defaultdict(list)
    with open(path, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            mappings[row["feature_id"]].append(row["file_path"])
    return mappings


# =====================================================================
# 2. ID生成器 & 文档标题读取
# =====================================================================
def make_id(*parts):
    """拼接parts生成短id (hash前8位)"""
    raw = ":".join(parts)
    return hashlib.md5(raw.encode()).hexdigest()[:8]


def read_doc_title(file_path):
    """读取md文件的H1标题"""
    abs_fp = resolve_path(file_path)
    if not abs_fp.exists():
        return ""
    try:
        with open(abs_fp, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("# "):
                    return line[2:].strip()
                if line and not line.startswith("#"):
                    break
    except Exception:
        pass
    return ""


# =====================================================================
# 3. 识别概述md
# =====================================================================
def classify_doc_type(filename, content, dir_path=""):
    """根据文件名、H1标题和目录推断doc_type"""
    h1_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    h1 = h1_match.group(1).strip() if h1_match else ""

    # 概述判定
    if "概述" in filename:
        return "overview"

    # H1前缀判定
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

    # 目录名判定
    dir_name = os.path.basename(dir_path) if dir_path else ""
    if "实现原理" in dir_name:
        return "principle"

    return "other"


def is_overview_by_structure(content):
    """检查md内容是否含标准概述section结构"""
    anchors = SECTION_ANCHOR_RE.findall(content)
    found = OVERVIEW_SECTIONS.intersection(set(anchors))
    return len(found) >= 2  # 至少2个核心section即认为是概述


def is_direct_child(file_path, feature_id):
    """判断文件是否直接在特性目录下(不在子目录中)

    逻辑: 文件所在目录名以 feature_id 开头,
    或者文件名以 feature_id 开头且不在更深的子目录中。
    """
    parent = os.path.dirname(file_path)
    parent_name = os.path.basename(parent)
    filename = os.path.basename(file_path)

    # 文件名以 feature_id 开头 + 在特性目录的直接下级
    if filename.startswith(feature_id) and FEATURE_ID_RE.match(parent_name):
        if FEATURE_ID_RE.match(parent_name).group(1) == feature_id:
            return True

    # 文件直接在以 feature_id 命名的目录下
    fid_in_parent = FEATURE_ID_RE.match(parent_name)
    if fid_in_parent and fid_in_parent.group(1) == feature_id:
        return True

    # 不在任何子特性目录下
    parts = Path(file_path).parts
    sub_dirs_after_feature = []
    found_feature = False
    for part in parts:
        m = FEATURE_ID_RE.match(part)
        if m:
            if m.group(1) == feature_id:
                found_feature = True
            else:
                if found_feature:
                    sub_dirs_after_feature.append(part)
        elif found_feature and "." not in part:
            sub_dirs_after_feature.append(part)

    # 如果文件名以feature_id开头, 且没有更深的子特性目录
    if filename.startswith(feature_id) and not sub_dirs_after_feature:
        return True

    return False


def find_overview_md(feature_id, file_paths):
    """
    为一个特性找到概述md文件。

    优先级:
      1. 文件名含"概述"
      2. 文件名以feature_id开头 + 直接在特性目录下
      3. 特性只有1个md文件

    返回: (overview_path, doc_assets)
      doc_assets = [(file_path, doc_type), ...]
    """
    overview_candidates = []
    other_files = []

    for fp in file_paths:
        filename = os.path.basename(fp)
        if "概述" in filename:
            overview_candidates.append((1, fp))  # 优先级最高
        elif filename.startswith(feature_id) and is_direct_child(fp, feature_id):
            overview_candidates.append((2, fp))
        else:
            other_files.append(fp)

    # 如果没有通过规则1/2找到的, 且只有1个文件, 那就是它
    if not overview_candidates and len(file_paths) == 1:
        overview_candidates.append((3, file_paths[0]))

    # 如果还是没有, 尝试通过内容结构验证
    if not overview_candidates:
        for fp in file_paths:
            abs_fp = resolve_path(fp)
            if abs_fp.exists():
                with open(abs_fp, encoding="utf-8") as f:
                    content = f.read()
                if is_overview_by_structure(content):
                    overview_candidates.append((4, fp))

    # 选择优先级最高的
    overview_path = None
    if overview_candidates:
        overview_candidates.sort(key=lambda x: x[0])
        overview_path = overview_candidates[0][1]

    # 构建 doc_assets
    doc_assets = []
    all_except_overview = [fp for fp in file_paths if fp != overview_path]

    if overview_path:
        doc_assets.append((overview_path, "overview"))

    for fp in all_except_overview:
        filename = os.path.basename(fp)
        dir_path = os.path.dirname(fp)
        abs_fp = resolve_path(fp)
        if abs_fp.exists():
            with open(abs_fp, encoding="utf-8") as f:
                content = f.read()
            doc_type = classify_doc_type(filename, content, dir_path)
        else:
            doc_type = "other"
        doc_assets.append((fp, doc_type))

    return overview_path, doc_assets


# =====================================================================
# 3. 解析概述md的结构化内容
# =====================================================================
def parse_overview_sections(content):
    """
    将概述md按 #### 标题拆分为 section dict。

    返回: dict[section_name] -> section_content (文本)
    """
    sections = {}
    current_name = None
    current_lines = []

    for line in content.split("\n"):
        m = SECTION_ANCHOR_RE.match(line)
        if m:
            if current_name:
                sections[current_name] = "\n".join(current_lines).strip()
            current_name = m.group(1)
            current_lines = []
        elif current_name:
            current_lines.append(line)

    if current_name:
        sections[current_name] = "\n".join(current_lines).strip()

    return sections


def extract_applicable_nf(sections):
    """从 '适用NF' section 提取NF列表

    注意: 部分文档标题为"适用 N F"(有空格), 但section解析时会保留原始标题。
    这里同时查找两种key。
    回退: 如果适用NF为空，从 '可获得性' section 中提取涉及NF。
    """
    # P1-3.1: 容忍各种空格/换行变体（如 "适用 N F"、"适用N F" 等）
    nf_text = ""
    for key in sections:
        if re.match(r"适\s*用\s*N\s*F", key):
            nf_text = sections[key]
            break
    text = nf_text
    if text:
        nfs = re.split(r"[、，,\n]", text)
        return [nf.strip() for nf in nfs if nf.strip()]

    # 回退: 从 [可获得性] section 中提取NF
    availability = sections.get("可获得性", "")
    if not availability:
        return []
    # 查找表头为 "涉及NF" 或 "适用NF" 的表格，取第一个数据行的第一列
    in_nf_table = False
    for line in availability.split("\n"):
        stripped = line.strip()
        parts = [p.strip() for p in stripped.split("|")]
        parts = [p for p in parts if p and p != "---"]
        if not parts:
            continue
        # 清理粗体
        first = re.sub(r"^\*\*(.+?)\*\*$", r"\1", parts[0])
        # 检测表头行
        if first in ("涉及NF", "适用NF", "涉及网元", "适用网元"):
            in_nf_table = True
            continue
        # 如果在NF表格中，取数据行
        if in_nf_table and len(parts) >= 1:
            nf_text = parts[0]
            nfs = re.split(r"[、，,\n]", nf_text)
            result = [nf.strip() for nf in nfs if nf.strip()]
            if result and any("-" in nf or "U" in nf.upper() for nf in result):
                return result
            in_nf_table = False
    return []


def extract_definition(sections):
    """从 '定义' section 提取全部纯文本段落"""
    text = sections.get("定义", "")
    if not text:
        return ""
    lines = text.split("\n")
    result_lines = []
    for line in lines:
        stripped = line.strip()
        # 跳过表格行、图片链接、空行
        if stripped.startswith("|") or stripped.startswith("!") or stripped.startswith(">"):
            continue
        if stripped:
            result_lines.append(stripped)
    return " ".join(result_lines) if result_lines else ""


def extract_customer_value(sections):
    """从 '客户价值' section 提取 — P1-3.2: 去掉表格行和引用行，只保留纯文本"""
    text = sections.get("客户价值", "")
    if not text:
        return ""
    lines = text.split("\n")
    result = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") or stripped == "---" or stripped.startswith(">"):
            continue
        if stripped:
            result.append(stripped)
    if result:
        return " ".join(result)
    # 如果全部是表格/引用，提取表格中的文本内容（非表头/非分隔行）
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|"):
            cells = [c.strip() for c in stripped.split("|")]
            # 清理粗体标记而不是丢弃
            cells = [re.sub(r"^\*\*(.+?)\*\*$", r"\1", c) for c in cells]
            cells = [c for c in cells if c and c != "---"]
            # 跳过表头行
            if cells and cells[0] in ("受益方", "受益描述", "客户价值"):
                continue
            result.extend(cells)
    return " ".join(result) if result else ""


def extract_application_scenario(sections):
    """从 '应用场景' section 提取"""
    text = sections.get("应用场景", "")
    if not text:
        return ""
    # 去掉表格部分, 只取描述段落
    lines = text.split("\n")
    desc_lines = []
    for line in lines:
        if line.strip().startswith("|") or line.strip().startswith(">"):
            break
        if line.strip():
            desc_lines.append(line.strip())
    return "\n".join(desc_lines) if desc_lines else text.split("\n\n")[0]


def extract_system_impact(sections):
    """从 '对系统的影响' section 提取"""
    return sections.get("对系统的影响", "")


def extract_restrictions(sections):
    """从 '应用限制' section 提取"""
    return sections.get("应用限制", "")


def extract_spec(sections):
    """从 '特性规格' section 提取"""
    return sections.get("特性规格", "")


def extract_standards(sections):
    """从 '遵循标准' section 解析标准列表

    三种表格格式:
      格式1: | 标准类别 | 标准编号 | 标准名称 |  (3列)
      格式2: | 标准类别 | 标准名称 |  (2列, 名称含编号)
      格式3: | 文档 | 描述 |  (2列, RFC格式)
    返回: [{"category": "...", "number": "...", "name": "..."}, ...]
    """
    text = sections.get("遵循标准", "")
    if not text:
        return []
    # 已知标准类别词
    CATEGORY_WORDS = {"3GPP", "RFC", "IETF", "ITU-T", "IEEE", "ISO"}
    standards = []
    # 表格类型状态: "category_name"(格式2) | "doc_desc"(格式3) | "three_col"(格式1) | None
    table_type = None

    for line in text.split("\n"):
        parts = [p.strip() for p in line.strip().split("|")]
        parts = [p for p in parts if p and p != "---"]
        # 清理粗体markdown: **text** -> text
        parts = [re.sub(r"^\*\*(.+?)\*\*$", r"\1", p) for p in parts]

        # 检测表头行, 确定表格类型
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
            # 其他表头行
            continue

        if not parts:
            continue

        if table_type == "three_col" and len(parts) >= 3:
            standards.append({
                "category": parts[0],
                "number": parts[1],
                "name": parts[2],
            })
        elif table_type == "category_name" and len(parts) >= 2:
            # | 3GPP | 3GPP TS 23.401 ... |
            category = parts[0]
            full_name = parts[1]
            # 从名称中提取编号(如 "3GPP TS 23.401 ..." → "TS 23.401")
            num_match = re.match(
                r"(?:3GPP\s+)?(TS\s+\d+\.\d+|TS\s+\d+)"
                r"|(?:ITU-T\s+)?(Recommendation\s+\S+)"
                r"|(RFC\s+\d+)",
                full_name
            )
            number = ""
            if num_match:
                number = num_match.group(1) or num_match.group(2) or num_match.group(3) or ""
            standards.append({
                "category": category,
                "number": number.strip(),
                "name": full_name,
            })
        elif table_type == "doc_desc" and len(parts) >= 2:
            # | RFC 827 | 描述 |  或  | 827 | 描述 |
            raw_num = parts[0].strip()
            if raw_num.upper().startswith("RFC"):
                category = "RFC"
                number = raw_num
            else:
                category = "RFC"
                number = f"RFC {raw_num}"
            standards.append({
                "category": category,
                "number": number,
                "name": parts[1],
            })
        elif not table_type and len(parts) >= 3:
            # 无表头但3列数据
            if parts[0] not in CATEGORY_WORDS or (
                parts[1] and parts[1][0].isdigit()
            ):
                standards.append({
                    "category": parts[0],
                    "number": parts[1],
                    "name": parts[2],
                })
    return standards


def extract_first_release(sections):
    """从 '发布历史' section 提取首次发布版本

    格式: | 特性版本 | 发布版本 | 发布说明 |
    """
    text = sections.get("发布历史", "")
    if not text:
        return ""
    for line in text.split("\n"):
        if "首次发布" in line:
            parts = [p.strip() for p in line.split("|")]
            parts = [p for p in parts if p]
            if len(parts) >= 2:
                version = parts[1]
                # 清理HTML标签
                version = re.sub(r"<[^>]+>", "", version).strip()
                # 清理前缀(如"UDG ")和后缀(如"及后续版本")
                version = re.sub(r"^(UDG|UNC)\s*", "", version)
                version = re.sub(r"\s*及后续版本.*$", "", version)
                return version.strip()
    return ""


def lookup_feature_by_name(raw_name, features_dict):
    """
    P1-1.2: 当相关特性列无特性ID时，用功能名模糊匹配features_dict。

    逻辑:
      1. 去掉链接标记 [xxx](yyy)，取链接文本
      2. 特殊值 NA、-、无 直接跳过
      3. 在 features_dict 中按 feature_name 做子串匹配
      4. 匹配到唯一结果则返回 feature_id，多个或零个则返回空
    """
    name = raw_name.strip()
    # 去链接标记
    link_m = re.match(r"\[([^\]]+)\]", name)
    if link_m:
        name = link_m.group(1)
    name = name.strip()
    # 跳过占位符
    if name in ("NA", "-", "无", "—", "N/A", "不涉及", "无。"):
        return ""
    # 子串匹配
    matches = []
    for fid, feat in features_dict.items():
        feat_name = feat.get("feature_name", "")
        if not feat_name:
            continue
        if name in feat_name or feat_name in name:
            matches.append(fid)
    return matches[0] if len(matches) == 1 else ""


def extract_feature_dependencies(feature_id, sections, features_dict=None):
    """
    从 '与其他特性的交互' section 解析依赖关系

    支持格式:
      格式A (4列): | 交互类型 | 相关特性 | 控制项名称 | 交互说明 |
      格式B (3列): | 交互类型 | 相关特性 | 交互关系 |
      格式C (2列): | 相关特性 | 交互关系 |
    返回: list[dict]
    """
    text = sections.get("与其他特性的交互", "")
    if not text or "不涉及" in text:
        return []

    # 先检测表格列格式
    table_col_count = 0
    for line in text.split("\n"):
        parts = [p.strip() for p in line.strip().split("|")]
        parts = [p for p in parts if p and p != "---"]
        if not parts:
            continue
        cleaned = [p.strip("*").strip() for p in parts]
        # 检测表头行确定列格式
        if "相关特性" in cleaned or "交互类型" in cleaned:
            table_col_count = len(parts)
            break

    deps = []
    for line in text.split("\n"):
        parts = [p.strip() for p in line.strip().split("|")]
        parts = [p for p in parts if p and p != "---"]
        if len(parts) < 2:
            continue
        # P0-1.1: 去粗体后判断表头变体（如 **交互类型**）
        header0 = parts[0].strip("*").strip()
        header1 = parts[1].strip("*").strip() if len(parts) > 1 else ""
        if header0 in ("交互类型", "交互") or header1 in ("相关特性", "和其他特性的交互关系"):
            continue

        # 根据列数适配字段
        if len(parts) >= 4:
            # 格式A: | 交互类型 | 相关特性 | 控制项名称 | 交互说明 |
            dep_type_raw = parts[0]
            related_feature_raw = parts[1]
            control_item = parts[2] if len(parts) > 2 else ""
            description = parts[3] if len(parts) > 3 else ""
        elif len(parts) == 3:
            # 格式B: | 交互类型 | 相关特性 | 交互关系 |
            dep_type_raw = parts[0]
            related_feature_raw = parts[1]
            description = parts[2] if len(parts) > 2 else ""
            control_item = ""
        elif len(parts) == 2:
            # 格式C: | 相关特性 | 交互关系 |
            dep_type_raw = "交互"
            related_feature_raw = parts[0]
            description = parts[1] if len(parts) > 1 else ""
            control_item = ""
        else:
            continue

        # P0-1.4: 清理HTML残留（控制项和说明列都可能含<br>）
        control_item = re.sub(r"<br\s*/?>", "; ", control_item)
        control_item = re.sub(r"<[^>]+>", "", control_item).strip()

        # 从"相关特性"列提取feature_id
        # P1-1.4: 优先使用markdown链接URL中的特性ID (链接文本可能有笔误)
        # 例: [GWFD-020808 用户面地址自动检测](../GWFD-010108 ..._xxx.md)
        # 链接文本GWFD-020808是笔误, URL路径中的GWFD-010108才是正确目标
        url_fid_match = re.search(
            r"\([^)]*?((?:GWFD|WSFD|IPFD|NPFD|SFFD)-\d{3,6})[^)]*\)",
            related_feature_raw
        )
        if url_fid_match:
            target_fid = url_fid_match.group(1)
        else:
            fid_match = FEATURE_ID_SEARCH_RE.search(related_feature_raw)
            target_fid = fid_match.group(1) if fid_match else ""

        # P1-1.2: 特性ID正则匹配失败时，用功能名模糊匹配
        if not target_fid and features_dict:
            target_fid = lookup_feature_by_name(related_feature_raw, features_dict)

        # 标准化 dep_type (文档中可能出现多种中文表述)
        dep_type = dep_type_raw
        if dep_type in ("依赖", "必须先开启"):
            dep_type = "depends_on"
        elif dep_type in ("互斥", "冲突"):
            dep_type = "conflicts_with"
        elif dep_type in ("影响", "与其他特性的影响", "与其他特性间的影响", "其他可能的影响"):
            dep_type = "affects"
        elif dep_type in ("被影响", "其他"):
            dep_type = "other"
        elif "协同" in dep_type:
            dep_type = "cooperates_with"
        elif dep_type in ("支持",):
            dep_type = "supports"
        elif "交互" in dep_type or "关系" in dep_type:
            dep_type = "interacts_with"
        # else: keep original (rare edge cases)

        # P0-1.4: 清理description中的HTML残留
        description = re.sub(r"<br\s*/?>", " ", description)
        description = re.sub(r"<[^>]+>", "", description)
        description = description.strip()

        # 跳过自引用和未映射的脏dep_type
        if target_fid == feature_id:
            continue
        # 如果dep_type仍然是中文长句（未命中任何映射规则），跳过
        if len(dep_type) > 10 and dep_type == dep_type_raw:
            continue

        if target_fid:
            deps.append({
                "id": f"{feature_id}:dep:{target_fid}",
                "source_feature_id": feature_id,
                "target_feature_id": target_fid,
                "dependency_type": dep_type,
                "description": description,
                "license_control_item": control_item,
                "source_type": "overview_explicit",
            })

    return deps


# P2: 特殊格式License硬编码表
# 这些特性使用通用解析器无法支持的格式（如转置表格），数据从原始md人工提取
# 数据来源：直接阅读产品文档的"可获得性"section并验证
# 如果未来出现更多类似格式，应改用专用解析器
_HARDCODED_LICENSES = {
    # WSFD-106201 小区广播服务: 转置表格 | Label | Value |
    # 原始md (特性概述_68358218.md line 54-57):
    #   | License功能项 | 82209076 LKV2PWSR01 PWS故障快速恢复 |
    #   | --- | --- |
    #   | License功能项 | 82207709 LKV2CBS02 小区广播服务 |
    #   | License资源项 | - 82200FMS LKV2CBSIFMM01 CBS广播服务接口及功能-4G
    #                    - 82200FMY LKV2CBSIFAM01 CBS广播服务接口及功能-5G |
    "WSFD-106201": [
        {"feature_id": "WSFD-106201", "license_number": "82209076",
         "license_code": "LKV2PWSR01", "license_name": "PWS故障快速恢复",
         "applicable_nf": "", "id": "WSFD-106201:license:82209076"},
        {"feature_id": "WSFD-106201", "license_number": "82207709",
         "license_code": "LKV2CBS02", "license_name": "小区广播服务",
         "applicable_nf": "", "id": "WSFD-106201:license:82207709"},
        {"feature_id": "WSFD-106201", "license_number": "82200FMS",
         "license_code": "LKV2CBSIFMM01", "license_name": "CBS广播服务接口及功能-4G",
         "applicable_nf": "MME", "id": "WSFD-106201:license:82200FMS"},
        {"feature_id": "WSFD-106201", "license_number": "82200FMY",
         "license_code": "LKV2CBSIFAM01", "license_name": "CBS广播服务接口及功能-5G",
         "applicable_nf": "AMF", "id": "WSFD-106201:license:82200FMY"},
    ],
}


def extract_licenses(feature_id, sections):
    """
    从 '可获得性' section 解析License信息

    支持的格式:
      1. 单行文本: "...对应的License控制项为 '82209822 LKV3G5BCBC01 内容计费基本功能'"
      2. License表格 (多列变体):
         | 适用NF | License控制项 |                            (GWFD)
         | 涉及NF | License控制项 |                            (UNC WSFD-010112)
         | 特性 | License控制项 |                              (UNC WSFD-010303/WSFD-103000)
         | 特性 | 适用NF | License控制项 |                     (UNC WSFD-104401 等15个特性)
      3. 纯文本段落(无引号): "82200EDD LKV2SALANSM01 5G LAN业务基本功能-USM"
      4. "无需获得License"
    """
    # P2: 少数特性使用特殊的转置格式 (Label列 + Value列)，无法用通用解析器处理
    # 直接返回预先验证过的 License 数据
    if feature_id in _HARDCODED_LICENSES:
        return _HARDCODED_LICENSES[feature_id]

    text = sections.get("可获得性", "")
    if not text:
        return []

    licenses = []

    # 先检查是否无License
    if "无需" in text and "License" in text:
        return []

    # 格式2: License表格 (多种列格式)
    # 已知表头变体:
    #   | 适用NF | License控制项 |                       (原格式2, GWFD常见)
    #   | 涉及NF | License控制项 |                       (UNC变体, WSFD-010112)
    #   | 特性 | License控制项 |                         (UNC变体, WSFD-010303/WSFD-103000)
    #   | 特性 | 适用NF | License控制项 |                (UNC 3列, WSFD-104401等15个特性)
    # 通用规则: 找含"License"的列作为License列; 找含"NF"或"适用"的列作为NF列(可选)
    in_table = False
    lic_col = -1
    nf_col = -1
    for line in text.split("\n"):
        parts = [p.strip() for p in line.strip().split("|")]
        parts = [p for p in parts if p and p != "---"]

        if not in_table:
            # 表头识别: 任一列含"License"作为表头(非数据值)
            # 通用规则: 只要某列名以"License"开头或包含"License控制项"/"License项"/"License支持"
            # 即认为是License列; NF列可选(没有则applicable_nf留空)
            lic_header_col = -1
            for i, p in enumerate(parts):
                p_clean = p.strip("*").strip()
                # 排除"License"在数据值中的情况(如"License许可后才能...")
                # 只匹配表头格式: "License控制项", "License项", "License支持", "License"
                if p_clean.startswith("License") and len(p_clean) <= 20:
                    lic_header_col = i
                    break
            if lic_header_col >= 0 and len(parts) >= 2:
                lic_col = lic_header_col
                nf_col = -1
                for i, p in enumerate(parts):
                    if i == lic_col:
                        continue
                    p_clean = p.strip("*").strip()
                    if "NF" in p_clean or "适用" in p_clean:
                        nf_col = i
                in_table = True
                continue
        else:
            # 表格数据行
            # 空行/分隔符行 (parts为空): 保持表格状态, 跳过
            if not parts:
                continue
            if len(parts) <= lic_col:
                # 列数不匹配, 表格结束
                in_table = False
                lic_col = -1
                nf_col = -1
                continue

            license_text = parts[lic_col].rstrip(" |").strip()
            license_text = re.sub(r"<br\s*/?>", " ", license_text)
            if not license_text:
                continue

            # 从License列提取: "编号 编码 名称"
            lm = re.match(r"([A-Za-z0-9]{6,12})\s+([A-Za-z0-9_\-]+)\s+(.+)", license_text)
            if lm:
                nf_part = ""
                if nf_col >= 0 and len(parts) > nf_col:
                    nf_part = parts[nf_col].rstrip(" |").strip()
                    nf_part = re.sub(r"<br\s*/?>", "、", nf_part)
                licenses.append({
                    "feature_id": feature_id,
                    "license_number": lm.group(1),
                    "license_code": lm.group(2),
                    "license_name": lm.group(3).strip().rstrip(" |"),
                    "applicable_nf": nf_part,
                })
            else:
                # 不符合License格式, 表格可能结束
                in_table = False
                lic_col = -1
                nf_col = -1

    if not licenses:
        # 格式1: 单行License控制项(引号包裹)
        # 匹配模式: "编号 编码 名称"  (引号中)
        single_license = re.search(
            r'["\u201c\u201d\'\u2018\u2019]+([A-Za-z0-9]{6,12})\s+([A-Za-z0-9_\-]+)\s+(.+?)["\u201c\u201d\'\u2018\u2019]',
            text, re.MULTILINE
        )
        if single_license:
            licenses.append({
                "feature_id": feature_id,
                "license_number": single_license.group(1),
                "license_code": single_license.group(2),
                "license_name": single_license.group(3).strip().rstrip("。"),
                "applicable_nf": "",
            })

    if not licenses:
        # 格式3: 纯文本段落中的License(无引号, 在"License支持"后出现)
        # 典型文本: "对应的License控制项为 "82200EDD LKV2SALANSM01 5G LAN业务基本功能-USM"。"
        # 或: "对应的License控制项为 82200EDD LKV2SALANSM01 5G LAN业务基本功能-USM。"
        for line in text.split("\n"):
            line = line.strip()
            # 跳过表格行和空行
            if line.startswith("|") or not line:
                continue
            # 在"License支持"或"控制项"附近的行中搜索
            lm = re.search(
                r'([A-Za-z0-9]{6,12})\s+([A-Za-z0-9_\-]+)\s+(.+?)(?:\s*[。.]|$)',
                line
            )
            if lm:
                name = lm.group(3).strip().rstrip("。").rstrip("|").strip()
                if name and len(name) > 2:  # 过滤掉误匹配
                    licenses.append({
                        "feature_id": feature_id,
                        "license_number": lm.group(1),
                        "license_code": lm.group(2),
                        "license_name": name,
                        "applicable_nf": "",
                    })

    # P0-2.2: 清理license_name脏数据 & 补充id字段
    clean_licenses = []
    for lic in licenses:
        name = lic.get("license_name", "").strip().rstrip("|").rstrip('"').rstrip("'").strip()
        if not name or len(name) < 2 or name in ("License控制项", "License支持"):
            continue
        lic["license_name"] = name
        lic["id"] = f"{feature_id}:license:{lic['license_number']}"
        clean_licenses.append(lic)
    licenses = clean_licenses

    return licenses


# =====================================================================
# 4. 主流程
# =====================================================================

# NF列名(来自xlsx)
NF_COLUMNS = ["GGSN(2G&3G)", "S/PGW-U(4G)", "S/PGW-U(5G NSA)", "UPF(5G)", "NB-IoT"]


def build_nf_support_map(feat):
    """从xlsx NF列构建 nf_support_map"""
    nf_map = {}
    for col in NF_COLUMNS:
        val = feat.get(col, "").strip()
        if val:
            nf_map[col] = val
    # 序列化为 k=v;k=v 格式
    return "; ".join(f"{k}={v}" for k, v in nf_map.items())


def build_base_row(product, fid, feat):
    """构建Feature基础字段(来自xlsx/step1)"""
    return {
        "id": f"{product}:{fid}",
        "feature_id": fid,
        "feature_name": feat.get("feature_name", ""),
        "product_type": product,
        "product_version": feat.get("product_version", ""),
        "is_directory": feat.get("is_directory", "false"),
        "section": feat.get("section", ""),
        "parent_feature_id": feat.get("parent_feature_id", ""),
        "nf_support_map": build_nf_support_map(feat),
    }


def process_product(product):
    """处理一个产品的全部特性"""
    features = load_features(product)
    file_mappings = load_file_mappings(product)

    feature_rows = []
    dependency_rows = []
    license_rows = []
    doc_asset_rows = []
    stats = {
        "total": len(features),
        "with_docs": 0,
        "overview_found": 0,
        "overview_empty": 0,
        "no_overview": 0,
        "no_docs": 0,
    }

    for fid, feat in sorted(features.items()):
        fps = file_mappings.get(fid, [])

        if not fps:
            # 无文档的特性
            row = build_base_row(product, fid, feat)
            row.update({
                "applicable_nf": "",
                "feature_type": "",
                "definition": "",
                "application_scenario": "",
                "system_impact": "",
                "restrictions": "",
                "spec": "",
                "standards": "",
                "first_release_version": "",
                "config_required": "",
                "customer_value": "",
                "has_overview": "no_docs",
            })
            feature_rows.append(row)
            stats["no_docs"] += 1
            continue

        stats["with_docs"] += 1

        # 找概述md
        overview_path, doc_assets = find_overview_md(fid, fps)

        if not overview_path:
            # 有文档但无概述
            row = build_base_row(product, fid, feat)
            row.update({
                "applicable_nf": "",
                "feature_type": "",
                "definition": "",
                "application_scenario": "",
                "system_impact": "",
                "restrictions": "",
                "spec": "",
                "standards": "",
                "first_release_version": "",
                "config_required": "",
                "customer_value": "",
                "has_overview": "no_overview",
            })
            feature_rows.append(row)
            stats["no_overview"] += 1

            # 仍然记录doc_assets
            for fp, dt in doc_assets:
                doc_asset_rows.append({
                    "id": f"{fid}:doc:{make_id(fid, fp)}",
                    "feature_id": fid,
                    "product_type": product,
                    "file_path": fp,
                    "doc_type": dt,
                    "doc_title": read_doc_title(fp),
                })
            continue

        # 读概述内容
        abs_overview = resolve_path(overview_path)
        if not abs_overview.exists():
            stats["overview_found"] += 1
            row = build_base_row(product, fid, feat)
            row["has_overview"] = "file_missing"
            feature_rows.append(row)
            continue

        with open(abs_overview, encoding="utf-8") as f:
            content = f.read()

        # 空文件检查
        if len(content.strip()) < 50:
            stats["overview_empty"] += 1
            row = build_base_row(product, fid, feat)
            row["has_overview"] = "empty"
            feature_rows.append(row)
            for fp, dt in doc_assets:
                doc_asset_rows.append({
                    "id": f"{fid}:doc:{make_id(fid, fp)}",
                    "feature_id": fid,
                    "product_type": product,
                    "file_path": fp,
                    "doc_type": dt,
                    "doc_title": read_doc_title(fp),
                })
            continue

        stats["overview_found"] += 1

        # 解析sections
        sections = parse_overview_sections(content)

        # 提取各字段
        applicable_nf = extract_applicable_nf(sections)
        definition = extract_definition(sections)
        standards_list = extract_standards(sections)
        first_release = extract_first_release(sections)
        deps = extract_feature_dependencies(fid, sections, features)
        licenses = extract_licenses(fid, sections)

        # 推断feature_type
        feature_type = infer_feature_type(fid, doc_assets, sections)

        row = build_base_row(product, fid, feat)
        row.update({
            "applicable_nf": "、".join(applicable_nf),
            "feature_type": feature_type,
            "definition": definition,
            "application_scenario": extract_application_scenario(sections),
            "system_impact": extract_system_impact(sections),
            "restrictions": extract_restrictions(sections),
            "spec": extract_spec(sections),
            "standards": "; ".join(
                s['number'] if s['number'].upper().startswith(s['category'].upper())
                else f"{s['category']} {s['number']}"
                for s in standards_list
            ),
            "first_release_version": first_release,
            "config_required": "true" if feature_type != "protocol_base" else "false",
            "customer_value": extract_customer_value(sections),
            "has_overview": "yes",
        })
        feature_rows.append(row)

        # 依赖关系
        dependency_rows.extend(deps)

        # License
        license_rows.extend(licenses)

        # DocAssets
        for fp, dt in doc_assets:
            doc_asset_rows.append({
                "id": f"{fid}:doc:{make_id(fid, fp)}",
                "feature_id": fid,
                "product_type": product,
                "file_path": fp,
                "doc_type": dt,
                "doc_title": read_doc_title(fp),
            })

    # 去重: 同一(source, target, type)只保留第一条
    seen_dep = set()
    unique_deps = []
    for d in dependency_rows:
        key = (d["source_feature_id"], d["target_feature_id"], d["dependency_type"])
        if key not in seen_dep:
            seen_dep.add(key)
            unique_deps.append(d)
    dependency_rows = unique_deps

    # P1-1.5: 为 conflicts_with 边计算 conflict_pair_id
    # 互斥语义上是对称的，A→B 和 B→A 共享同一个 pair_id，便于：
    #   - 前端展示时按 pair_id 去重（一条边只展示一次）
    #   - 审查时合并两个方向的证据
    # CSV 仍保留双向两条记录（证据完整可追溯），仅通过 pair_id 关联。
    for d in dependency_rows:
        if d["dependency_type"] == "conflicts_with":
            pair = sorted([d["source_feature_id"], d["target_feature_id"]])
            d["conflict_pair_id"] = f"conflict:{pair[0]}-{pair[1]}"
        else:
            d["conflict_pair_id"] = ""

    return feature_rows, dependency_rows, license_rows, doc_asset_rows, stats


def infer_feature_type(feature_id, doc_assets, sections):
    """推断feature_type

    protocol_base: 无需配置(如会话管理、NSA组网)
    config_enable: 有明确配置步骤
    business_policy: 复杂策略配置
    """
    # 检查是否有activation文档
    has_activation = any(dt == "activation" for _, dt in doc_assets)
    # 检查"可获得性"中是否说"无需配置"
    availability = sections.get("可获得性", "")
    no_config_needed = "无需配置" in availability

    if no_config_needed and not has_activation:
        return "protocol_base"
    elif has_activation:
        # 进一步区分config_enable和business_policy
        # 策略型通常有多个activation文档或含"策略"/"规则"等关键词
        activation_count = sum(1 for _, dt in doc_assets if dt == "activation")
        definition = sections.get("定义", "")
        policy_keywords = ["策略", "规则", "过滤", "计费", "QoS", "带宽", "流量控制", "访问控制", "策略控制"]
        is_policy = any(kw in definition for kw in policy_keywords)

        if activation_count >= 2 and is_policy:
            return "business_policy"
        else:
            return "config_enable"
    else:
        return "config_enable"


# =====================================================================
# 5. 输出
# =====================================================================
def write_csv(filename, rows, fieldnames):
    path = DATA_DIR / filename
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"  -> {filename}: {len(rows)} rows")


def write_report(all_stats, total_features, total_deps, total_licenses,
                 total_docs, no_overview_list):
    lines = [
        "# L1 抽取报告",
        "",
        "## 概要统计",
        "",
        f"| 指标 | UDG | UNC | 合计 |",
        f"|------|-----|-----|------|",
        f"| 特性总数 | {all_stats['UDG']['total']} | {all_stats['UNC']['total']} | {all_stats['UDG']['total'] + all_stats['UNC']['total']} |",
        f"| 有文档 | {all_stats['UDG']['with_docs']} | {all_stats['UNC']['with_docs']} | {all_stats['UDG']['with_docs'] + all_stats['UNC']['with_docs']} |",
        f"| 概述已抽取 | {all_stats['UDG']['overview_found']} | {all_stats['UNC']['overview_found']} | {all_stats['UDG']['overview_found'] + all_stats['UNC']['overview_found']} |",
        f"| 概述为空 | {all_stats['UDG']['overview_empty']} | {all_stats['UNC']['overview_empty']} | {all_stats['UDG']['overview_empty'] + all_stats['UNC']['overview_empty']} |",
        f"| 有文档但无概述 | {all_stats['UDG']['no_overview']} | {all_stats['UNC']['no_overview']} | {all_stats['UDG']['no_overview'] + all_stats['UNC']['no_overview']} |",
        f"| 无文档 | {all_stats['UDG']['no_docs']} | {all_stats['UNC']['no_docs']} | {all_stats['UDG']['no_docs'] + all_stats['UNC']['no_docs']} |",
        "",
        f"- 特性依赖关系: {total_deps} 条",
        f"- License映射: {total_licenses} 条",
        f"- DocAsset分类: {total_docs} 条",
        "",
    ]

    if no_overview_list:
        lines.append("## 未找到概述的特性")
        lines.append("")
        for fid, pt in no_overview_list:
            lines.append(f"- {pt}: {fid}")
        lines.append("")

    path = DATA_DIR / "l1_extraction_report.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  -> l1_extraction_report.md")


def main():
    print("=" * 60)
    print("Step 4: L1 抽取 — 从概述md提取Feature结构化属性")
    print("=" * 60)

    feature_fields = [
        "id", "feature_id", "feature_name", "product_type",
        "product_version", "is_directory", "section", "parent_feature_id",
        "nf_support_map",
        "applicable_nf", "feature_type", "definition",
        "application_scenario", "system_impact", "restrictions",
        "spec", "standards", "first_release_version",
        "config_required", "customer_value", "has_overview",
    ]
    dep_fields = [
        "id", "source_feature_id", "target_feature_id",
        "dependency_type", "description", "license_control_item", "source_type",
        "conflict_pair_id",
    ]
    license_fields = [
        "id", "feature_id", "license_number", "license_code",
        "license_name", "applicable_nf",
    ]
    doc_fields = ["id", "feature_id", "product_type", "file_path", "doc_type", "doc_title"]

    all_stats = {}
    no_overview_list = []

    for product in ["UDG", "UNC"]:
        print(f"\n--- Processing {product} ---")
        features, deps, licenses, docs, stats = process_product(product)
        all_stats[product] = stats
        print(f"  Total: {stats['total']}, Overview: {stats['overview_found']}, "
              f"Empty: {stats['overview_empty']}, No overview: {stats['no_overview']}, "
              f"No docs: {stats['no_docs']}")

        for row in features:
            if row.get("has_overview") in ("no_overview", "empty"):
                no_overview_list.append((row["feature_id"], product))

        # 按产品拆分输出
        prefix = f"l1_{product.lower()}"
        write_csv(f"{prefix}_feature_attributes.csv", features, feature_fields)
        write_csv(f"{prefix}_feature_dependency.csv", deps, dep_fields)
        write_csv(f"{prefix}_feature_license.csv", licenses, license_fields)
        write_csv(f"{prefix}_doc_assets.csv", docs, doc_fields)

    # 输出报告
    print("\n--- Writing report ---")
    total_deps = sum(
        len(list(csv.DictReader(open(DATA_DIR / f"l1_{p.lower()}_feature_dependency.csv", encoding="utf-8-sig"))))
        for p in ["UDG", "UNC"]
    )
    total_licenses = sum(
        len(list(csv.DictReader(open(DATA_DIR / f"l1_{p.lower()}_feature_license.csv", encoding="utf-8-sig"))))
        for p in ["UDG", "UNC"]
    )
    total_docs = sum(
        len(list(csv.DictReader(open(DATA_DIR / f"l1_{p.lower()}_doc_assets.csv", encoding="utf-8-sig"))))
        for p in ["UDG", "UNC"]
    )
    total_features = sum(s["total"] for s in all_stats.values())
    write_report(
        all_stats,
        total_features,
        total_deps,
        total_licenses,
        total_docs,
        no_overview_list,
    )

    print("\nDone.")


if __name__ == "__main__":
    main()
