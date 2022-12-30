from __future__ import annotations

import sys
from typing import Any

from pydantic import BaseModel

from app.domain.events import DomainEvent


class CommandResult(BaseModel):
    result: Any = None
    events: list[DomainEvent] = []
    errors: list[Any] = []

    def has_errors(self) -> bool:
        return len(self.errors) > 0

    def is_ok(self) -> bool:
        return not self.has_errors()

    @classmethod
    def ok(cls, result: Any = None, events: list | None = None) -> CommandResult:
        """Creates a successful result"""
        if events is None:
            events = []
        return cls(result=result, events=events)
    
    @classmethod
    def failed(cls, message: str = 'Failure', exception: Exception | None = None) -> CommandResult:
        """Creates a failed result"""
        exception_info = sys.exc_info()
        errors = [(message, exception, exception_info)]
        return cls(errors=errors)


class CommandHandler:
    pass
