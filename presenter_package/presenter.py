from model.service import Service
from view.abstract_ui import AbstractUI


class PresenterModule:
    def __init__(self, view: AbstractUI, service: Service):
        self.view = view
        self.service = service
        self.view.set_presenter(self)

    def create_text_note(self, head: str, body: str):
        self.service.create_text_note(head, body)

    def create_list_note(self, head: str, body: list):
        self.service.create_list_note(head, body)

    def get_list_notes(self) -> list:
        return self.service.get_list_notes()

    def get_list_on_date(self, start: str, end: str) -> list:
        return self.service.get_list_on_date(start, end)

    def save_storage(self, path: str):
        self.view.display(self.service.save_storage(path) + '\n')

    def load_storage(self, path: str):
        self.view.display(self.service.load_storage(path) + '\n')

    def print_note(self, id_note: str):
        self.view.display(self.service.get_note(id_note))

    def edit_note(self, id_note: str, head: str, body):
        self.view.display(self.service.edit_note(id_note, head, body) + '\n')

    def del_note(self, id_note: str):
        self.view.display(self.service.del_note(id_note) + '\n')

    def has_note(self, id_note: str) -> bool:
        return self.service.has_note(id_note)
