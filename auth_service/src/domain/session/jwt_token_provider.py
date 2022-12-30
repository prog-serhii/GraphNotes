import uuid
from datetime import datetime, timedelta

from jose import JWTError, jwt

from app.domain.users.entities import User
from app.domain.session.token_provider import TokenProvider
from app.domain.value_objects import UUID


class JWTTokenProvider(TokenProvider):
    SECRET_KEY = "49ab29c11e371da0230bb762f24119d9fd98486ed34a4b74585db50f714f285e"
    ALGORITHM = "HS256"
    REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 30
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    def create_token(self, user: User, expires_delta: timedelta | None = None) -> str:
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
        data_to_encode = {'sub': str(user.id), 'exp': expire}
        return jwt.encode(data_to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)

    def create_refresh_token(self, user: User) -> str:
        return self.create_token(
            user=user, expires_delta=timedelta(minutes=self.REFRESH_TOKEN_EXPIRE_MINUTES)
        )

    def get_user_id_from_token(self, auth_token: str) -> UUID:
        payload = jwt.decode(auth_token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
        return uuid.UUID(payload['sub'])

    def validate_token(self, auth_token: str) -> bool:
        try:
            payload = jwt.decode(auth_token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            if 'sub' not in payload:
                print('JWT token has not expected format')
                return False
            return True
        except JWTError:
            print('Invalid or expi JWT token')
            return False
