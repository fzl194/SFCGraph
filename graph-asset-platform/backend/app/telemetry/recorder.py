"""打点记录器：对象级访问追加到 jsonl。

打点是观测用、非功能性：record() 内部吞异常，绝不向上抛，绝不阻断 /md、/domains 请求。
"""
import json
import logging
import threading
from datetime import datetime, timezone
from pathlib import Path

from .. import config  # 运行时读 config.TELEMETRY_FILE，便于测试 monkeypatch（与 auth.py 同模式）

logger = logging.getLogger(__name__)
_lock = threading.Lock()


def record(endpoint: str, id_: str, type_: str) -> None:
    """追加一条对象级访问记录。失败吞掉 + log，不抛。"""
    try:
        line = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "endpoint": endpoint,
            "id": id_,
            "type": type_,
        }
        path = Path(config.TELEMETRY_FILE)
        path.parent.mkdir(parents=True, exist_ok=True)
        with _lock:
            with open(path, "a", encoding="utf-8") as f:
                f.write(json.dumps(line, ensure_ascii=False) + "\n")
    except Exception as e:  # noqa: BLE001 — 观测用，绝不阻断业务
        logger.warning("telemetry record failed: %s", e)
