"""临时分析工具 v2：基于命令族行为模式（verb 画像）+ 命名，对 object_keyword 做数据驱动的 kind 归类。
输出到 UTF-8 文件供阅读（避免 bash GBK 乱码）。
"""
import json
from collections import defaultdict, Counter
from pathlib import Path

ASSETS = Path("CommandGraph/data/assets")
FILES = [
    ASSETS / "UDG/20.15.2/mml_commands.jsonl",
    ASSETS / "UNC/20.15.2/mml_commands.jsonl",
]

CRUD_VERBS = {"ADD", "MOD", "RMV", "DEL"}
QUERY_VERBS = {"LST", "DSP"}
# 动作/操作类 verb（从 B6 杂项里归纳）
ACTION_VERBS = {
    "SWP", "RST", "CLR", "STP", "LOD", "SYN", "RTR", "EXP", "IMP", "ACT",
    "BKP", "CHK", "COL", "RBL", "FTR", "OPR", "STR", "CLB", "TST", "SND",
    "RUN", "CVT", "DLT", "GEN", "SRT", "PWR", "LCK", "CMD",
}

groups = defaultdict(lambda: {"verbs": Counter(), "zh": set(), "max_records": None, "cnt": 0, "nf": ""})

for f in FILES:
    nf = f.parts[-3]
    with open(f, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            ok = (r.get("object_keyword") or "").strip()
            if not ok:
                continue
            key = f"{nf}:{ok}"
            g = groups[key]
            g["nf"] = nf
            g["verbs"][r.get("verb", "")] += 1
            if r.get("command_name_zh"):
                g["zh"].add(r["command_name_zh"])
            mr = r.get("max_records")
            if mr:
                g["max_records"] = mr
            g["cnt"] += 1


def classify(key, g):
    vs = set(g["verbs"].keys())
    kupper = key.upper()
    has_crud = bool(vs & CRUD_VERBS)
    has_set = "SET" in vs
    qry_only = vs <= QUERY_VERBS and vs  # 非空且全是查询
    non_query = vs - QUERY_VERBS
    act_only = bool(non_query) and non_query <= ACTION_VERBS

    if "BIND" in kupper:                       # 用户认可：绑定
        return "binding"
    if kupper.endswith("ALL"):                 # 批量清理
        return "batch_op"
    if qry_only:                               # 仅查询
        return "query_target"
    if act_only and not has_crud and not has_set:  # 仅动作
        return "action"
    if has_set and not has_crud:               # SET±LST，无增删改 → 全局设置/开关
        return "global_setting"
    if has_crud:                               # 有增删改 → 实体
        return "entity"
    return "other"


result = defaultdict(list)
for key, g in sorted(groups.items()):
    kind = classify(key, g)
    result[kind].append((key, g))

ORDER = ["entity", "global_setting", "binding", "query_target", "action", "batch_op", "other"]
out = []
out.append("=" * 90)
out.append(f"对象族总数（nf:object_keyword）：{len(groups)}   UDG:{sum(1 for g in groups.values() if g['nf']=='UDG')}  UNC:{sum(1 for g in groups.values() if g['nf']=='UNC')}")
out.append("")
out.append("【按行为模式归类的 kind 分布】")
out.append(f"{'kind':<16}{'数量':>7}{'占比':>8}")
total = len(groups)
for k in ORDER:
    n = len(result[k])
    out.append(f"{k:<16}{n:>7}{n*100/total:>7.1f}%")
out.append("")
out.append("=" * 90)

# entity 内部细分（看 CRUD 完整度）
out.append("【entity 桶内部：CRUD 完整度分布】")
crud_profile = Counter()
for key, g in result["entity"]:
    vs = set(g["verbs"].keys())
    crud = vs & CRUD_VERBS
    has_full = {"ADD", "MOD", "RMV"} <= vs
    if has_full:
        crud_profile["ADD+MOD+RMV(完整CRUD)"] += 1
    elif "ADD" in vs and "RMV" in vs:
        crud_profile["ADD+RMV(无MOD)"] += 1
    elif "ADD" in vs and "MOD" in vs:
        crud_profile["ADD+MOD(无RMV)"] += 1
    elif "ADD" in vs:
        crud_profile["仅ADD"] += 1
    elif "MOD" in vs:
        crud_profile["仅MOD"] += 1
    else:
        crud_profile["其他crud组合:" + "/".join(sorted(crud))] += 1
for k, v in crud_profile.most_common():
    out.append(f"  {k:<28} {v}")
out.append("")

out.append("=" * 90)
out.append("【各桶样本：keyword | 中文名 | verbs | 命令数 | max_records】")
for k in ORDER:
    items = result[k]
    out.append(f"\n--- {k} ({len(items)}) ---")
    for key, g in items[:18]:
        zh = next(iter(g["zh"]), "")[:22]
        verbs = "/".join(sorted(g["verbs"].keys()))[:26]
        out.append(f"  {key:<34} {zh:<22} {verbs:<26} n={g['cnt']:<3} mr={g['max_records']}")

# binding 专项（用户认可，全部列出）
out.append("")
out.append("=" * 90)
out.append(f"【binding 全量清单（命名含 BIND）：{len(result['binding'])} 个】")
for key, g in sorted(result["binding"].items()) if False else result["binding"]:
    zh = next(iter(g["zh"]), "")[:24]
    verbs = "/".join(sorted(g["verbs"].keys()))
    out.append(f"  {key:<40} {zh:<24} {verbs}")

Path("CommandGraph/data/object_kind_analysis.txt").write_text("\n".join(out), encoding="utf-8")
print(f"written {len(out)} lines -> CommandGraph/data/object_kind_analysis.txt")
print(f"total groups: {len(groups)}")
for k in ORDER:
    print(f"  {k}: {len(result[k])}")
