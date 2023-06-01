from view.commands.create_list_note import CreateListNote
from view.commands.create_text_note import CreateTextNote
from view.commands.del_note import DelNote
from view.commands.edit_note import EditNote
from view.commands.exit import Exit
from view.commands.load_storage import LoadStorage
from view.commands.print_list_notes import PrintListNotes
from view.commands.print_note import PrintNote
from view.commands.save_storage import SaveStorage
from view.abstract_ui import AbstractUI


class MainMenu:
    def __init__(self, view: AbstractUI):
        self.view = view
        self.command_list = list()
        self.command_list.append(Exit(self.view))
        self.command_list.append(CreateTextNote(self.view))
        self.command_list.append(CreateListNote(self.view))
        self.command_list.append(PrintNote(self.view))
        self.command_list.append(EditNote(self.view))
        self.command_list.append(DelNote(self.view))
        self.command_list.append(PrintListNotes(self.view))
        self.command_list.append(SaveStorage(self.view))
        self.command_list.append(LoadStorage(self.view))

    def print(self) -> str:
        output = ''
        output += '~~~~~~~~~~~~~~~~Меню:~~~~~~~~~~~~~~~~' + '\n'
        for i in range(len(self.command_list)):
            output += str(i+1) + ': ' + self.command_list[i].get_description() + '\n'
        output += '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + '\n'
        return output

    def execute(self, num_command: int):
        self.command_list[num_command-1].execute()

    def size(self) -> int:
        return len(self.command_list)
