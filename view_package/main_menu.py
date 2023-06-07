from view_package.commands.create_list_note import CreateListNote
from view_package.commands.create_text_note import CreateTextNote
from view_package.commands.del_note import DelNote
from view_package.commands.edit_note import EditNote
from view_package.commands.exit import Exit
from view_package.commands.load_storage import LoadStorage
from view_package.commands.print_list_notes import PrintListNotes
from view_package.commands.print_list_on_date import PrintListOnDate
from view_package.commands.print_note import PrintNote
from view_package.commands.save_storage import SaveStorage
from view_package.abstract_ui import AbstractUI


class MainMenu:
    def __init__(self, view: AbstractUI):
        self.__view = view
        self.__command_list = list()
        self.__command_list.append(Exit(self.__view))
        self.__command_list.append(CreateTextNote(self.__view))
        self.__command_list.append(CreateListNote(self.__view))
        self.__command_list.append(PrintListNotes(self.__view))
        self.__command_list.append(PrintListOnDate(self.__view))
        self.__command_list.append(PrintNote(self.__view))
        self.__command_list.append(EditNote(self.__view))
        self.__command_list.append(DelNote(self.__view))
        self.__command_list.append(SaveStorage(self.__view))
        self.__command_list.append(LoadStorage(self.__view))

    def print(self) -> str:
        output = ''
        output += '~~~~~~~~~~~~~~~~Меню:~~~~~~~~~~~~~~~~' + '\n'
        for i in range(len(self.__command_list)):
            output += str(i+1) + ': ' + self.__command_list[i].get_description() + '\n'
        output += '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + '\n'
        return output

    def execute(self, num_command: int):
        self.__command_list[num_command - 1].execute()

    def size(self) -> int:
        return len(self.__command_list)
