from .unit_of_work import AbstractUnitOfWork


class FakeUnitOfWork(AbstractUnitOfWork):

    def commit(self):
        pass

    def rollback(self):
        pass
