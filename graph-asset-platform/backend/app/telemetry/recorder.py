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


def record(endpoint: str, id_: str = "", type_: str = "", *, user: str = "", caller: str = "", level: str = "request", operator: str = "") -> None:
    """追加一条访问记录。失败吞掉 + log，不抛。

    level: request/object；operator: SKILL 调用者工号（X-User-Id），前端为空。
    """
    try:
        line = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "user": user,
            "operator": operator,
            "caller": caller,
            "endpoint": endpoint,
            "id": id_,
            "type": type_,
            "level": level,
        }
        path = Path(config.TELEMETRY_OBJECTS_FILE if level == "object" else config.TELEMETRY_REQUESTS_FILE)
        path.parent.mkdir(parents=True, exist_ok=True)
        with _lock:
            with open(path, "a", encoding="utf-8") as f:
                f.write(json.dumps(line, ensure_ascii=False) + "\n")
    except Exception as e:  # noqa: BLE001 — 观测用，绝不阻断业务
        logger.warning("telemetry record failed: %s", e)
