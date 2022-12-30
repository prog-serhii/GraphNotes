class DomainException(Exception):
    pass


class BusinesValidationException(DomainException):

    def __init__(self, rule) -> None:
        self.rule = rule

    def __str__(self) -> str:
        return str(self.rule)
