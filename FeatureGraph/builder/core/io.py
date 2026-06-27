"""JSONL 读写工具（FeatureGraph 公共）。"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable


def load_jsonl(path: str | Path) -> list[dict]:
    """读 JSONL，文件不存在返回空列表。"""
    fp = Path(path)
    if not fp.exists():
        return []
    with fp.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def write_jsonl(path: str | Path, items: Iterable[dict]) -> None:
    """写 JSONL（覆盖），自动创建父目录。"""
    fp = Path(path)
    fp.parent.mkdir(parents=True, exist_ok=True)
    with fp.open("w", encoding="utf-8") as f:
        for item in items:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
