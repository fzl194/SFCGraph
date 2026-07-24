"""用户操作：生成 key、认证、权限检查、CRUD。"""
import secrets
from datetime import datetime, timezone
from typing import Optional

from . import store


def gen_key() -> str:
    """生成全局唯一 key（撞则重试）。"""
    while True:
        k = "gap_" + secrets.token_hex(16)
        if store.find_by_key(k) is None:
            return k


def authenticate(key: str) -> Optional[dict]:
    return store.find_by_key(key)


def check_perm(user: dict, perm: str) -> bool:
    """perm ∈ frontend/upload/test/skill/admin。
    upload/test 依赖 can_frontend（无前端权限则无效）；is_admin 全权。"""
    if user.get("is_admin"):
        return True
    if perm == "frontend":
        return bool(user.get("can_frontend"))
    if perm == "upload":
        return bool(user.get("can_frontend")) and bool(user.get("can_upload"))
    if perm == "test":
        return bool(user.get("can_frontend")) and bool(user.get("can_test"))
    if perm == "skill":
        return bool(user.get("can_skill")) or bool(user.get("can_frontend"))
    return False  # admin 仅 is_admin


def create_user(username: str, can_frontend: bool, can_skill: bool, is_admin: bool = False, can_upload: bool = False, can_test: bool = False) -> dict:
    if store.find_by_name(username) is not None:
        raise ValueError(f"用户已存在: {username}")
    user = {
        "username": username,
        "key": gen_key(),
        "can_frontend": can_frontend,
        "can_upload": can_upload,
        "can_test": can_test,
        "can_skill": can_skill,
        "is_admin": is_admin,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    return store.add_user(user)


def reset_key(username: str) -> Optional[str]:
    k = gen_key()
    u = store.update_user(username, {"key": k})
    return k if u else None


def set_perms(username: str, *, can_frontend: bool, can_upload: bool, can_test: bool, can_skill: bool, is_admin: bool) -> Optional[dict]:
    return store.update_user(username, {
        "can_frontend": can_frontend, "can_upload": can_upload, "can_test": can_test,
        "can_skill": can_skill, "is_admin": is_admin,
    })


def delete_user(username: str) -> bool:
    return store.delete_user(username)
