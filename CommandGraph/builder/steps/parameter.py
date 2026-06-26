"""步骤 parameter：CSV/XLSX → CommandParameter + has_parameter + depends_on 三件套。

run(ctx) -> int(参数节点条数)。从旧 build_commandparameter.main 移植，
参数从 ctx 取（不再 argparse）。

ctx 额外字段：
  parameter_csv        CSV/XLSX 绝对路径（None 则跳过）
  out_dir              产物目录绝对路径（参数 jsonl 与两个关系 sidecar 都写这里）

命令关联校验：读同目录 mml_commands.jsonl 提 command_id 集合（可选，存在才校验）。
"""
from pathlib import Path
from types import SimpleNamespace

from ..params import build_from_rows, load_command_ids, load_rows, write_jsonl


def run(ctx: SimpleNamespace) -> int:
    if not getattr(ctx, "parameter_csv", None):
        print(f"[parameter:{ctx.nf}/{ctx.version}] 无 parameter_csv，跳过")
        return 0

    out_dir = Path(ctx.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    params_path = out_dir / "command_parameters.jsonl"
    has_path = out_dir / "command_has_parameter.jsonl"
    deps_path = out_dir / "parameter_conditional_required.jsonl"

    mml_path = out_dir / "mml_commands.jsonl"
    command_ids = load_command_ids(mml_path) if mml_path.exists() else None

    rows = load_rows(ctx.parameter_csv)
    result = build_from_rows(rows, source_name=Path(ctx.parameter_csv).name, command_ids=command_ids)

    write_jsonl(params_path, result["parameters"])
    write_jsonl(has_path, result["has_parameter_edges"])
    write_jsonl(deps_path, result["conditional_required_edges"])

    print(f"[parameter:{ctx.nf}/{ctx.version}] rows: {len(rows)} "
          f"| parameters: {len(result['parameters'])} "
          f"| has_parameter: {len(result['has_parameter_edges'])} "
          f"| conditional_required: {len(result['conditional_required_edges'])} "
          f"| skipped_placeholders: {result['skipped_placeholders']} "
          f"| missing_commands: {len(result['missing_commands'])} "
          f"| unresolved_deps: {len(result['unresolved_dependencies'])}")
    if result["missing_commands"]:
        print("  missing command refs (first 20):")
        for item in result["missing_commands"][:20]:
            print(f"    - {item}")
    return len(result["parameters"])
