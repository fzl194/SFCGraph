"""Configuration loader for platform-next."""
from pathlib import Path
import yaml

_CONFIG: dict | None = None


def load_config() -> dict:
    global _CONFIG
    if _CONFIG is None:
        config_path = Path(__file__).resolve().parent.parent / "config.yaml"
        with open(config_path, "r", encoding="utf-8") as f:
            _CONFIG = yaml.safe_load(f)
    return _CONFIG


def get_config() -> dict:
    if _CONFIG is None:
        return load_config()
    return _CONFIG
