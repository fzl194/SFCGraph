"""
Step 2: 解析命令文档结构化内容 → 命令元数据 CSV

读取每个命令 md 文件，按 section 提取：
- 命令名、操作动词、中文标题
- 适用NF
- 命令功能描述
- 注意事项
- 操作权限
- 参数说明（原文）
- 使用实例
- 输出结果说明
"""
import csv
import re
import json
import hashlib
from pathlib import Path
from collections import Counter

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

INPUT_CSV = DATA_DIR / "udg_command_inventory.csv"
OUTPUT_CSV = DATA_DIR / "udg_command_metadata.csv"

# ── Section 锚点正则 ──────────────────────────────
# 匹配 #### [命令功能](...) 或 ## [命令功能](...)
SECTION_RE = re.compile(r"^(#{2,4})\s*\[([^\]]+)\]\(#[^)]*\)", re.MULTILINE)
# 适用NF
NF_RE = re.compile(r"\*\*适用NF[：:]\s*([^*]+)\*\*")
# 命令名
COMMAND_NAME_RE = re.compile(r"^(ADD|MOD|RMV|DEL|DSP|LST|SET|CLR|STR|STP|ACT|DEA|SYN|RST|RTR|SWP|BKP|LCK|ULK|CFG|GET|PUT|POST|EXE|RUN)\s+(\S+)", re.IGNORECASE)

FIELDS = [
    "command_id",
    "command_name",
    "operation_verb",
    "command_object_name",
    "command_title_zh",
    "ne_type",
    "applicable_nf",
    "description",
    "notes",
    "permissions",
    "has_param_table",
    "param_table_raw",
    "has_usage_example",
    "usage_example_raw",
    "has_output_description",
    "output_description_raw",
    "sections_found",
    "section_count",
    # 目录层级（从 inventory 传递）
    "service_category",
    "service_domain",
    "config_object_area",
    "specific_operation",
    "classification_path",
    "file_path",
    "doc_id",
]


def make_id(*parts):
    raw = ":".join(str(p) for p in parts)
    return hashlib.md5(raw.encode()).hexdigest()[:10]


def split_sections(content: str) -> dict[str, str]:
    """将 md 内容按 section 拆分为 {section_name: content} 字典。"""
    matches = list(SECTION_RE.finditer(content))
    sections = {}
    for i, m in enumerate(matches):
        name = m.group(2).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        section_content = content[start:end].strip()
        sections[name] = section_content
    return sections


def extract_nf(text: str) -> str:
    """从文本中提取适用NF。"""
    m = NF_RE.search(text)
    if m:
        return m.group(1).strip().replace("、", ",").replace("，", ",")
    return ""


def parse_command_file(file_path: str, inventory_row: dict) -> dict | None:
    """解析单个命令文档，提取结构化内容。"""
    try:
        content = Path(file_path).read_text(encoding="utf-8")
    except Exception as e:
        print(f"  [WARN] 读取失败: {file_path}: {e}")
        return None

    # 跳过空文件或极小文件
    if len(content.strip()) < 50:
        return None

    # 拆分 sections
    sections = split_sections(content)
    section_names = list(sections.keys())

    # 提取命令功能 section
    func_content = ""
    for key in ["命令功能", "功能"]:
        if key in sections:
            func_content = sections[key]
            break

    # 适用NF（从命令功能 section 提取）
    applicable_nf = extract_nf(func_content)

    # 描述（去掉NF行后的第一段文本）
    description = ""
    if func_content:
        lines = func_content.split("\n")
        desc_lines = []
        for line in lines:
            line = line.strip()
            if line.startswith("**适用NF") or line.startswith("**适用") or line.startswith("适用NF"):
                continue
            if line.startswith(">"):
                # 引用块也算描述
                desc_lines.append(line)
            elif line:
                if desc_lines:
                    break
                desc_lines.append(line)
        description = " ".join(desc_lines).strip()

    # 注意事项
    notes = sections.get("注意事项", sections.get("注意", ""))

    # 操作权限
    permissions = sections.get("操作用户权限", sections.get("用户权限", ""))

    # 参数说明
    param_content = sections.get("参数说明", "")
    has_param_table = "|" in param_content and "---" in param_content

    # 使用实例
    usage_content = sections.get("使用实例", sections.get("使用范例", ""))
    has_usage_example = bool(usage_content.strip())

    # 输出结果说明
    output_content = sections.get("输出结果说明", sections.get("输出说明", ""))
    has_output = bool(output_content.strip())

    # 从 inventory 传递
    cmd_name = inventory_row.get("command_name", "")
    verb = inventory_row.get("operation_verb", "")
    obj_name = inventory_row.get("command_object_name", "")
    title = inventory_row.get("command_title_zh", "")

    # 如果 inventory 没解析出命令名，尝试从内容解析
    if not cmd_name:
        h1_match = re.search(r"^#\s+.+?（(\w+\s+\w+)）", content, re.MULTILINE)
        if not h1_match:
            h1_match = re.search(r"^#\s+.+?\((\w+\s+\w+)\)", content, re.MULTILINE)
        if h1_match:
            cmd_name = h1_match.group(1)
            cm = COMMAND_NAME_RE.match(cmd_name)
            if cm:
                verb = cm.group(1).upper()
                obj_name = cm.group(2)

    return {
        "command_id": make_id("UDG", cmd_name, inventory_row.get("doc_id", "")),
        "command_name": cmd_name,
        "operation_verb": verb,
        "command_object_name": obj_name,
        "command_title_zh": title,
        "ne_type": "UDG",
        "applicable_nf": applicable_nf,
        "description": description[:500] if description else "",
        "notes": notes[:1000] if notes else "",
        "permissions": permissions[:200] if permissions else "",
        "has_param_table": "yes" if has_param_table else "no",
        "param_table_raw": param_content[:5000] if param_content else "",
        "has_usage_example": "yes" if has_usage_example else "no",
        "usage_example_raw": usage_content[:2000] if usage_content else "",
        "has_output_description": "yes" if has_output else "no",
        "output_description_raw": output_content[:3000] if output_content else "",
        "sections_found": json.dumps(section_names, ensure_ascii=False),
        "section_count": len(section_names),
        "service_category": inventory_row.get("service_category", ""),
        "service_domain": inventory_row.get("service_domain", ""),
        "config_object_area": inventory_row.get("config_object_area", ""),
        "specific_operation": inventory_row.get("specific_operation", ""),
        "classification_path": inventory_row.get("classification_path", ""),
        "file_path": file_path,
        "doc_id": inventory_row.get("doc_id", ""),
    }


def main():
    # 读取 inventory
    with open(INPUT_CSV, encoding="utf-8-sig") as f:
        inventory = list(csv.DictReader(f))

    print(f"读取 {len(inventory)} 条命令清单")
    records = []
    stats = Counter()
    errors = []

    for i, row in enumerate(inventory):
        file_path = row["file_path"]
        if not Path(file_path).exists():
            errors.append(f"文件不存在: {file_path}")
            continue

        result = parse_command_file(file_path, row)
        if result:
            records.append(result)
            stats["success"] += 1
        else:
            stats["skipped"] += 1
            errors.append(f"解析为空: {file_path}")

        if (i + 1) % 500 == 0:
            print(f"  进度: {i + 1}/{len(inventory)}")

    # 写入 CSV
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(records)

    # 统计
    print(f"\n===== Step 2 解析结果 =====")
    print(f"成功: {stats['success']}")
    print(f"跳过: {stats['skipped']}")
    print(f"错误: {len(errors)}")

    # 各 section 覆盖率
    section_counter = Counter()
    nf_counter = Counter()
    for r in records:
        sections = json.loads(r["sections_found"])
        for s in sections:
            section_counter[s] += 1
        if r["applicable_nf"]:
            nf_counter["has_nf"] += 1
        else:
            nf_counter["no_nf"] += 1
        if r["has_param_table"] == "yes":
            stats["has_param"] += 1
        if r["has_usage_example"] == "yes":
            stats["has_example"] += 1

    total = len(records)
    print(f"\n--- Section 覆盖率 (total={total}) ---")
    for s, c in section_counter.most_common(15):
        print(f"  {s}: {c} ({c*100/total:.1f}%)")

    print(f"\n--- 关键字段覆盖率 ---")
    print(f"  有参数表: {stats['has_param']} ({stats['has_param']*100/total:.1f}%)")
    print(f"  有使用实例: {stats['has_example']} ({stats['has_example']*100/total:.1f}%)")
    print(f"  有适用NF: {nf_counter['has_nf']} ({nf_counter.get('has_nf',0)*100/total:.1f}%)")

    # 审计报告
    audit_dir = DATA_DIR / "audit"
    audit_dir.mkdir(exist_ok=True)
    with open(audit_dir / "step2_audit_v1.md", "w", encoding="utf-8") as f:
        f.write("# Step 2 审计报告 v1\n\n")
        f.write(f"## 统计\n\n")
        f.write(f"- 成功解析: {stats['success']}\n")
        f.write(f"- 跳过: {stats['skipped']}\n")
        f.write(f"- 有参数表: {stats['has_param']} ({stats['has_param']*100/total:.1f}%)\n")
        f.write(f"- 有使用实例: {stats['has_example']} ({stats['has_example']*100/total:.1f}%)\n")
        f.write(f"- 有适用NF: {nf_counter.get('has_nf',0)} ({nf_counter.get('has_nf',0)*100/total:.1f}%)\n\n")
        f.write(f"## Section 覆盖率\n\n")
        for s, c in section_counter.most_common():
            f.write(f"- {s}: {c} ({c*100/total:.1f}%)\n")
        if errors[:10]:
            f.write(f"\n## 错误样本 (前10)\n\n")
            for e in errors[:10]:
                f.write(f"- {e}\n")

    print(f"\n审计报告: {audit_dir / 'step2_audit_v1.md'}")
    print(f"输出文件: {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
