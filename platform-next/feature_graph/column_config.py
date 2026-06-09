"""Column configuration for feature graph list view."""
from shared.config import get_config


def get_columns() -> list[dict]:
    """Return column config from config.yaml."""
    cfg = get_config()
    return cfg.get("feature_graph", {}).get("columns", [])
