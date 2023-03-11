import abc

from domain.entities import Entity
from domain.value_objects import UUID


class Repository(abc.ABC):
    """An interface for a generic repository"""

    @abc.abstractmethod
    def add(self, entity: Entity):
        raise NotImplementedError()

    @abc.abstractmethod
    def remove(self, entity: Entity):
        raise NotImplementedError()

    @abc.abstractmethod
    def get_by_id(self, id_: UUID) -> Entity:
        raise NotImplementedError()

    def __getitem__(self, index) -> Entity:
        return self.get_by_id(index)

    @staticmethod
    def next_id() -> UUID:
        return UUID.v4()
