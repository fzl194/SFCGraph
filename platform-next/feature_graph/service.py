"""Feature graph data service — reads CSV files, provides business logic."""
from pathlib import Path
from shared.config import get_config
from shared.csv_service import load_csv


class FeatureGraphService:
    def __init__(self):
        cfg = get_config()["feature_graph"]
        self._data_dir = Path(cfg["data_dir"]).resolve()
        self._doc_root = Path(cfg["doc_root"]).resolve()
        self._columns = cfg.get("columns", [])
        self._features = load_csv(str(self._data_dir / "l1_udg_feature_attributes.csv"))
        self._docs = load_csv(str(self._data_dir / "l1_udg_doc_assets.csv"))
        self._dependencies = load_csv(str(self._data_dir / "l1_udg_feature_dependency.csv"))
        self._licenses = load_csv(str(self._data_dir / "l1_udg_feature_license.csv"))
        # Also try UNC data
        self._unc_features = load_csv(str(self._data_dir / "l1_unc_feature_attributes.csv"))
        self._unc_docs = load_csv(str(self._data_dir / "l1_unc_doc_assets.csv"))
        self._unc_deps = load_csv(str(self._data_dir / "l1_unc_feature_dependency.csv"))
        self._unc_licenses = load_csv(str(self._data_dir / "l1_unc_feature_license.csv"))

    def get_column_config(self) -> list[dict]:
        return self._columns

    def get_stats(self) -> dict:
        features = self._all_features()
        total = len(features)
        by_product: dict[str, int] = {}
        by_type: dict[str, int] = {}
        by_section: dict[str, int] = {}
        config_required_count = 0
        for f in features:
            p = f.get("product_type", "unknown")
            t = f.get("feature_type", "unknown")
            s = f.get("section", "unknown")
            by_product[p] = by_product.get(p, 0) + 1
            by_type[t] = by_type.get(t, 0) + 1
            by_section[s] = by_section.get(s, 0) + 1
            if f.get("config_required", "").lower() in ("true", "yes"):
                config_required_count += 1
        return {
            "total": total,
            "config_required": config_required_count,
            "by_product": by_product,
            "by_type": by_type,
            "by_section": by_section,
        }

    def list_features(
        self,
        product_type: str | None = None,
        feature_type: str | None = None,
        section: str | None = None,
        search: str | None = None,
        page: int = 1,
        size: int = 50,
    ) -> dict:
        features = self._all_features()
        # Filter
        filtered = []
        for f in features:
            if product_type and f.get("product_type") != product_type:
                continue
            if feature_type and f.get("feature_type") != feature_type:
                continue
            if section and f.get("section") != section:
                continue
            if search:
                s_lower = search.lower()
                searchable = (
                    f.get("feature_id", "") + f.get("feature_name", "") + f.get("definition", "")
                ).lower()
                if s_lower not in searchable:
                    continue
            filtered.append(f)
        total = len(filtered)
        start = (page - 1) * size
        items = filtered[start : start + size]
        return {"total": total, "page": page, "size": size, "items": items}

    def get_feature(self, feature_id: str, product_type: str | None = None) -> dict | None:
        for f in self._all_features():
            if f.get("feature_id") == feature_id:
                if product_type and f.get("product_type") != product_type:
                    continue
                return f
        return None

    def get_feature_docs(self, feature_id: str) -> list[dict]:
        all_docs = self._docs + self._unc_docs
        return [d for d in all_docs if d.get("feature_id") == feature_id]

    def get_feature_deps(self, feature_id: str) -> list[dict]:
        all_deps = self._dependencies + self._unc_deps
        return [
            d
            for d in all_deps
            if d.get("source_feature_id") == feature_id
            or d.get("target_feature_id") == feature_id
        ]

    def get_feature_licenses(self, feature_id: str) -> list[dict]:
        all_lic = self._licenses + self._unc_licenses
        return [l for l in all_lic if l.get("feature_id") == feature_id]

    def get_all_dependencies(
        self,
        dependency_type: str | None = None,
    ) -> list[dict]:
        all_deps = self._dependencies + self._unc_deps
        if dependency_type:
            return [d for d in all_deps if d.get("dependency_type") == dependency_type]
        return all_deps

    def get_all_licenses(self) -> list[dict]:
        return self._licenses + self._unc_licenses

    def get_doc_content(self, rel_path: str) -> str:
        """Read an md file content from doc_root. Prevents path traversal."""
        full_path = (self._doc_root / rel_path).resolve()
        doc_root_resolved = str(self._doc_root.resolve())
        if not str(full_path).startswith(doc_root_resolved):
            return "Access denied: path traversal blocked"
        if not full_path.exists():
            return f"File not found: {rel_path}"
        try:
            return full_path.read_text(encoding="utf-8")
        except Exception as e:
            return f"Error reading file: {e}"

    def resolve_doc_path(self, rel_path: str) -> Path | None:
        """Resolve and validate a doc path. Returns None if traversal or not found."""
        full_path = (self._doc_root / rel_path).resolve()
        doc_root_resolved = str(self._doc_root.resolve())
        if not str(full_path).startswith(doc_root_resolved):
            return None
        if not full_path.exists() or not full_path.is_file():
            return None
        return full_path

    # --- internal ---

    def _all_features(self) -> list[dict]:
        return self._features + self._unc_features


# Singleton
_service: FeatureGraphService | None = None


def get_service() -> FeatureGraphService:
    global _service
    if _service is None:
        _service = FeatureGraphService()
    return _service
