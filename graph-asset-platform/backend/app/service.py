"""单例 Service：持有 store / registry / index，启动建索引，导入后重建。

测试隔离：``get_service`` 延迟构造单例；测试通过 ``monkeypatch.setattr(service, "_service", s)``
把单例指向 tmp_data_dir 上的 store，避免污染真实 platform-data。
"""
from typing import Optional

from .bundle import import_bundle  # noqa: F401  (re-export for routers)
from .config import ASSETS_DIR, DEFAULT_REGISTRY_PATH
from .index import Index
from .registry import Registry
from .store import Store


class Service:
    def __init__(self):
        self.store = Store(ASSETS_DIR)
        self.registry = Registry.load_default()
        self.index = Index.build(self.store, self.registry)

    def rebuild(self) -> None:
        """导入后重建内存索引（读 API 必须看到最新数据）。"""
        self.index = Index.build(self.store, self.registry)


_service: Optional[Service] = None


def get_service() -> Service:
    """延迟初始化的全局单例（lifespan 启动时预热）。"""
    global _service
    if _service is None:
        _service = Service()
    return _service
