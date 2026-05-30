"""
Step 7: 最终合并 + Schema 归纳

合并所有步骤的数据产出，生成最终的命令图谱数据集，
并根据实际发现归纳 Schema 文档。
"""
import csv
import json
import shutil
from pathlib import Path
from collections import Counter

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
FINAL_DIR = DATA_DIR / "final"
FINAL_DIR.mkdir(exist_ok=True)

# 输入文件
INPUT_COMMANDS = DATA_DIR / "udg_command_metadata.csv"
INPUT_PARAMS = DATA_DIR / "udg_parameters.csv"
INPUT_ENUMS = DATA_DIR / "udg_param_enum_values.csv"
INPUT_OBJECTS = DATA_DIR / "udg_config_objects.csv"
INPUT_GROUPS = DATA_DIR / "udg_command_groups.csv"
INPUT_RELATIONSHIPS = DATA_DIR / "udg_semantic_relationships_reviewed.json"
# 如果 reviewed 不存在，使用 raw
INPUT_RELATIONSHIPS_RAW = DATA_DIR / "udg_semantic_relationships_raw.json"


def copy_csv(src, dst_name):
    """复制 CSV 到最终目录。"""
    dst = FINAL_DIR / dst_name
    if src.exists():
        shutil.copy2(src, dst)
        with open(src, encoding="utf-8-sig") as f:
            count = sum(1 for _ in csv.DictReader(f))
        print(f"  {dst_name}: {count} records")
        return count
    return 0


def export_relationships_csv():
    """将 JSON 关系转为 CSV。"""
    # 优先使用 reviewed，否则使用 raw
    input_file = INPUT_RELATIONSHIPS if INPUT_RELATIONSHIPS.exists() else INPUT_RELATIONSHIPS_RAW
    if not input_file.exists():
        print("  relationships.csv: 无数据")
        return 0

    with open(input_file, encoding="utf-8") as f:
        rels = json.load(f)

    if not rels:
        print("  relationships.csv: 0 records")
        return 0

    # 收集所有字段
    all_keys = set()
    for r in rels:
        all_keys.update(r.keys())

    fields = sorted(all_keys)
    output = FINAL_DIR / "relationships.csv"

    with open(output, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rels)

    print(f"  relationships.csv: {len(rels)} records")
    return len(rels)


def generate_schema():
    """根据实际发现生成 Schema 文档。"""
    # 统计各表规模
    stats = {}
    for csv_file in FINAL_DIR.glob("*.csv"):
        with open(csv_file, encoding="utf-8-sig") as f:
            stats[csv_file.stem] = sum(1 for _ in csv.DictReader(f))

    # 关系统计
    rel_file = INPUT_RELATIONSHIPS if INPUT_RELATIONSHIPS.exists() else INPUT_RELATIONSHIPS_RAW
    rel_types = Counter()
    rel_total = 0
    if rel_file.exists():
        with open(rel_file, encoding="utf-8") as f:
            rels = json.load(f)
        rel_total = len(rels)
        rel_types = Counter(r.get("type", "unknown") for r in rels)

    # 命令统计
    verb_counter = Counter()
    cat_counter = Counter()
    with open(INPUT_COMMANDS, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            verb_counter[row.get("operation_verb", "")] += 1
            cat_counter[row.get("service_category", "")] += 1

    # 参数统计
    param_type_counter = Counter()
    req_type_counter = Counter()
    with open(INPUT_PARAMS, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            param_type_counter[row.get("value_type", "")] += 1
            req_type_counter[row.get("required_type", "")] += 1

    schema = f"""# Command Graph Schema — UDG 20.15.2

## 1. 概述

命令图谱是三层配置图谱的底层基础层，将 MML 命令体系建模为可生成、可核查的配置对象网络。

**构建范围**: UDG 20.15.2 产品文档
**构建方法**: 代码抽取（命令/参数/配置对象）+ LLM语义抽取（关系）

## 2. 数据规模

| 数据类型 | 记录数 |
|---------|--------|
| 命令 (Command) | {stats.get('commands', 0)} |
| 参数 (Parameter) | {stats.get('parameters', 0)} |
| 枚举值 (EnumValue) | {stats.get('enum_values', 0)} |
| 配置对象 (ConfigObject) | {stats.get('config_objects', 0)} |
| 命令组 (CommandGroup) | {stats.get('command_groups', 0)} |
| 语义关系 (Relationship) | {rel_total} |

## 3. 节点类型

### 3.1 Command（命令）

每个 MML 命令对应一个节点。

| 字段 | 类型 | 说明 |
|------|------|------|
| command_id | string | 唯一标识 (hash) |
| command_name | string | MML命令名 (如 MOD NGM2MPLCY) |
| operation_verb | enum | 操作动词 |
| command_object_name | string | 命令对象名 |
| command_title_zh | string | 中文标题 |
| applicable_nf | string | 适用NF |
| description | text | 命令功能描述 |
| notes | text | 注意事项 |
| permissions | text | 操作权限 |
| service_category | string | 一级分类 |
| service_domain | string | 二级分类 |
| config_object_area | string | 三级分类 |

**操作动词分布**:
"""
    for verb, count in verb_counter.most_common():
        if verb:
            schema += f"- {verb}: {count}\n"

    schema += f"""
### 3.2 Parameter（参数）

命令参数节点。

| 字段 | 类型 | 说明 |
|------|------|------|
| param_id | string | 唯一标识 (hash) |
| command_name | string | 所属命令 |
| param_identifier | string | 参数标识 (如 SUBRANGE) |
| param_name_zh | string | 参数中文名 |
| required_type | enum | 必选参数/可选参数/条件必选参数/条件可选参数 |
| condition_raw | text | 条件说明原文 |
| meaning | text | 参数含义 |
| data_source | string | 数据来源 |
| value_range_raw | text | 取值范围原文 |
| value_type | enum | 值类型 |
| default_value_raw | text | 默认值原文 |
| config_principle_raw | text | 配置原则原文 |
| has_enum_values | boolean | 是否有枚举值 |
| condition_deps_raw | json | 条件依赖关系 |

**值类型分布**:
"""
    for vt, count in param_type_counter.most_common():
        if vt:
            schema += f"- {vt}: {count}\n"

    schema += f"""
**必选/可选分布**:
"""
    for rt, count in req_type_counter.most_common():
        if rt:
            schema += f"- {rt}: {count}\n"

    schema += f"""
### 3.3 ConfigObject（配置对象）

通过命令名归纳的配置对象，同对象名的不同操作构成 CRUD 命令族。

| 字段 | 类型 | 说明 |
|------|------|------|
| object_id | string | 唯一标识 (hash) |
| object_name | string | 配置对象名 (如 FILTER) |
| object_name_zh | string | 中文名 |
| command_count | int | 包含的命令数 |
| has_full_crud | boolean | 是否有完整 CRUD |
| parameter_count | int | 参数总数 |
| create/read/update/delete_commands | json | 各角色命令列表 |

### 3.4 EnumValue（枚举值）

枚举型参数的取值选项。

| 字段 | 类型 | 说明 |
|------|------|------|
| param_id | string | 所属参数 |
| enum_value | string | 枚举值 (如 ENABLE) |
| enum_label | string | 中文标签 |
| enum_description | string | 说明 |

## 4. 关系类型

通过 LLM 语义抽取发现的关系，每条关系包含 evidence_text（原文引用）。

| 关系类型 | 数量 | 说明 |
|---------|------|------|
"""
    for rtype, count in rel_types.most_common():
        schema += f"| {rtype} | {count} | {_describe_rel_type(rtype)} |\n"

    schema += f"""
## 5. 层级结构

命令图谱的分类层级来自产品文档目录结构：

```
UDG MML命令/
├── {chr(10).join(f'├── {cat} ({count})' for cat, count in cat_counter.most_common())}
```

## 6. 构建方法

| 数据 | 方法 | 抽取工具 |
|------|------|---------|
| 命令元数据 | 代码抽取 | step2_parse_commands.py |
| 参数详情 | 代码抽取 | step3_extract_parameters.py |
| 配置对象 | 代码发现 | step4_discover_config_objects.py |
| 语义关系 | LLM抽取+审查 | step5/step6 (DeepSeek) |
"""

    schema_path = BASE_DIR / "COMMAND_GRAPH_SCHEMA.md"
    with open(schema_path, "w", encoding="utf-8") as f:
        f.write(schema)
    print(f"\nSchema 文档: {schema_path}")
    return stats, rel_types


def _describe_rel_type(rtype):
    descriptions = {
        "param_condition": "参数条件依赖",
        "cmd_prerequisite": "命令前置依赖",
        "cmd_reference": "命令引用关系",
        "param_exclusion": "参数互斥",
        "risk_level": "风险等级",
        "effect_timing": "生效时机",
        "config_object_hierarchy": "配置对象层级",
    }
    return descriptions.get(rtype, rtype)


def main():
    print("===== Step 7: 最终合并 + Schema 归纳 =====\n")

    # 复制最终数据
    print("--- 复制最终数据 ---")
    copy_csv(INPUT_COMMANDS, "commands.csv")
    copy_csv(INPUT_PARAMS, "parameters.csv")
    copy_csv(INPUT_ENUMS, "enum_values.csv")
    copy_csv(INPUT_OBJECTS, "config_objects.csv")
    copy_csv(INPUT_GROUPS, "command_groups.csv")
    rel_count = export_relationships_csv()

    # 生成 Schema
    print("\n--- 生成 Schema ---")
    generate_schema()

    # 最终统计报告
    print("\n===== 最终统计 =====")
    total_files = 0
    for csv_file in FINAL_DIR.glob("*.csv"):
        with open(csv_file, encoding="utf-8-sig") as f:
            count = sum(1 for _ in csv.DictReader(f))
        print(f"  {csv_file.name}: {count}")
        total_files += 1
    print(f"\n共 {total_files} 个最终数据文件")
    print(f"最终数据目录: {FINAL_DIR}")

    # 审计报告
    audit_dir = DATA_DIR / "audit"
    audit_dir.mkdir(exist_ok=True)
    with open(audit_dir / "step7_audit_v1.md", "w", encoding="utf-8") as f:
        f.write("# Step 7 审计报告\n\n")
        f.write("## 最终数据\n\n")
        for csv_file in sorted(FINAL_DIR.glob("*.csv")):
            with open(csv_file, encoding="utf-8-sig") as cf:
                count = sum(1 for _ in csv.DictReader(cf))
            f.write(f"- {csv_file.name}: {count}\n")
        f.write(f"\n## Schema\n\n")
        f.write(f"- 已生成: COMMAND_GRAPH_SCHEMA.md\n")

    print(f"审计报告: {audit_dir / 'step7_audit_v1.md'}")


if __name__ == "__main__":
    main()
