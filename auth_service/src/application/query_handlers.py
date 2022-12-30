from typing import Any


class QueryResult:

    def __init__(self, result: Any) -> None:
        self.__result = result
        self.__errors = []


class QueryHandler:
    """Base query handler class"""
