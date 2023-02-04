from domain.exceptions import BusinesValidationException
from domain.rules import BusinessRule


class BusinesRuleValidationMixin:

    @staticmethod
    def check_rule(rule: BusinessRule) -> None:
        if rule.is_broken():
            raise BusinesValidationException(rule)
