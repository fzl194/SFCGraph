"""步骤 paramref：内网参数引用规则 → parameter_references.jsonl + object_refers_to.jsonl。

run(ctx) -> int(references 边数)。

ctx 字段：
  nf, version            网元/版本
  out_dir                产物目录绝对路径
  param_reference_csv    参数引用规则 csv/xlsx 绝对路径（按网元版本配置；None 则跳过产空）
"""
from pathlib import Path
from types import SimpleNamespace

from ..core import param_reference as core


def run(ctx: SimpleNamespace) -> int:
    out_dir = Path(ctx.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    refs_path = out_dir / "parameter_references.jsonl"
    obj_refs_path = out_dir / "object_refers_to.jsonl"

    path = getattr(ctx, "param_reference_csv", None)
    if not path or not Path(path).exists():
        print(f"[paramref:{ctx.nf}/{ctx.version}] 无 param_reference_csv，跳过（产空文件）")
        core.write_jsonl(refs_path, [])
        core.write_jsonl(obj_refs_path, [])
        return 0

    result = core.build_param_references(path, ctx.version)
    core.write_jsonl(refs_path, result["parameter_references"])
    core.write_jsonl(obj_refs_path, result["object_refers_to"])
    print(f"[paramref:{ctx.nf}/{ctx.version}] references: {len(result['parameter_references'])} "
          f"| refers_to: {len(result['object_refers_to'])} -> {refs_path}")
    return len(result["parameter_references"])
