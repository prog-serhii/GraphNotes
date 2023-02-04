from __future__ import annotations

from typing import Optional

from domain.entities import AggregateRoot, Entity
from domain.value_objects import UUID
from domain.note.entities import Note
from domain.folder.value_objects import FolderName, FolderColor

# TODO
NoteId = int

class Folder(Entity):

    def __init__(
        self, entity_id: UUID, name: FolderName, color: FolderColor, parent: Optional[Folder] = None
    ) -> None:
        super().__init__(entity_id)

        self._name = name
        self._color = color

        self._parent_folder: Folder | None = None
        self._subfolders: list[Folder] = []
        self._notes: list[NoteId] = []

    def is_subfolder_of(self, other: Folder) -> bool:
        pass
    
    def add_subfolder(self, subfolder: Folder):
        subfolder.parent_folder = self
        self.subfolders.append(subfolder)

    def remove_subfolder(self, subfolder: Folder):
        self.subfolders.remove(subfolder)

    def put_note(self, note: Note):
        pass

    def remove_note(self, note: Note):
        pass

    def rename_folder(self, name: str):
        pass

    def change_folder_color(self, color: FolderColor):
        pass

    def delete_folder(self):
        pass

    def folder_has_no_notes(self):
        return bool(self._notes)
    
    def folder_has_no_subfolder(self):
        return bool(self._subfolders)


class FoldersTree(AggregateRoot):

    def __init__(self, entity_id: UUID) -> None:
        super().__init__(entity_id)

        self._folders: list[Folder] = []

    def add_folder(
        self, id: UUID, name: FolderName, color: FolderColor, parent: Optional[Folder] = None
    ) -> Folder:
        folder = Folder(entity_id=id, name=name, color=color, parent=parent)
        if parent is None:
            self._folders.append(folder)
        return folder

    def delete_folder(self, folder: Folder):
        # validation
        if folder in self._folders:
            self._folders.remove(folder)
        raise Exception('Folder is not present')

    def move_folder(self, folder: Folder, parent: Optional[Folder]):
        if folder.is_subfolder_of(parent):
            raise Exception('Folder is already here')
        
        if parent is None:
            pass
