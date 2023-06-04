import time

from presenter_package.presenter import PresenterModule
from view.abstract_ui import AbstractUI
from view.main_menu import MainMenu


class ConsoleUI(AbstractUI):
    __WRONG_VALUE = 'Введено некорректное значение'

    def __init__(self):
        self.__run = True
        self.__main_menu = MainMenu(self)
        self.__presenter = None

    def welcome(self):
        self.display('Добро пожаловать в MyNoteApp!')
        self.display('*****************************' + '\n')
        self.display('Вы можете загрузить базу MyNotes.json.' + '\n')

    def start(self):
        self.welcome()
        while self.__run:
            self.print_menu()
            self.execute()

    def set_presenter(self, presenter: PresenterModule):
        self.__presenter = presenter

    def display(self, text: str):
        print(text)

    def print_menu(self):
        self.display(self.__main_menu.print())

    def execute(self):
        user_input = input('Введите номер команды > ')
        if self.is_int(user_input):
            num_command = int(user_input)
            if self.check_command(num_command):
                self.display('-------------------------------------' + '\n')
                self.__main_menu.execute(num_command)

    def is_int(self, value) -> bool:
        if value is None:
            self.display(self.__WRONG_VALUE + '\n')
            return False
        try:
            int(value)
            return True
        except ValueError:
            self.display(self.__WRONG_VALUE + '\n')
            return False

    def check_command(self, num_command) -> bool:
        if num_command > self.__main_menu.size() or num_command < 1:
            self.display(self.__WRONG_VALUE + '\n')
            return False
        return True

    def exit(self):
        self.__run = False
        self.display('Завершение работы.')

    def create_text_note(self):
        self.display('Создание текстовой заметки...')
        head = input('Введите тему > ')
        body = input('Введите содержание > ')
        self.__presenter.create_text_note(head, body)
        self.display('Заметка создана' + '\n')

    def create_list_note(self):
        self.display('Создание заметки-списка...')
        head = input('Введите тему > ')
        user_list = input('Введите элементы списка (через запятую) > ')
        body = user_list.split(',')
        self.__presenter.create_list_note(head, body)
        self.display('Заметка создана' + '\n')

    def print_list_notes(self):
        notes = self.__presenter.get_list_notes()
        output = 'Список заметок:' + '\n' + 'ID    Дата заметки:        Тема:' + '\n'
        if len(notes) > 0:
            for item in notes:
                output += str(item.get_id_note()) + ': ' + '(' + \
                          item.get_creation_time() + ') -> ' + \
                          item.get_header() + '\n'
        else:
            output += 'Записи отсутствуют'
        self.display(output + '\n')

    def print_list_on_date(self):
        self.display('Задание диапазона дат...')
        start = input('Введите начало диапазона (д.м.г Ч:М) > ')
        end = input('Введите конец диапазона (д.м.г Ч:М) > ')
        if self.is_date(start) and self.is_date(end):
            notes = self.__presenter.get_list_on_date(start, end)
            output = f'Список заметок в интервале с {start} по {end} :' + \
                     '\n' + 'ID    Дата заметки:        Тема:' + '\n'
            if len(notes) > 0:
                for item in notes:
                    output += str(item.get_id_note()) + ': ' + '(' + \
                              item.get_creation_time() + ') -> ' + \
                              item.get_header() + '\n'
            else:
                output += 'Записи отсутствуют' + '\n'
            self.display(output + '\n')
        else:
            self.display(self.__WRONG_VALUE + '\n')

    def is_date(self, date: str) -> bool:
        if date is None:
            self.display(self.__WRONG_VALUE + '\n')
            return False
        try:
            time.strptime(date, '%d.%m.%Y %H:%M')
            return True
        except ValueError:
            self.display(self.__WRONG_VALUE + '\n')
            return False

    def save_storage(self):
        self.display('Сохранение заметок...')
        path = input('Введите название файла (без расширения) > ')
        path += '.json'
        self.__presenter.save_storage(path)

    def load_storage(self):
        self.display('Загрузка заметок...')
        path = input('Введите название файла (без расширения) > ')
        path += '.json'
        self.__presenter.load_storage(path)

    def print_note(self):
        id_note = input('Введите ID заметки > ')
        self.display('')
        self.__presenter.print_note(id_note)
        self.display('')

    def edit_note(self):
        self.display('Редактирование заметки...')
        id_note = input('Введите ID заметки > ')
        self.display('')
        if self.__presenter.has_note(id_note):
            self.__presenter.print_note(id_note)
            self.display('\n' + 'Редактируем заметку...')
            if id_note[0] == 't':
                head = input('Введите тему > ')
                body = input('Введите содержание > ')
                self.__presenter.edit_text_note(id_note, head, body)
                self.display('')
            else:
                head = input('Введите тему > ')
                user_list = input('Введите элементы списка (через запятую) > ')
                body = user_list.split(',')
                self.__presenter.edit_list_note(id_note, head, body)
                self.display('')
        else:
            self.display('Заметка не найдена.' + '\n')

    def del_note(self):
        self.display('Удаление заметки...')
        id_note = input('Введите ID заметки > ')
        self.__presenter.del_note(id_note)
        self.display('')
