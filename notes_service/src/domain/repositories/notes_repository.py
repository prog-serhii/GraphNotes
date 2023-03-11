from abc import ABC

from domain.repositories import Repository


class NotesRepository(Repository, ABC):
    """An interface for Notes Repository"""
