from view_package.commands.abstract_command import AbstractCommand
from view_package.abstract_ui import AbstractUI


class LoadStorage(AbstractCommand):
    def __init__(self, view: AbstractUI):
        self.view = view

    def get_description(self) -> str:
        return 'Загрузить заметки из файла'

    def execute(self):
        self.view.load_storage()
