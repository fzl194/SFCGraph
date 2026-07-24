from pathlib import Path

# 资产库根（可被环境变量覆盖）。默认 ./platform-data/assets
DATA_DIR = Path(__file__).resolve().parents[2] / "platform-data"
ASSETS_DIR = DATA_DIR / "assets"
TESTS_DIR = DATA_DIR / "tests"  # 测试用例管理子系统（独立于 assets，隔离）
DEFAULT_REGISTRY_PATH = Path(__file__).resolve().parent / "default_registry.yaml"

# —— 运营打点（jsonl，对象级 + 请求级）——
TELEMETRY_DIR = DATA_DIR / "telemetry"
TELEMETRY_FILE = TELEMETRY_DIR / "access.jsonl"

# —— 用户体系（多用户，明文 KEY，不入 git）——
USERS_FILE = DATA_DIR / "users.json"
