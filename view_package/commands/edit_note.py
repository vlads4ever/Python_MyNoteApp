from view_package.commands.abstract_command import AbstractCommand
from view_package.abstract_ui import AbstractUI


class EditNote(AbstractCommand):
    def __init__(self, view: AbstractUI):
        self.view = view

    def get_description(self) -> str:
        return 'Редактировать заметку'

    def execute(self):
        self.view.edit_note()
