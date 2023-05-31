from view.commands.abstract_command import AbstractCommand
from view.abstract_ui import AbstractUI


class Exit(AbstractCommand):
    def __init__(self, view: AbstractUI):
        self.view = view

    def get_description(self) -> str:
        return 'Выход'

    def execute(self):
        self.view.exit()