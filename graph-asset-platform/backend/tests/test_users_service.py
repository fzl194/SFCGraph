"""users.service 测试：gen_key 唯一、authenticate、check_perm 矩阵、create/reset/delete。"""


def _seed(tmp_path, monkeypatch, users):
    import json
    import app.config as cfg
    monkeypatch.setattr(cfg, "USERS_FILE", tmp_path / "users.json")
    (tmp_path / "users.json").write_text(json.dumps({"users": users}), encoding="utf-8")


def test_gen_key_unique_and_prefixed(tmp_path, monkeypatch):
    _seed(tmp_path, monkeypatch, [{"username": "a", "key": "gap_existing"}])
    from app.users.service import gen_key
    k = gen_key()
    assert k.startswith("gap_") and k != "gap_existing"


def test_authenticate_by_key(tmp_path, monkeypatch):
    _seed(tmp_path, monkeypatch, [{"username": "u", "key": "k1", "can_skill": True}])
    from app.users.service import authenticate
    assert authenticate("k1")["username"] == "u"
    assert authenticate("nope") is None


def test_check_perm_matrix():
    from app.users.service import check_perm
    admin = {"is_admin": True}
    fe = {"can_frontend": True}
    fe_up = {"can_frontend": True, "can_upload": True}
    fe_test = {"can_frontend": True, "can_test": True}
    sk = {"can_skill": True}
    plain = {}
    # admin 全权
    assert all(check_perm(admin, p) for p in ("frontend", "upload", "test", "skill", "admin"))
    # can_frontend：前端✓，但 upload/test✗（需额外 flag）
    assert check_perm(fe, "frontend") and not check_perm(fe, "upload") and not check_perm(fe, "test")
    # can_frontend+can_upload：upload✓，test✗
    assert check_perm(fe_up, "upload") and not check_perm(fe_up, "test")
    # can_frontend+can_test：test✓，upload✗
    assert check_perm(fe_test, "test") and not check_perm(fe_test, "upload")
    # 无 can_frontend 但有 can_upload：upload✗（依赖 can_frontend）
    assert not check_perm({"can_upload": True}, "upload")
    # can_skill：skill✓，前端✗
    assert check_perm(sk, "skill") and not check_perm(sk, "frontend")
    assert not check_perm(plain, "frontend")


def test_create_user_returns_key_and_rejects_dup(tmp_path, monkeypatch):
    _seed(tmp_path, monkeypatch, [{"username": "u", "key": "k"}])
    from app.users.service import create_user
    import pytest
    u = create_user("new", can_frontend=True, can_skill=False)
    assert u["key"].startswith("gap_") and u["can_frontend"] is True
    with pytest.raises(ValueError):
        create_user("u", can_frontend=False, can_skill=False)


def test_reset_key_and_set_perms(tmp_path, monkeypatch):
    _seed(tmp_path, monkeypatch, [{"username": "u", "key": "k", "can_frontend": False}])
    from app.users.service import reset_key, set_perms
    from app.users.store import find_by_name
    new_k = reset_key("u")
    assert new_k and new_k != "k"
    set_perms("u", can_frontend=True, can_upload=False, can_test=False, can_skill=True, is_admin=False)
    assert find_by_name("u")["can_frontend"] is True


def test_set_perms_roundtrip_all_flags(tmp_path, monkeypatch):
    """set_perms 6 个权限位往返（防位置参数顺序写错）。"""
    _seed(tmp_path, monkeypatch, [{"username": "u", "key": "k"}])
    from app.users.service import set_perms
    from app.users.store import find_by_name
    set_perms("u", can_frontend=True, can_upload=True, can_test=False, can_skill=True, is_admin=False)
    u = find_by_name("u")
    assert u["can_frontend"] is True
    assert u["can_upload"] is True
    assert u["can_test"] is False
    assert u["can_skill"] is True
    assert u["is_admin"] is False
