from model_package.service import Service
from view_package.abstract_ui import AbstractUI


class PresenterModule:
    def __init__(self, view: AbstractUI, service: Service):
        self.__view = view
        self.__service = service
        self.__view.set_presenter(self)

    def create_text_note(self, head: str, body: str):
        self.__service.create_text_note(head, body)

    def create_list_note(self, head: str, body: list):
        self.__service.create_list_note(head, body)

    def get_list_notes(self) -> list:
        return self.__service.get_list_notes()

    def get_list_on_date(self, start: str, end: str) -> list:
        return self.__service.get_list_on_date(start, end)

    def save_storage(self, path: str):
        self.__view.display(self.__service.save_storage(path) + '\n')

    def load_storage(self, path: str):
        self.__view.display(self.__service.load_storage(path) + '\n')

    def print_note(self, id_note: str):
        self.__view.display(self.__service.get_note(id_note))

    def edit_text_note(self, id_note: str, head: str, body: str):
        self.__view.display(self.__service.edit_text_note(id_note, head, body) + '\n')

    def edit_list_note(self, id_note: str, head: str, body: list):
        self.__view.display(self.__service.edit_list_note(id_note, head, body) + '\n')

    def del_note(self, id_note: str):
        self.__view.display(self.__service.del_note(id_note) + '\n')

    def has_note(self, id_note: str) -> bool:
        return self.__service.has_note(id_note)
