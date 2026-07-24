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
    sk = {"can_skill": True}
    plain = {}
    assert check_perm(admin, "frontend") and check_perm(admin, "skill") and check_perm(admin, "admin")
    assert check_perm(fe, "frontend") and check_perm(fe, "skill") and not check_perm(fe, "admin")
    assert not check_perm(sk, "frontend") and check_perm(sk, "skill") and not check_perm(sk, "admin")
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
    set_perms("u", can_frontend=True, can_skill=True, is_admin=False)
    assert find_by_name("u")["can_frontend"] is True
