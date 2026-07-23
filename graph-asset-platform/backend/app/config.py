import os
from pathlib import Path

# 资产库根（可被环境变量覆盖）。默认 ./platform-data/assets
DATA_DIR = Path(__file__).resolve().parents[2] / "platform-data"
ASSETS_DIR = DATA_DIR / "assets"
TESTS_DIR = DATA_DIR / "tests"  # 测试用例管理子系统（独立于 assets，隔离）
DEFAULT_REGISTRY_PATH = Path(__file__).resolve().parent / "default_registry.yaml"

# —— 鉴权（单一共享 KEY；空 → 中间件旁路，仅开发用）——
# 取值绝不 echo 到日志/响应（见 spec §6）。
API_KEY = os.environ.get("GAP_API_KEY", "")

# —— 运营打点（jsonl，对象级）——
TELEMETRY_DIR = DATA_DIR / "telemetry"
TELEMETRY_FILE = TELEMETRY_DIR / "access.jsonl"
