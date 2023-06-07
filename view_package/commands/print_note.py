from view_package.commands.abstract_command import AbstractCommand
from view_package.abstract_ui import AbstractUI


class PrintNote(AbstractCommand):
    def __init__(self, view: AbstractUI):
        self.view = view

    def get_description(self) -> str:
        return 'Вывести заметку'

    def execute(self):
        self.view.print_note()
