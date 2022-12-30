from app.domain.events import DomainEvent
from app.domain.value_objects import UUID


class UserCreated(DomainEvent):
    id: UUID
    first_name: str
    last_name: str
    email: str


class UserNameChanged(DomainEvent):
    first_name: str
    last_name: str
    email: str
