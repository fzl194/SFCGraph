"""步骤 enrich：读 mml_commands.jsonl → 跑全部 extractor → 写回 + 打印非空率。

run(ctx) -> int(处理条数)。从旧 enrich_mmlcommand.main 移植，
改为遍历 extractors.registry.apply_all（注册制），不再硬编码 10 个调用。

幂等：派生字段可重算覆盖（沿用旧机制）。
"""
import json
from pathlib import Path
from types import SimpleNamespace

from ..extractors import registry


def run(ctx: SimpleNamespace) -> int:
    p = Path(ctx.out_dir) / "mml_commands.jsonl"
    cmds = [json.loads(line) for line in p.open(encoding="utf-8") if line.strip()]
    enriched = [registry.apply_all(c) for c in cmds]
    with p.open("w", encoding="utf-8") as f:
        for c in enriched:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")

    n = len(enriched)
    print(f"[enrich:{ctx.nf}/{ctx.version}] enriched {n} commands -> {p}")
    if n:
        for field in registry.names():
            ne = sum(1 for c in enriched if c.get(field) not in (None, "", [], {}))
            print(f"  {field}: 非空 {ne}/{n} ({ne * 100 // n}%)")
    return n
