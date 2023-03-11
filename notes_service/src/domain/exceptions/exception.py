from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from domain.rules import BusinessRule


class DomainException(Exception):
    pass


class BusinessRuleValidationException(DomainException):

    def __init__(self, rule: BusinessRule) -> None:
        self.rule = rule

    def __str__(self) -> str:
        return str(self.rule)
