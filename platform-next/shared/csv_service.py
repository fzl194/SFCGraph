"""Generic CSV loading service with caching."""
import csv
from pathlib import Path
from functools import lru_cache


@lru_cache(maxsize=32)
def load_csv(csv_path: str) -> list[dict]:
    """Load a CSV file and return list of dicts. Results are cached."""
    path = Path(csv_path)
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]


def clear_cache():
    """Clear the CSV cache (useful for data reloads)."""
    load_csv.cache_clear()
