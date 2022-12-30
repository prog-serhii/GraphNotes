import abc

from app.domain.entities import Entity
from app.domain.repositories import GenericRepository


class UserRepository(GenericRepository):
    """An interface for User repository"""

    @abc.abstractmethod
    def find_by_email(self, email: str) -> Entity | None:
        raise NotImplementedError()
