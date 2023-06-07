from view_package.commands.abstract_command import AbstractCommand
from view_package.abstract_ui import AbstractUI


class DelNote(AbstractCommand):
    def __init__(self, view: AbstractUI):
        self.view = view

    def get_description(self) -> str:
        return 'Удалить заметку'

    def execute(self):
        self.view.del_note()
