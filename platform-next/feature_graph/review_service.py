"""In-memory review state service.

Stores accept/reject decisions for dependencies and licenses.
Ready for future DB replacement — just swap the implementation.
"""
from dataclasses import dataclass, field
from enum import Enum


class ReviewStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"


@dataclass
class ReviewItem:
    item_type: str   # "dependency" | "license"
    item_id: str     # composite key, e.g. "GWFD-020301:dep:GWFD-110101"
    status: ReviewStatus = ReviewStatus.PENDING
    comment: str = ""


class ReviewStore:
    """Interface for review state. Current impl: in-memory dict.
    Future: swap to DB-backed implementation.
    """

    def __init__(self):
        self._items: dict[str, ReviewItem] = {}

    def _key(self, item_type: str, item_id: str) -> str:
        return f"{item_type}:{item_id}"

    def get_status(self, item_type: str, item_id: str) -> ReviewStatus:
        key = self._key(item_type, item_id)
        return self._items[key].status if key in self._items else ReviewStatus.PENDING

    def get_comment(self, item_type: str, item_id: str) -> str:
        key = self._key(item_type, item_id)
        return self._items[key].comment if key in self._items else ""

    def accept(self, item_type: str, item_id: str, comment: str = "") -> ReviewItem:
        key = self._key(item_type, item_id)
        item = ReviewItem(item_type=item_type, item_id=item_id,
                          status=ReviewStatus.ACCEPTED, comment=comment)
        self._items[key] = item
        return item

    def reject(self, item_type: str, item_id: str, comment: str = "") -> ReviewItem:
        key = self._key(item_type, item_id)
        item = ReviewItem(item_type=item_type, item_id=item_id,
                          status=ReviewStatus.REJECTED, comment=comment)
        self._items[key] = item
        return item

    def reset(self, item_type: str, item_id: str) -> ReviewItem:
        key = self._key(item_type, item_id)
        item = ReviewItem(item_type=item_type, item_id=item_id,
                          status=ReviewStatus.PENDING)
        self._items[key] = item
        return item

    def get_all(self, item_type: str | None = None) -> list[dict]:
        items = self._items.values()
        if item_type:
            items = [i for i in items if i.item_type == item_type]
        return [
            {"item_type": i.item_type, "item_id": i.item_id,
             "status": i.status.value, "comment": i.comment}
            for i in items
        ]

    def bulk_get(self, item_type: str, item_ids: list[str]) -> dict[str, str]:
        """Return {item_id: status} for a batch of IDs."""
        return {iid: self.get_status(item_type, iid).value for iid in item_ids}


# Singleton
_store: ReviewStore | None = None


def get_review_store() -> ReviewStore:
    global _store
    if _store is None:
        _store = ReviewStore()
    return _store
