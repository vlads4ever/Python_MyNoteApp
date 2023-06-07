from view_package.commands.abstract_command import AbstractCommand
from view_package.abstract_ui import AbstractUI


class CreateListNote(AbstractCommand):
    def __init__(self, view: AbstractUI):
        self.view = view

    def get_description(self) -> str:
        return 'Создать заметку-список'

    def execute(self):
        self.view.create_list_note()
