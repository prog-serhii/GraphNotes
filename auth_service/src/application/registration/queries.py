from datetime import datetime

from pydantic import BaseModel

from app.application.queries import Query


class GetUserRegistrationQuery(Query):
    pass


class UserRegistrationDto(BaseModel):
    email: str
    first_name: str
    last_name: str
    register_date: datetime
    status: str
