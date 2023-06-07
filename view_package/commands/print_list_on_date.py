from view_package.commands.abstract_command import AbstractCommand
from view_package.abstract_ui import AbstractUI


class PrintListOnDate(AbstractCommand):
    def __init__(self, view: AbstractUI):
        self.view = view

    def get_description(self) -> str:
        return 'Вывести список заметок в интервале'

    def execute(self):
        self.view.print_list_on_date()