import uuid
from dataclasses import dataclass


UUID = uuid
UUID.v4 = uuid.uuid4


@dataclass
class ValueObject:
    """Base class for value objects"""
