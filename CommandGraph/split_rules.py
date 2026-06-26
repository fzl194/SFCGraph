"""把 7 表合一的内网规则.csv 拆成独立表 csv（开发验证用）。

读 CommandGraph/old/data/内网规则.csv，按 "X、表名" 标记行分段，
输出每张表（表头+数据）到 CommandGraph/data/rules/{表名}.csv。
"""
import csv
from pathlib import Path

SRC = Path("CommandGraph/old/data/内网规则.csv")
OUT_DIR = Path("CommandGraph/data/rules")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# 表编号 → 输出文件名
TABLE_MAP = {
    "1": "参数表",
    "2": "MOD规则",
    "3": "参数关系",
    "4": "重复规则",
    "5": "RMV规则",
    "6": "SET规则",
    "7": "SP规则",
}


def table_num(row):
    """行是否是表标记行（首字段 '数字、xxx'），返回编号或 None。"""
    if not row:
        return None
    cell = (row[0] or "").strip()
    for num in TABLE_MAP:
        if cell.startswith(num + "、"):
            return num
    return None


def trim_trailing_empties(row):
    """裁掉行尾部的空字段，保留有效数据。"""
    last = len(row)
    while last > 1 and (row[last - 1] or "").strip() == "":
        last -= 1
    return row[:last]


with SRC.open(encoding="utf-8-sig") as f:
    rows = list(csv.reader(f))

tables: dict[str, list[list[str]]] = {}
current = None
for row in rows:
    num = table_num(row)
    if num:
        current = num
        tables.setdefault(current, [])
        continue
    if current is None:
        continue
    # 跳过全空行
    if all((c or "").strip() == "" for c in row):
        continue
    tables[current].append(row)

print(f"源: {SRC}")
print(f"输出目录: {OUT_DIR}")
print("-" * 50)
for num, data_rows in tables.items():
    name = TABLE_MAP[num]
    out = OUT_DIR / f"{name}.csv"
    with out.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        for r in data_rows:
            w.writerow(trim_trailing_empties(r))
    # 表头预览
    header = data_rows[0] if data_rows else []
    header_preview = ",".join(c for c in header if c)[:60]
    print(f"{name}.csv: {len(data_rows)} 行 | 表头: {header_preview}")
