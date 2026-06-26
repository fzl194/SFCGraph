"""小范围验证 ConfigObject builder：读已有 UDG jsonl + 拆好的规则表，
跑聚合，抽样看结果（不重扫 md，快）。
"""
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path("CommandGraph").resolve()))
from builder.core import config_object as core  # noqa: E402

NF, VER = "UDG", "20.15.2"
OUT = Path(f"CommandGraph/data/assets/{NF}/{VER}")
RULES = Path("CommandGraph/data/rules")

mml = core.load_jsonl(str(OUT / "mml_commands.jsonl"))
params = core.load_jsonl(str(OUT / "command_parameters.jsonl"))
mod = core.load_mod_rules(str(RULES / "MOD规则.csv"))
rmv = core.load_rmv_rules(str(RULES / "RMV规则.csv"))
uniq = core.load_uniqueness_rules(str(RULES / "重复规则.csv"))

result = core.build_config_objects(NF, VER, mml, params, mod, rmv, uniq)
objs = result["objects"]

print(f"mml_commands: {len(mml)} | params: {len(params)}")
print(f"MOD规则对象: {len(mod)} | RMV规则对象: {len(rmv)} | 重复规则对象: {len(uniq)}")
print(f"ConfigObject: {len(objs)} | edges: {len(result['edges'])}")
print(f"kind 分布: {dict(Counter(o['object_kind'] for o in objs))}")
print(f"有 identifier: {sum(1 for o in objs if o['identifier_parameters'])}")
print(f"有 uniqueness: {sum(1 for o in objs if o['uniqueness_keys'])}")
print(f"有 attribute: {sum(1 for o in objs if o['attribute_names'])}")

print("\n=== 抽样对象 ===")
for name in ["ACL", "ABSTIMERANGE", "URR", "REFRESHSRV", "RULEBINDING",
             "NATSESSION", "ABNTRAFFICDT", "BGPALL"]:
    o = next((o for o in objs if o["object_name"] == name), None)
    if not o:
        print(f"{name}: <不存在>")
        continue
    print(f"{name:16} kind={o['object_kind']:14} id={o['identifier_parameters']} "
          f"uniq={o['uniqueness_keys']} attrs={len(o['attribute_names'])} "
          f"zh={o['object_name_zh'][:18]}")

# identifier/uniqueness 命中校验：MOD规则里有的对象，是否都抽到 identifier
print("\n=== identifier 命中校验（MOD规则对象）===")
miss = [obj for obj in mod if not next((o for o in objs if o["object_name"] == obj and o["identifier_parameters"]), None)]
print(f"MOD规则 {len(mod)} 对象，抽到 identifier 的: {len(mod) - len(miss)}, 缺失: {miss}")
