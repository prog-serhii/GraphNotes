import abc

from app.domain.entities import Entity
from app.domain.value_objects import UUID


class GenericRepository(abc.ABC):
    """An interface for generic repository"""

    @abc.abstractmethod
    def add(self, entity: Entity):
        raise NotImplementedError()

    @abc.abstractmethod
    def remove(self, entity: Entity):
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, entity: Entity):
        raise NotImplementedError()

    @abc.abstractmethod
    def get_by_id(self, id: UUID) -> Entity:
        raise NotImplementedError()

    def __getitem__(self, index: UUID) -> Entity:
        return self.get_by_id(index)

    @staticmethod
    def next_id() -> UUID:
        return UUID.v4()
