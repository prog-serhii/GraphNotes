from datetime import datetime, timedelta

from app.domain.entities import Entity
from app.domain.value_objects import UUID
from app.domain.users.entities import User
from app.domain.session.token_provider import TokenProvider


class Session(Entity):

    def __init__(
        self, session_id: UUID, user: User, token_provider: TokenProvider,
        remember_me: bool, user_agent: str, ip_address: str
    ):
        super().__init__(session_id)
        self.ip_address: str = ip_address
        self.user_agent: str = user_agent
        self.user_id: UUID = user.id
        self.expiration_date: datetime = datetime.utcnow() + timedelta(days=3)
        self.access_token = token_provider.create_token(user)

        self.refresh_token: str | None = None
        if remember_me:
            self.refresh_token = token_provider.create_refresh_token(user)

        self.last_activity: datetime | None = None

    @property
    def is_expired(self) -> bool:
        return datetime.utcnow() > self.expiration_date
