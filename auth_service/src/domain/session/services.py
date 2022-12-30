from datetime import datetime

from app.domain.session.entities import Session
from app.domain.session.token_provider import TokenProvider
from app.domain.session.repositories import SessionRepository
from app.domain.users.repositories import UserRepository


class SessionAuthenticationService:

    def __init__(
        self, token_provider: TokenProvider, session_repository: SessionRepository, user_repository: UserRepository
    ):
        self.token_provider = token_provider
        self.session_repository = session_repository
        self.user_repository = user_repository

    def authenticate(self, access_token: str):
        session = self.session_repository.find_by_access_token(access_token)
        if not session:
            raise Exception(f'Session with access code {access_token} doesn\'t exist.')

        # checkRule(newSessionCannotBeExpiredWhenRefreshTokenIsMissing(session));
        if session.is_expired:
            return Session(
                session_id=Session.next_id(),
                user=self.user_repository.get_by_id(session.user_id),
                token_provider=self.token_provider,
                remember_me=True,
                user_agent=session.user_agent,
                ip_address=session.ip_address
            )

        session.last_activity = datetime.utcnow()
        return session

    def logout(self, access_token: str):
        session = self.session_repository.find_by_access_token(access_token)
        if not session:
            raise Exception(f'Session with access code {access_token} doesn\'t exist.')

        session.expiration_date = datetime.utcnow()
        session.refresh_token = None
        return self.session_repository.update(session)
