from domain.rules import BusinessRuleValidationMixin
from .entity import Entity


class Aggregate(BusinessRuleValidationMixin, Entity):
    """Consits of 1+ entities. Spans transaction boundaries."""
