"""Step license: 扫描 License 控制项文档 → licenses.jsonl。"""
from __future__ import annotations

from pathlib import Path

from ..core.io import write_jsonl
from ..core.license import extract_license_items
from .registry import step


@step("license", output_file="licenses.jsonl")
def run(ctx):
    source = Path(ctx["license_source"])
    out = Path(ctx["data_dir"]) / "licenses.jsonl"
    items = extract_license_items(source, ctx["project_root"], ctx["nf"], ctx["version"])
    write_jsonl(out, items)
    print(f"[license:{ctx['nf']}/{ctx['version']}] {len(items)} License → {out}")
    return len(items)
