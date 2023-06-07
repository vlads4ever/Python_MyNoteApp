from view_package.commands.abstract_command import AbstractCommand
from view_package.abstract_ui import AbstractUI


class CreateTextNote(AbstractCommand):
    def __init__(self, view: AbstractUI):
        self.view = view

    def get_description(self) -> str:
        return 'Создать текстовую заметку'

    def execute(self):
        self.view.create_text_note()
