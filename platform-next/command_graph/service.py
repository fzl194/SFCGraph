"""Command graph data service — reads CSV files, provides business logic."""
import json
from pathlib import Path
from shared.csv_service import load_csv


class CommandGraphService:
    def __init__(self):
        self._data_dir = Path(__file__).resolve().parent.parent.parent / "command-graph" / "data"
        self._doc_root = Path(__file__).resolve().parent.parent.parent
        self._udg = load_csv(str(self._data_dir / "udg_commands.csv"))
        self._unc = load_csv(str(self._data_dir / "unc_commands.csv"))

    def _all_commands(self) -> list[dict]:
        return self._udg + self._unc

    def get_stats(self) -> dict:
        all_cmds = self._all_commands()
        by_product = {}
        for c in all_cmds:
            p = c.get("product", "unknown")
            by_product[p] = by_product.get(p, 0) + 1
        return {
            "total": len(all_cmds),
            "udg": len(self._udg),
            "unc": len(self._unc),
            "by_product": by_product,
        }

    def list_commands(
        self,
        product: str | None = None,
        search: str | None = None,
        page: int = 1,
        size: int = 50,
    ) -> dict:
        commands = self._all_commands()
        filtered = []
        for c in commands:
            if product and c.get("product") != product:
                continue
            if search:
                s_lower = search.lower()
                searchable = (
                    c.get("command_name", "")
                    + c.get("command_name_zh", "")
                    + c.get("command_function", "")
                    + "".join(json.loads(c.get("category_path", "[]")))
                ).lower()
                if s_lower not in searchable:
                    continue
            filtered.append(c)

        # Sort globally by product then command_name
        filtered.sort(key=lambda c: (c.get("product", ""), c.get("command_name", "")))

        total = len(filtered)
        start = (page - 1) * size
        items = filtered[start : start + size]
        return {"total": total, "page": page, "size": size, "items": items}

    def get_command(self, product: str, command_name: str) -> dict | None:
        source = self._udg if product == "UDG" else self._unc
        for c in source:
            if c.get("command_name") == command_name:
                return c
        return None

    def get_command_md(self, product: str, command_name: str) -> str:
        """Load and return the raw MD content for a command."""
        cmd = self.get_command(product, command_name)
        if not cmd or not cmd.get("file_path"):
            return ""
        md_path = self._doc_root / "output" / cmd["file_path"]
        if not md_path.exists():
            return ""
        return md_path.read_text(encoding="utf-8")

    def resolve_doc_path(self, rel_path: str) -> Path | None:
        """Resolve a relative path under doc_root/output, with safety checks."""
        full = (self._doc_root / "output" / rel_path).resolve()
        output_root = (self._doc_root / "output").resolve()
        if not str(full).startswith(str(output_root)):
            return None
        if full.exists() and full.is_file():
            return full
        return None

    def get_doc_content(self, rel_path: str) -> str:
        """Load MD content from a relative path under output/."""
        full = self.resolve_doc_path(rel_path)
        if not full:
            return ""
        return full.read_text(encoding="utf-8")


# Singleton
_service: CommandGraphService | None = None


def get_service() -> CommandGraphService:
    global _service
    if _service is None:
        _service = CommandGraphService()
    return _service
