import abc

from app.domain.repositories import GenericRepository
from app.domain.session.entities import Session
from app.domain.value_objects import UUID


class SessionRepository(GenericRepository):

    @abc.abstractmethod
    def find_by_user_id(self, user_id: UUID) -> list[Session]:
        raise NotImplementedError()

    @abc.abstractmethod
    def find_by_access_token(self, access_token: str) -> Session | None:
        raise NotImplementedError()
