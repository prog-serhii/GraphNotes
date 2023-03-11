from infrastructure.repositories import Repository


class InMemoryRepository(Repository):
    def __init__(self) -> None:
        self.objects = {}
