from pathlib import Path


class Store:
    """统一资产库读写：在 <data>/assets/ 下按相对路径读写 md 文件。

    所有 rel（相对路径）参数均为使用正斜杠的归一化路径（如
    ``Command/UDG/20.15.2/UDG@MMLCommand@ADD URR.md``）。实现内部会做路径穿越防护，
    任何逃逸 assets 根的路径都会抛 ``ValueError``。
    """

    def __init__(self, assets_dir: Path):
        self.root = Path(assets_dir)
        self.root.mkdir(parents=True, exist_ok=True)
        # resolve 一次缓存，避免每次调用都做系统调用
        self._root_resolved = self.root.resolve()

    def _resolve(self, rel: str) -> Path:
        """把相对路径解析为绝对路径，并校验未逃逸 assets 根。"""
        rel_path = rel.replace("\\", "/")
        # 严格禁止绝对路径与盘符写法（Windows 下 "C:\\..." 会被 Path 拼接覆盖根）
        if rel_path.startswith("/"):
            raise ValueError(f"非法路径（绝对路径）: {rel}")
        # pathlib 的 join 对含 .. 的路径会原样拼接；用 os.path.normpath 思路：直接 resolve 后比对祖先
        p = (self.root / rel_path).resolve()
        root = self._root_resolved
        if p != root and root not in p.parents:
            raise ValueError(f"非法路径（逃逸 assets 根）: {rel}")
        return p

    def write(self, rel: str, text: str) -> None:
        p = self._resolve(rel)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")

    def read(self, rel: str) -> str:
        return self._resolve(rel).read_text(encoding="utf-8")

    def exists(self, rel: str) -> bool:
        return self._resolve(rel).exists()

    def list_md(self) -> list:
        """返回所有 md 文件相对 assets 根的归一化路径（正斜杠）。"""
        return [
            str(p.relative_to(self.root)).replace("\\", "/")
            for p in self.root.rglob("*.md")
        ]

    def list_dir(self, rel: str = "") -> tuple[list[str], list[str]]:
        """该目录的直接子项（不递归）→ (子目录名列表, 文件名列表)，均排序。

        供前端文件夹树懒加载：展开某层只读该层子项，避免一次拉全量。
        rel 为空时返回 assets 根的直接子项。不存在/非目录 → ([], [])。
        """
        p = self._resolve(rel) if rel else self._root_resolved
        if not p.exists() or not p.is_dir():
            return [], []
        dirs: list[str] = []
        files: list[str] = []
        for child in p.iterdir():
            if child.is_dir():
                dirs.append(child.name)
            elif child.is_file():
                files.append(child.name)
        return sorted(dirs), sorted(files)
