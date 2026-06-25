"""步骤 mmlcommand：扫源 md → mml_commands.jsonl。

run(ctx) -> int(写出条数)。逻辑从旧 build_mmlcommand.main 移植，
参数从 ctx 取（不再 argparse），去重沿用 command_id 集合。

ctx 字段（SimpleNamespace）：
  nf, version          网元/版本
  source               源 MML 命令 md 目录绝对路径
  project_root         SFCGraph 根绝对路径（md_path 相对它，用于 source_evidence_ids）
  out_dir              产物目录绝对路径（= assets_root/nf/version）
"""
import json
import os
from pathlib import Path
from types import SimpleNamespace

from ..core.identity import to_mmlcommand
from ..core.md_reader import parse_md


def run(ctx: SimpleNamespace) -> int:
    source = Path(ctx.source)
    project_root = Path(ctx.project_root)
    out = Path(ctx.out_dir) / "mml_commands.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)

    md_files = sorted(source.rglob("*.md"))
    seen = set()
    ok = skipped = 0
    with out.open("w", encoding="utf-8") as f:
        for fp in md_files:
            raw = parse_md(str(fp), str(source))
            if not raw:
                skipped += 1
                continue
            # md_path 相对 SFCGraph 根（后端 doc_root=SFCGraph 根能读到原始 md）
            md_path = os.path.relpath(str(fp), str(project_root)).replace("\\", "/")
            obj = to_mmlcommand(raw, ctx.nf, ctx.version, md_path)
            if obj["command_id"] in seen:
                continue
            seen.add(obj["command_id"])
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")
            ok += 1
    print(f"[mmlcommand:{ctx.nf}/{ctx.version}] scan {len(md_files)} md -> "
          f"built {ok} MMLCommands, skipped {skipped} non-command -> {out}")
    return ok
