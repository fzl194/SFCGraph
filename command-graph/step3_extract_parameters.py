"""
Step 3: 参数解析 → 参数表 + 枚举值表

从 step2 产出的 param_table_raw 中解析参数表格，
提取每个参数的标识、名称、必选/可选、含义、数据来源、取值范围、默认值、配置原则。
"""
import csv
import re
import json
import hashlib
from pathlib import Path
from collections import Counter

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

INPUT_CSV = DATA_DIR / "udg_command_metadata.csv"
OUTPUT_PARAMS = DATA_DIR / "udg_parameters.csv"
OUTPUT_ENUMS = DATA_DIR / "udg_param_enum_values.csv"

# ── 参数说明子字段锚点 ─────────────────────
# 按顺序排列，用于分割连续文本
FIELD_ANCHORS = [
    "可选必选说明",
    "参数含义",
    "数据来源",
    "取值范围",
    "默认值",
    "配置原则",
]

# 枚举值提取：- "VALUE（label）"：description 或 - VALUE（label）：description
ENUM_PATTERN = re.compile(
    r"[-*]\s*[\"" "]?"
    r"(\w[\w.]*)"                          # VALUE
    r"(?:[\"" "])?"
    r"(?:（([^）]+)）)?\s*"                # （label）
    r"[：:]\s*(.+?)(?=\n[-*]|\n$|$)",     # : description
    re.MULTILINE,
)

# 条件依赖提取：当"PARAM"配置为"VALUE"时 / 在"PARAM"配置为"VALUE"时
COND_DEP_PATTERN = re.compile(
    r'(?:当|在)[""\u201c](\w+)[""\u201d]配置为[""\u201c]([^""\u201c\u201d]+)[""\u201d]时',
)

# Markdown 表格行解析
TABLE_ROW_RE = re.compile(r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|$")
TABLE_SEP_RE = re.compile(r"^\|[-\s]+\|[-\s]+\|[-\s]+\|$")

FIELDS_PARAMS = [
    "param_id",
    "command_name",
    "operation_verb",
    "param_identifier",
    "param_name_zh",
    "required_type",
    "condition_raw",
    "meaning",
    "data_source",
    "value_range_raw",
    "value_type",
    "default_value_raw",
    "config_principle_raw",
    "has_enum_values",
    "enum_count",
    "condition_deps_raw",
    "raw_description",
]

FIELDS_ENUMS = [
    "param_id",
    "command_name",
    "param_identifier",
    "enum_value",
    "enum_label",
    "enum_description",
]


def make_id(*parts):
    raw = ":".join(str(p) for p in parts)
    return hashlib.md5(raw.encode()).hexdigest()[:10]


def classify_value_type(value_range: str) -> str:
    """判断参数值类型。"""
    if not value_range:
        return "unknown"
    vr = value_range.strip()
    # NA / 不涉及（含全角冒号后缀）
    vr_stripped = vr.rstrip("：: ")
    if vr_stripped in ("NA", "N/A", "－", "—", "-", "无", "不涉及", "不适用"):
        return "not_applicable"
    # 布尔
    if vr in ("ON/OFF", "ENABLE/DISABLE", "YES/NO", "TRUE/FALSE", "是/否", "开/关"):
        return "boolean"
    if "TRUE" in vr and "FALSE" in vr and ("或" in vr or "/" in vr):
        return "boolean"
    # 枚举型: 以 - 开头，包含中文括号，或包含"枚举"关键字
    if vr.startswith("-") or "（" in vr or "枚举" in vr:
        return "enum"
    # 数值范围: 支持全角波浪号～、半角~、短横线- 以及中文"至"
    if re.search(r"\d+\s*[~～\-—]\s*\d+", vr):
        return "integer_range"
    # 十六进制范围
    if re.search(r"0x[0-9a-fA-F]+\s*[~～\-—]\s*0x[0-9a-fA-F]+", vr):
        return "integer_range"
    # 字符串类型
    if "字符串" in vr or "输入长度" in vr:
        return "string"
    # IP/MAC
    if "IP" in vr or "IPv4" in vr or "IPv6" in vr:
        return "ip_address"
    if "MAC" in vr:
        return "mac_address"
    return "other"


def extract_enum_values(value_range: str) -> list[dict]:
    """从取值范围中提取枚举值。"""
    if not value_range or "- " not in value_range:
        return []

    results = []
    # 按行分割，找以 - 或 * 开头的枚举项
    lines = value_range.split("\n")
    for line in lines:
        line = line.strip()
        if not line.startswith("-") and not line.startswith("*"):
            continue
        line = line.lstrip("-* ").strip()
        if not line:
            continue

        # 格式: VALUE（label）：description 或 VALUE: description
        m = re.match(
            r'["" "]?(\w[\w.]*?)["" "]?'
            r'(?:（([^）]+)）)?'
            r'\s*[：:]\s*(.+)',
            line,
        )
        if m:
            results.append({
                "enum_value": m.group(1).strip(),
                "enum_label": m.group(2) or "",
                "enum_description": m.group(3).strip() if m.group(3) else "",
            })
        else:
            # 可能是简单格式: VALUE（label）
            m2 = re.match(r'["" "]?(\w[\w.]*?)["" "]?(?:（([^）]+)）)?', line)
            if m2:
                results.append({
                    "enum_value": m2.group(1).strip(),
                    "enum_label": m2.group(2) or "",
                    "enum_description": "",
                })
    return results


def extract_condition_deps(description: str) -> list[dict]:
    """提取条件依赖关系。"""
    deps = []
    for m in COND_DEP_PATTERN.finditer(description):
        deps.append({
            "param": m.group(1),
            "value": m.group(2),
        })
    return deps


def parse_param_description(raw: str) -> dict:
    """解析参数说明单元格，用锚点分割提取各子字段。"""
    # 清理 <br> 标签为换行
    text = raw.replace("<br>", "\n").replace("<br/>", "\n").replace("<br />", "\n")

    result = {
        "required_type": "",
        "condition_raw": "",
        "meaning": "",
        "data_source": "",
        "value_range_raw": "",
        "default_value_raw": "",
        "config_principle_raw": "",
    }

    # 找到所有锚点位置
    positions = []
    for anchor in FIELD_ANCHORS:
        # 匹配锚点 + 可能的冒号
        for m in re.finditer(re.escape(anchor) + r"[：:]", text):
            positions.append((m.start(), m.end(), anchor))

    # 按位置排序
    positions.sort(key=lambda x: x[0])

    # 按锚点提取内容
    for i, (start, end, anchor) in enumerate(positions):
        # 内容从锚点后到下一个锚点前
        next_start = positions[i + 1][0] if i + 1 < len(positions) else len(text)
        content = text[end:next_start].strip()

        if anchor == "可选必选说明":
            result["required_type"] = content
            # 尝试从 required_type 中提取前提条件
            cond_m = re.search(r"前提条件[：:]\s*(.+?)(?:参数含义|$)", content)
            if cond_m:
                result["condition_raw"] = cond_m.group(1).strip()
        elif anchor == "参数含义":
            result["meaning"] = content
        elif anchor == "数据来源":
            result["data_source"] = content
        elif anchor == "取值范围":
            result["value_range_raw"] = content
        elif anchor == "默认值":
            result["default_value_raw"] = content
        elif anchor == "配置原则":
            result["config_principle_raw"] = content

    # 如果锚点分割没找到 required_type，尝试简单匹配
    if not result["required_type"]:
        if "必选参数" in text and "可选参数" not in text:
            result["required_type"] = "必选参数"
        elif "可选参数" in text and "必选参数" not in text:
            result["required_type"] = "可选参数"
        elif "条件必选" in text:
            result["required_type"] = "条件必选参数"
        elif "条件可选" in text:
            result["required_type"] = "条件可选参数"

    # 标准化 required_type：只保留4种类型
    rt = result["required_type"]
    if rt:
        if "条件必选" in rt or ("必选" in rt and "条件" in rt):
            result["required_type"] = "条件必选参数"
        elif "条件可选" in rt or ("可选" in rt and "条件" in rt):
            result["required_type"] = "条件可选参数"
        elif "必选" in rt:
            result["required_type"] = "必选参数"
        elif "可选" in rt:
            result["required_type"] = "可选参数"

    return result


def parse_param_table(param_table_raw: str, command_name: str, verb: str) -> tuple[list[dict], list[dict]]:
    """解析参数说明 markdown 表格。"""
    params = []
    enums = []

    if not param_table_raw or "|" not in param_table_raw:
        return params, enums

    lines = param_table_raw.strip().split("\n")
    for line in lines:
        # 跳过分隔行
        if TABLE_SEP_RE.match(line):
            continue
        m = TABLE_ROW_RE.match(line)
        if not m:
            continue

        param_id_text = m.group(1).strip()
        param_name = m.group(2).strip()
        param_desc = m.group(3).strip()

        # 跳过表头（含 markdown 粗体标记）
        cleaned_id = param_id_text.strip("*").strip()
        if cleaned_id in ("参数标识", "参数ID", "参数说明") or "---" in param_id_text:
            continue

        # 解析子字段
        subfields = parse_param_description(param_desc)

        # 提取条件依赖
        cond_deps = extract_condition_deps(param_desc)

        # 分类值类型
        value_type = classify_value_type(subfields["value_range_raw"])

        # 提取枚举值
        enum_values = extract_enum_values(subfields["value_range_raw"])

        pid = make_id("UDG", command_name, param_id_text)

        param_record = {
            "param_id": pid,
            "command_name": command_name,
            "operation_verb": verb,
            "param_identifier": param_id_text,
            "param_name_zh": param_name,
            "required_type": subfields["required_type"],
            "condition_raw": subfields["condition_raw"][:300],
            "meaning": subfields["meaning"][:500],
            "data_source": subfields["data_source"],
            "value_range_raw": subfields["value_range_raw"][:1000],
            "value_type": value_type,
            "default_value_raw": subfields["default_value_raw"][:200],
            "config_principle_raw": subfields["config_principle_raw"][:500],
            "has_enum_values": "yes" if enum_values else "no",
            "enum_count": len(enum_values),
            "condition_deps_raw": json.dumps(cond_deps, ensure_ascii=False) if cond_deps else "",
            "raw_description": param_desc[:2000],
        }
        params.append(param_record)

        # 枚举值记录
        for ev in enum_values:
            enums.append({
                "param_id": pid,
                "command_name": command_name,
                "param_identifier": param_id_text,
                **ev,
            })

    return params, enums


def main():
    with open(INPUT_CSV, encoding="utf-8-sig") as f:
        metadata = list(csv.DictReader(f))

    print(f"读取 {len(metadata)} 条命令元数据")

    all_params = []
    all_enums = []
    stats = Counter()
    param_commands = 0

    for i, row in enumerate(metadata):
        if row["has_param_table"] != "yes":
            continue
        param_commands += 1

        cmd_name = row["command_name"]
        verb = row["operation_verb"]
        param_raw = row["param_table_raw"]

        params, enums = parse_param_table(param_raw, cmd_name, verb)
        all_params.extend(params)
        all_enums.extend(enums)
        stats["commands_with_params"] += 1
        stats["total_params"] += len(params)

        if (i + 1) % 500 == 0:
            print(f"  进度: {i+1}/{len(metadata)}, 累计参数: {stats['total_params']}")

    # 写入 CSV
    with open(OUTPUT_PARAMS, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS_PARAMS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(all_params)

    with open(OUTPUT_ENUMS, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS_ENUMS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(all_enums)

    # 统计
    print(f"\n===== Step 3 参数解析结果 =====")
    print(f"有参数表的命令: {stats['commands_with_params']}")
    print(f"总参数数: {stats['total_params']}")
    print(f"总枚举值数: {len(all_enums)}")

    # 值类型分布
    type_counter = Counter(r["value_type"] for r in all_params)
    print(f"\n--- 值类型分布 ---")
    for t, c in type_counter.most_common():
        print(f"  {t}: {c} ({c*100/len(all_params):.1f}%)")

    # 必选/可选分布
    req_counter = Counter(r["required_type"] for r in all_params)
    print(f"\n--- 必选/可选分布 ---")
    for t, c in req_counter.most_common():
        print(f"  {t or '(空)'}: {c}")

    # 枚举参数统计
    enum_params = [r for r in all_params if r["has_enum_values"] == "yes"]
    print(f"\n--- 枚举参数 ---")
    print(f"  有枚举值的参数: {len(enum_params)}")
    print(f"  总枚举值: {len(all_enums)}")

    # 条件依赖
    cond_params = [r for r in all_params if r["condition_deps_raw"]]
    print(f"  有条件依赖的参数: {len(cond_params)}")

    # 子字段提取率
    meaning_filled = sum(1 for r in all_params if r["meaning"])
    vr_filled = sum(1 for r in all_params if r["value_range_raw"])
    dv_filled = sum(1 for r in all_params if r["default_value_raw"])
    cp_filled = sum(1 for r in all_params if r["config_principle_raw"])
    total = len(all_params)
    print(f"\n--- 子字段提取率 ---")
    print(f"  参数含义: {meaning_filled} ({meaning_filled*100/total:.1f}%)")
    print(f"  取值范围: {vr_filled} ({vr_filled*100/total:.1f}%)")
    print(f"  默认值: {dv_filled} ({dv_filled*100/total:.1f}%)")
    print(f"  配置原则: {cp_filled} ({cp_filled*100/total:.1f}%)")

    # 审计报告
    audit_dir = DATA_DIR / "audit"
    audit_dir.mkdir(exist_ok=True)
    with open(audit_dir / "step3_audit_v1.md", "w", encoding="utf-8") as f:
        f.write("# Step 3 审计报告 v1\n\n")
        f.write(f"## 统计\n\n")
        f.write(f"- 有参数表的命令: {stats['commands_with_params']}\n")
        f.write(f"- 总参数数: {total}\n")
        f.write(f"- 总枚举值数: {len(all_enums)}\n")
        f.write(f"- 有条件依赖的参数: {len(cond_params)}\n\n")
        f.write(f"## 子字段提取率\n\n")
        f.write(f"- 参数含义: {meaning_filled} ({meaning_filled*100/total:.1f}%)\n")
        f.write(f"- 取值范围: {vr_filled} ({vr_filled*100/total:.1f}%)\n")
        f.write(f"- 默认值: {dv_filled} ({dv_filled*100/total:.1f}%)\n")
        f.write(f"- 配置原则: {cp_filled} ({cp_filled*100/total:.1f}%)\n\n")
        f.write(f"## 值类型分布\n\n")
        for t, c in type_counter.most_common():
            f.write(f"- {t}: {c} ({c*100/total:.1f}%)\n")
        f.write(f"\n## 必选/可选分布\n\n")
        for t, c in req_counter.most_common():
            f.write(f"- {t or '(空)'}: {c}\n")

    print(f"\n审计报告: {audit_dir / 'step3_audit_v1.md'}")
    print(f"输出: {OUTPUT_PARAMS}, {OUTPUT_ENUMS}")


if __name__ == "__main__":
    main()
