import pytest
from pathlib import Path


@pytest.fixture
def tmp_data_dir(tmp_path, monkeypatch):
    """把 app.config.DATA_DIR / ASSETS_DIR 重定向到 tmp_path，返回 assets 目录 Path。"""
    data = tmp_path / "platform-data"
    assets = data / "assets"
    assets.mkdir(parents=True)
    import app.config as config
    monkeypatch.setattr(config, "DATA_DIR", data)
    monkeypatch.setattr(config, "ASSETS_DIR", assets)
    return assets
