from model_package.notes.list_note import ListNote
from model_package.notes.text_note import TextNote
from model_package.saving.abstract_adapter import AbstractAdapter
from model_package.storage.notes import NotesStorage


class Service:
    def __init__(self, save_adapter: AbstractAdapter):
        self.__notes = NotesStorage()
        self.__save_adapter = save_adapter

    def create_text_note(self, head: str, body: str):
        text_note = TextNote(head, body)
        self.__notes.push(text_note)

    def create_list_note(self, head: str, body: list):
        list_note = ListNote(head, body)
        self.__notes.push(list_note)

    def get_list_notes(self) -> list:
        return self.__notes.get_list()

    def get_list_on_date(self, start: str, end: str) -> list:
        return self.__notes.get_list_on_date(start, end)

    def save_storage(self, path: str) -> str:
        self.__save_adapter.save(self.__notes, path)
        return 'Заметки сохранены в файл.'

    def load_storage(self, path: str) -> str:
        self.__notes = self.__save_adapter.load(path)
        return 'Заметки загружены из файла.'

    def get_note(self, id_note: str) -> str:
        return self.__notes.get_note(id_note)

    def edit_text_note(self, id_note: str, head: str, body: str) -> str:
        return self.__notes.edit_text_note(id_note, head, body)

    def edit_list_note(self, id_note: str, head: str, body: list) -> str:
        return self.__notes.edit_list_note(id_note, head, body)

    def del_note(self, id_note: str) -> str:
        return self.__notes.del_note(id_note)

    def has_note(self, id_note: str) -> bool:
        return self.__notes.has_note(id_note)
