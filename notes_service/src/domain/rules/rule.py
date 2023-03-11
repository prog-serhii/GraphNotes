from pydantic import BaseModel

from domain.exceptions import BusinessRuleValidationException


class BusinessRule(BaseModel):
    """This is a base class for implementing domain rules"""

    class Congig:
        arbitrary_types_allowed = True

    ___message: str = 'Busioness rule is broken'

    def get_message(self) -> str:
        return self.___message

    def is_broken(self) -> bool:
        pass

    def __str__(self) -> str:
        return f'{self.__class__.__name__} {super().__str__()}'


class BusinessRuleValidationMixin:

    def check_rule(self, rule: BusinessRule):
        if rule.is_broken():
            raise BusinessRuleValidationException(rule)
