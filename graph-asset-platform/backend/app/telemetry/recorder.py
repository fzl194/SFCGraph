"""打点记录器：访问记录追加到 jsonl（请求级 ① + 对象级 ②）。

打点是观测用、非功能性：record() 内部吞异常，绝不向上抛，绝不阻断业务。
"""
import json
import logging
import threading
from datetime import datetime, timezone
from pathlib import Path

from .. import config

logger = logging.getLogger(__name__)
_lock = threading.Lock()


def record(endpoint: str, id_: str = "", type_: str = "", *, user: str = "", caller: str = "", level: str = "request") -> None:
    """追加一条访问记录。失败吞掉 + log，不抛。

    level: request（中间件，全量轨迹）/ object（/md /domains，统计用）。
    """
    try:
        line = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "user": user,
            "caller": caller,
            "endpoint": endpoint,
            "id": id_,
            "type": type_,
            "level": level,
        }
        path = Path(config.TELEMETRY_FILE)
        path.parent.mkdir(parents=True, exist_ok=True)
        with _lock:
            with open(path, "a", encoding="utf-8") as f:
                f.write(json.dumps(line, ensure_ascii=False) + "\n")
    except Exception as e:  # noqa: BLE001 — 观测用，绝不阻断业务
        logger.warning("telemetry record failed: %s", e)
