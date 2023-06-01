from model.notes.list_note import ListNote
from model.notes.text_note import TextNote
from model.saving.abstract_adapter import AbstractAdapter
from model.storage.notes import NotesStorage


class Service:
    def __init__(self, save_adapter: AbstractAdapter):
        self.notes = NotesStorage()
        self.save_adapter = save_adapter

    def create_text_note(self, head: str, body: str):
        text_note = TextNote(head, body)
        self.notes.push(text_note)

    def create_list_note(self, head: str, body: list):
        text_note = ListNote(head, body)
        self.notes.push(text_note)

    def get_list_notes(self) -> list:
        return self.notes.get_list()

    def get_list_on_date(self, start: str, end: str) -> list:
        return self.notes.get_list_on_date(start, end)

    def save_storage(self, path: str) -> str:
        self.save_adapter.save(self.notes, path)
        return 'Заметки сохранены в файл.'

    def load_storage(self, path: str) -> str:
        self.notes = self.save_adapter.load(path)
        return 'Заметки загружены из файла.'

    def get_note(self, id_note: str) -> str:
        return self.notes.get_note(id_note)

    def edit_note(self, id_note: str, head: str, body) -> str:
        return self.notes.edit_note(id_note, head, body)

    def del_note(self, id_note: str) -> str:
        return self.notes.del_note(id_note)

    def has_note(self, id_note: str) -> bool:
        return self.notes.has_note(id_note)
