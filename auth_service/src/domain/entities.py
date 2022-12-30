from dataclasses import dataclass, field

from app.domain.mixins import BusinesRuleValidationMixin, EventMixin
from app.domain.value_objects import UUID


# @dataclass
# class Entity:
#     """Base class for entities"""
#
#     id: UUID = field(hash=True)
#
#     @classmethod
#     def next_id(cls) -> UUID:
#         return UUID.v4()
#
#
# @dataclass
# class AggregateRoot(BusinesRuleValidationMixin, EventMixin, Entity):
#     """Consits of 1+ entities. Spans transaction boundaries."""

class Entity:
    """Base class for entities"""

    def __init__(self, entity_id: UUID):
        self.id = entity_id

    def __hash__(self) -> int:
        return hash(self.id)

    @classmethod
    def next_id(cls) -> UUID:
        return UUID.v4()
