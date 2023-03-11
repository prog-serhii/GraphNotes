from __future__ import annotations

from typing import Any

from domain.value_objects import UUID


class Entity:
    """Base class for entity objects"""

    def __init__(self, entity_id: UUID) -> None:
        self.id = entity_id

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Entity):
            return False
        return other.id == self.id

    @classmethod
    def next_id(cls) -> UUID:
        return UUID.v4()
