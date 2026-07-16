from pathlib import Path

# 资产库根（可被环境变量覆盖）。默认 ./platform-data/assets
DATA_DIR = Path(__file__).resolve().parents[2] / "platform-data"
ASSETS_DIR = DATA_DIR / "assets"
DEFAULT_REGISTRY_PATH = Path(__file__).resolve().parent / "default_registry.yaml"
