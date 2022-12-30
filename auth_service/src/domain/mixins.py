from app.domain.events import DomainEvent
from app.domain.exceptions import BusinesValidationException
from app.domain.rules import BusinessRule


class BusinesRuleValidationMixin:

    @staticmethod
    def check_rule(rule: BusinessRule) -> None:
        if rule.is_broken():
            raise BusinesValidationException(rule)


class EventMixin:

    def __init__(self) -> None:
        self._pending_domain_events: list[DomainEvent] = []

    def _record_event(self, event: DomainEvent) -> None:
        self._pending_domain_events.append(event)

    @property
    def domain_events(self) -> list[DomainEvent]:
        return self._pending_domain_events[:]

    def clear_events(self) -> None:
        self._pending_domain_events.clear()
