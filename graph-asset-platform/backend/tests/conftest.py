import io
import zipfile

import pytest
from pathlib import Path

FIXTURES_DIR = Path(__file__).parent / "fixtures"


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


@pytest.fixture
def sample_bundle_zip() -> bytes:
    """把 tests/fixtures/sample_bundle/ 目录打包成 zip 字节。

    目录布局 = 与统一资产库一致的归一化相对路径（Layer/nf/version/id.md 与
    Business/domain/scenario/id.md），可直接喂给 ``import_bundle``。
    """
    root = FIXTURES_DIR / "sample_bundle"
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(root.rglob("*")):
            if p.is_file():
                rel = p.relative_to(root).as_posix()
                z.writestr(rel, p.read_text(encoding="utf-8"))
    return buf.getvalue()
