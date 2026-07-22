"""测试子系统单例 Service + 写入锁。

``get_test_service`` 延迟构造；写审查（写盘）+ rebuild 必须串行化（``test_lock``），
独立于图谱 ``import_lock``，互不干扰。
"""
import threading
from typing import Optional

from ..config import TESTS_DIR
from .index import TestIndex
from .store import TestStore

# 模块级写入锁（独立于图谱 service.import_lock）
test_lock = threading.Lock()


class TestService:
    def __init__(self):
        self.store = TestStore(TESTS_DIR)
        self.index = TestIndex.build(self.store)

    def rebuild(self) -> None:
        """写盘后重建内存索引（读 API 必须看到最新数据）。"""
        self.index = TestIndex.build(self.store)


_test_service: Optional[TestService] = None


def get_test_service() -> TestService:
    global _test_service
    if _test_service is None:
        _test_service = TestService()
    return _test_service
