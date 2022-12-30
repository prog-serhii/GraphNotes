from app.domain.events import DomainEvent
from app.domain.value_objects import UUID


class SessionCreated(DomainEvent):
    session_id: str
    user_id: UUID
