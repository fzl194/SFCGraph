"""步骤 configobject：mml_commands + command_parameters + 内网规则表
→ config_objects.jsonl + command_object_edges.jsonl。

run(ctx) -> int(ConfigObject 条数)。

ctx 字段（SimpleNamespace）：
  nf, version          网元/版本
  out_dir              产物目录绝对路径（= assets_root/nf/version）
  mod_rules_csv        MOD规则.csv 绝对路径（可选，None 则 identifier 仅靠 RMV）
  rmv_rules_csv        RMV规则.csv 绝对路径（可选）
  uniqueness_rules_csv 重复规则.csv 绝对路径（可选）

读取同目录 mml_commands.jsonl + command_parameters.jsonl（由前置 step 产出）。
"""
from pathlib import Path
from types import SimpleNamespace

from ..core import config_object as core


def run(ctx: SimpleNamespace) -> int:
    out_dir = Path(ctx.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    objects_path = out_dir / "config_objects.jsonl"
    edges_path = out_dir / "command_object_edges.jsonl"

    mml_commands = core.load_jsonl(str(out_dir / "mml_commands.jsonl"))
    command_parameters = core.load_jsonl(str(out_dir / "command_parameters.jsonl"))

    mod_rules = core.load_mod_rules(getattr(ctx, "mod_rules_csv", None))
    rmv_rules = core.load_rmv_rules(getattr(ctx, "rmv_rules_csv", None))
    uniq_rules = core.load_uniqueness_rules(getattr(ctx, "uniqueness_rules_csv", None))

    result = core.build_config_objects(
        ctx.nf, ctx.version, mml_commands, command_parameters,
        mod_rules, rmv_rules, uniq_rules,
    )
    core.write_jsonl(objects_path, result["objects"])
    core.write_jsonl(edges_path, result["edges"])

    # 简单分布统计
    kind_counts = {}
    for o in result["objects"]:
        kind_counts[o["object_kind"]] = kind_counts.get(o["object_kind"], 0) + 1
    has_id = sum(1 for o in result["objects"] if o["identifier_parameters"])
    has_uniq = sum(1 for o in result["objects"] if o["uniqueness_keys"])

    print(f"[configobject:{ctx.nf}/{ctx.version}] "
          f"commands: {len(mml_commands)} | objects: {len(result['objects'])} "
          f"| edges: {len(result['edges'])}")
    print(f"  kind 分布: {kind_counts}")
    print(f"  有 identifier: {has_id} | 有 uniqueness: {has_uniq} -> {objects_path}")
    return len(result["objects"])
