from typing import Type


from domain.entities import Entity
from infrastructure.repositories import Repository


class SqlAlchemyRepository(Repository):
    data_mapper = None
    model_class: Type[Entity] = None
