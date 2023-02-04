from domain.rules import BusinessRule


class DomainException(Exception):
    pass


class BusinesValidationException(DomainException):

    def __init__(self, rule: BusinessRule) -> None:
        self.rule = rule

    def __str__(self) -> str:
        return str(self.rule)
