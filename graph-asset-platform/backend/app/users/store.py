"""users.json 读写（明文 KEY；进程内 Lock 串行写，保证原子）。"""
import json
import threading
from pathlib import Path
from typing import Optional

from .. import config

_lock = threading.Lock()


def _load() -> dict:
    path = Path(config.USERS_FILE)
    if not path.exists():
        return {"users": []}
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    data.setdefault("users", [])
    return data


def _save(data: dict) -> None:
    path = Path(config.USERS_FILE)
    path.parent.mkdir(parents=True, exist_ok=True)
    with _lock:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


def list_users() -> list:
    return _load()["users"]


def find_by_key(key: str) -> Optional[dict]:
    for u in _load()["users"]:
        if u.get("key") == key:
            return u
    return None


def find_by_name(username: str) -> Optional[dict]:
    for u in _load()["users"]:
        if u.get("username") == username:
            return u
    return None


def add_user(user: dict) -> dict:
    data = _load()
    data["users"].append(user)
    _save(data)
    return user


def update_user(username: str, patch: dict) -> Optional[dict]:
    data = _load()
    for u in data["users"]:
        if u.get("username") == username:
            u.update(patch)
            _save(data)
            return u
    return None


def delete_user(username: str) -> bool:
    data = _load()
    before = len(data["users"])
    data["users"] = [u for u in data["users"] if u.get("username") != username]
    if len(data["users"]) < before:
        _save(data)
        return True
    return False
