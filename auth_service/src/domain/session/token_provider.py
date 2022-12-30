import abc

from app.domain.users.entities import User
from app.domain.value_objects import UUID


class TokenProvider(abc.ABC):

    @abc.abstractmethod
    def create_token(self, user: User) -> str:
        raise NotImplementedError()

    @abc.abstractmethod
    def create_refresh_token(self, user: User) -> str:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_user_id_from_token(self, auth_token: str) -> UUID:
        raise NotImplementedError()