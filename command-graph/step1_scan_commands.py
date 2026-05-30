"""
Step 1: 扫描 UDG MML 命令目录 → 命令清单 CSV

扫描 output/UDG.../OM参考/命令/UDG MML命令/ 下所有 md 文件，
从目录路径层级和文件名中提取分类信息和命令名。
"""
import csv
import re
import os
from pathlib import Path
from collections import Counter

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# UDG MML 命令文档根目录
COMMAND_ROOT = BASE_DIR.parent / "output" / "UDG_Product_Documentation_CH_20.15.2" / "OM参考" / "命令" / "UDG MML命令"

# 输出文件
OUTPUT_CSV = DATA_DIR / "udg_command_inventory.csv"

# 文件名解析正则：提取中文标题、命令名、文档ID
# 格式1：中文标题（MML命令名）_文档ID.md  （全角括号）
# 格式2：中文标题(MML命令名)_文档ID.md    （半角括号）
# 格式3：中文标题_文档ID.md（无命令名）
FILE_PATTERN = re.compile(
    r"^(?P<title>.+?)"
    r"(?:[（(](?P<command>[^）)]+)[）)])?"
    r"_(?P<doc_id>\d+)\.md$"
)

# 命令名解析：动词 + 空格 + 对象名
COMMAND_VERB_PATTERN = re.compile(
    r"^(ADD|MOD|RMV|DEL|DSP|LST|SET|CLR|STR|STP|ACT|DEA|SYN|RST|RTR|SWP|BKP|LCK|ULK|CFG|GET|PUT|POST|EXE|RUN)\s+(.+)$",
    re.IGNORECASE,
)

# 输出 CSV 字段
FIELDS = [
    "file_path",           # md 文件完整路径
    "file_name",           # 文件名（含后缀）
    "ne_type",             # 网元类型：UDG
    "service_category",    # 一级分类（如：用户面服务管理）
    "service_domain",      # 二级分类（如：会话管理）
    "config_object_area",  # 三级分类（如：GTP隧道管理）
    "specific_operation",  # 四级（如果有）
    "classification_path", # 完整分类路径（JSON array）
    "command_title_zh",    # 中文标题
    "command_name",        # MML 命令名（如 DSP NGLANMACEXINFO）
    "operation_verb",      # 操作动词（如 DSP）
    "command_object_name", # 命令对象名（如 NGLANMACEXINFO）
    "doc_id",              # 文档ID
    "is_special_file",     # 是否特殊文件（非命令md）
    "dir_depth",           # 目录深度（相对COMMAND_ROOT）
]


def parse_file_name(file_name: str) -> dict:
    """从文件名提取中文标题、命令名、文档ID。"""
    m = FILE_PATTERN.match(file_name)
    if not m:
        return {
            "command_title_zh": file_name.replace(".md", ""),
            "command_name": "",
            "doc_id": "",
        }

    title = m.group("title").strip()
    command = m.group("command") or ""
    doc_id = m.group("doc_id") or ""

    # 解析命令名
    verb = ""
    obj_name = ""
    if command:
        cm = COMMAND_VERB_PATTERN.match(command.strip())
        if cm:
            verb = cm.group(1).upper()
            obj_name = cm.group(2).strip()
        else:
            # 非标准动词格式，整串作为 command_name
            obj_name = command.strip()

    return {
        "command_title_zh": title,
        "command_name": command.strip(),
        "operation_verb": verb,
        "command_object_name": obj_name,
        "doc_id": doc_id,
    }


def get_classification(rel_path: Path) -> dict:
    """从相对路径提取分类层级。"""
    parts = list(rel_path.parts)
    # parts[-1] 是文件名，parts[:-1] 是目录路径
    dir_parts = parts[:-1] if len(parts) > 1 else []

    result = {
        "service_category": "",
        "service_domain": "",
        "config_object_area": "",
        "specific_operation": "",
        "classification_path": "",
        "dir_depth": len(dir_parts),
    }

    if len(dir_parts) >= 1:
        result["service_category"] = dir_parts[0]
    if len(dir_parts) >= 2:
        result["service_domain"] = dir_parts[1]
    if len(dir_parts) >= 3:
        result["config_object_area"] = dir_parts[2]
    if len(dir_parts) >= 4:
        result["specific_operation"] = " / ".join(dir_parts[3:])

    result["classification_path"] = " / ".join(dir_parts) if dir_parts else ""
    return result


def scan_commands():
    """扫描所有 md 文件，构建命令清单。"""
    records = []
    stats = Counter()
    special_files = []

    if not COMMAND_ROOT.exists():
        print(f"ERROR: 命令根目录不存在: {COMMAND_ROOT}")
        return

    # 遍历所有 md 文件
    all_md_files = sorted(COMMAND_ROOT.rglob("*.md"))
    stats["total_files"] = len(all_md_files)
    print(f"扫描目录: {COMMAND_ROOT}")
    print(f"找到 {stats['total_files']} 个 md 文件")

    for md_file in all_md_files:
        rel_path = md_file.relative_to(COMMAND_ROOT)
        file_name = md_file.name

        # 跳过根目录的特殊文件
        is_special = rel_path.parent == Path(".") and not FILE_PATTERN.match(file_name)

        parsed_name = parse_file_name(file_name)
        classification = get_classification(rel_path)

        record = {
            "file_path": str(md_file),
            "file_name": file_name,
            "ne_type": "UDG",
            **classification,
            **parsed_name,
            "is_special_file": "yes" if is_special else "no",
        }
        records.append(record)

        if is_special:
            special_files.append(file_name)
            stats["special_files"] += 1
        else:
            stats["command_files"] += 1
            if parsed_name["command_name"]:
                stats["with_command_name"] += 1
            else:
                stats["without_command_name"] += 1

    # 写入 CSV
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(records)

    # 统计报告
    print(f"\n===== Step 1 扫描结果 =====")
    print(f"总文件数: {stats['total_files']}")
    print(f"命令文件: {stats['command_files']}")
    print(f"特殊文件: {stats['special_files']} ({special_files})")
    print(f"有命令名: {stats['with_command_name']}")
    print(f"无命令名: {stats['without_command_name']}")

    # 分类统计
    cat_counter = Counter()
    verb_counter = Counter()
    for r in records:
        if r["is_special_file"] == "no":
            cat_counter[r["service_category"]] += 1
            if r["operation_verb"]:
                verb_counter[r["operation_verb"]] += 1

    print(f"\n--- 一级分类统计 ---")
    for cat, count in cat_counter.most_common():
        print(f"  {cat}: {count}")

    print(f"\n--- 操作动词统计 ---")
    for verb, count in verb_counter.most_common():
        print(f"  {verb}: {count}")

    # 保存审计报告
    audit_dir = DATA_DIR / "audit"
    audit_dir.mkdir(exist_ok=True)
    audit_path = audit_dir / "step1_audit_v1.md"
    with open(audit_path, "w", encoding="utf-8") as f:
        f.write("# Step 1 审计报告 v1\n\n")
        f.write(f"## 统计\n\n")
        f.write(f"- 总文件数: {stats['total_files']}\n")
        f.write(f"- 命令文件: {stats['command_files']}\n")
        f.write(f"- 特殊文件: {stats['special_files']} ({', '.join(special_files)})\n")
        f.write(f"- 有命令名: {stats['with_command_name']}\n")
        f.write(f"- 无命令名: {stats['without_command_name']}\n\n")
        f.write(f"## 一级分类\n\n")
        for cat, count in cat_counter.most_common():
            f.write(f"- {cat}: {count}\n")
        f.write(f"\n## 操作动词\n\n")
        for verb, count in verb_counter.most_common():
            f.write(f"- {verb}: {count}\n")

    print(f"\n审计报告: {audit_path}")
    print(f"输出文件: {OUTPUT_CSV}")
    return records


if __name__ == "__main__":
    scan_commands()
