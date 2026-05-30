"""
Step 4: 配置对象发现

从命令名、目录路径、参数交集三个维度归纳配置对象，
并发现命令组（同对象的 CRUD 命令族）。
"""
import csv
import json
import re
import hashlib
from pathlib import Path
from collections import Counter, defaultdict

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

INPUT_COMMANDS = DATA_DIR / "udg_command_metadata.csv"
INPUT_PARAMS = DATA_DIR / "udg_parameters.csv"

OUTPUT_OBJECTS = DATA_DIR / "udg_config_objects.csv"
OUTPUT_GROUPS = DATA_DIR / "udg_command_groups.csv"

# 命令名解析：VERB + OBJECT_NAME
COMMAND_NAME_RE = re.compile(
    r"^(ADD|MOD|RMV|DEL|DSP|LST|SET|CLR|STR|STP|ACT|DEA|SYN|RST|RTR|SWP|BKP|LCK|ULK|CFG|GET|PUT|POST|EXE|RUN)\s+(\S+)$",
    re.IGNORECASE,
)

# CRUD 角色
CRUD_MAP = {
    "ADD": "create",
    "MOD": "update",
    "SET": "update",
    "RMV": "delete",
    "DEL": "delete",
    "DSP": "read",
    "LST": "read",
    "CLR": "delete",
    "RST": "update",
    "RTR": "read",
    "ACT": "update",
    "DEA": "update",
    "STR": "update",
    "STP": "update",
    "SYN": "update",
    "LCK": "update",
    "ULK": "update",
    "SWP": "update",
    "CFG": "update",
}

FIELDS_OBJECTS = [
    "object_id",
    "object_name",
    "object_name_zh",
    "ne_type",
    "service_category",
    "service_domain",
    "config_object_area",
    "command_count",
    "create_commands",
    "read_commands",
    "update_commands",
    "delete_commands",
    "other_commands",
    "parameter_count",
    "top_parameters",
    "has_full_crud",
    "classification_path",
]

FIELDS_GROUPS = [
    "group_id",
    "object_name",
    "command_name",
    "operation_verb",
    "crud_role",
    "command_title_zh",
    "service_category",
    "service_domain",
    "config_object_area",
]


def make_id(*parts):
    raw = ":".join(str(p) for p in parts)
    return hashlib.md5(raw.encode()).hexdigest()[:10]


def discover_objects():
    # 读取命令元数据
    with open(INPUT_COMMANDS, encoding="utf-8-sig") as f:
        commands = list(csv.DictReader(f))
    print(f"读取 {len(commands)} 条命令元数据")

    # 读取参数
    params_by_command = defaultdict(list)
    with open(INPUT_PARAMS, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            params_by_command[row["command_name"]].append(row["param_identifier"])
    print(f"读取 {sum(len(v) for v in params_by_command.values())} 个参数")

    # ── 方法1: 从命令名归纳配置对象 ──────────────
    # 相同 object_name 的命令属于同一配置对象
    obj_groups = defaultdict(list)
    for cmd in commands:
        obj_name = cmd.get("command_object_name", "")
        if not obj_name:
            continue
        obj_groups[obj_name].append(cmd)

    # 构建配置对象表
    objects = []
    groups = []

    for obj_name, cmds in sorted(obj_groups.items()):
        # 取最常见的分类路径
        cat_counter = Counter()
        domain_counter = Counter()
        area_counter = Counter()
        title_zh_counter = Counter()
        for c in cmds:
            cat_counter[c["service_category"]] += 1
            domain_counter[c["service_domain"]] += 1
            area_counter[c["config_object_area"]] += 1
            # 从中文标题中提取对象名
            title_zh_counter[c["command_title_zh"]] += 1

        service_cat = cat_counter.most_common(1)[0][0] if cat_counter else ""
        service_dom = domain_counter.most_common(1)[0][0] if domain_counter else ""
        config_area = area_counter.most_common(1)[0][0] if area_counter else ""

        # 提取对象中文名（从最常见的中文标题中去掉操作动词）
        obj_name_zh = ""
        for title, _ in title_zh_counter.most_common():
            # 去掉"增加/修改/删除/查询/设置/显示/清除/..."前缀
            cleaned = re.sub(
                r"^(增加|修改|删除|查询|设置|显示|清除|启动|停止|激活|去激活|同步|复位|恢复|切换|锁定|解锁|配置|获取|执行|运行)",
                "",
                title,
            )
            if cleaned:
                obj_name_zh = cleaned
                break

        # 收集参数
        all_params = set()
        for c in cmds:
            for p in params_by_command.get(c["command_name"], []):
                all_params.add(p)
        top_params = sorted(all_params)[:10]

        # CRUD 分类
        crud = {"create": [], "read": [], "update": [], "delete": [], "other": []}
        for c in cmds:
            verb = c.get("operation_verb", "").upper()
            role = CRUD_MAP.get(verb, "other")
            crud[role].append(c["command_name"])

        has_full_crud = (
            len(crud["create"]) > 0
            and len(crud["read"]) > 0
            and len(crud["update"]) > 0
            and len(crud["delete"]) > 0
        )

        obj_record = {
            "object_id": make_id("UDG", obj_name),
            "object_name": obj_name,
            "object_name_zh": obj_name_zh,
            "ne_type": "UDG",
            "service_category": service_cat,
            "service_domain": service_dom,
            "config_object_area": config_area,
            "command_count": len(cmds),
            "create_commands": json.dumps(crud["create"], ensure_ascii=False),
            "read_commands": json.dumps(crud["read"], ensure_ascii=False),
            "update_commands": json.dumps(crud["update"], ensure_ascii=False),
            "delete_commands": json.dumps(crud["delete"], ensure_ascii=False),
            "other_commands": json.dumps(crud["other"], ensure_ascii=False),
            "parameter_count": len(all_params),
            "top_parameters": json.dumps(top_params, ensure_ascii=False),
            "has_full_crud": "yes" if has_full_crud else "no",
            "classification_path": f"{service_cat} / {service_dom} / {config_area}" if service_cat else "",
        }
        objects.append(obj_record)

        # 命令组记录
        for c in cmds:
            verb = c.get("operation_verb", "").upper()
            role = CRUD_MAP.get(verb, "other")
            groups.append({
                "group_id": make_id("UDG", obj_name, c["command_name"]),
                "object_name": obj_name,
                "command_name": c["command_name"],
                "operation_verb": verb,
                "crud_role": role,
                "command_title_zh": c.get("command_title_zh", ""),
                "service_category": c.get("service_category", ""),
                "service_domain": c.get("service_domain", ""),
                "config_object_area": c.get("config_object_area", ""),
            })

    # 写入 CSV
    with open(OUTPUT_OBJECTS, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS_OBJECTS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(objects)

    with open(OUTPUT_GROUPS, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS_GROUPS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(groups)

    # 统计
    print(f"\n===== Step 4 配置对象发现结果 =====")
    print(f"配置对象数: {len(objects)}")
    print(f"命令组记录数: {len(groups)}")

    # CRUD 完整性
    full_crud = sum(1 for o in objects if o["has_full_crud"] == "yes")
    print(f"完整CRUD的配置对象: {full_crud}")

    # 按命令数分布
    cmd_count_dist = Counter(o["command_count"] for o in objects)
    print(f"\n--- 配置对象命令数分布 ---")
    for count, num in sorted(cmd_count_dist.items()):
        print(f"  {count}个命令: {num}个配置对象")

    # 按分类分布
    cat_dist = Counter(o["service_category"] for o in objects)
    print(f"\n--- 配置对象分类分布 ---")
    for cat, num in cat_dist.most_common():
        print(f"  {cat}: {num}")

    # 参数最多的配置对象
    top_by_params = sorted(objects, key=lambda o: o["parameter_count"], reverse=True)[:10]
    print(f"\n--- 参数最多的配置对象 (Top 10) ---")
    for o in top_by_params:
        print(f"  {o['object_name']:30s} ({o['object_name_zh'][:15]}): {o['parameter_count']}参数, {o['command_count']}命令, CRUD={o['has_full_crud']}")

    # 审计报告
    audit_dir = DATA_DIR / "audit"
    audit_dir.mkdir(exist_ok=True)
    with open(audit_dir / "step4_audit_v1.md", "w", encoding="utf-8") as f:
        f.write("# Step 4 审计报告 v1\n\n")
        f.write(f"## 统计\n\n")
        f.write(f"- 配置对象数: {len(objects)}\n")
        f.write(f"- 命令组记录数: {len(groups)}\n")
        f.write(f"- 完整CRUD的配置对象: {full_crud}\n\n")
        f.write(f"## 命令数分布\n\n")
        for count, num in sorted(cmd_count_dist.items()):
            f.write(f"- {count}个命令: {num}个配置对象\n")
        f.write(f"\n## Top 10 参数最多的配置对象\n\n")
        for o in top_by_params:
            f.write(f"- **{o['object_name']}** ({o['object_name_zh'][:15]}): {o['parameter_count']}参数, {o['command_count']}命令\n")

    print(f"\n审计报告: {audit_dir / 'step4_audit_v1.md'}")
    print(f"输出: {OUTPUT_OBJECTS}, {OUTPUT_GROUPS}")


if __name__ == "__main__":
    discover_objects()
