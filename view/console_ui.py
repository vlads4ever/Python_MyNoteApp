from presenter_package.presenter_module import PresenterModule
from view.abstract_ui import AbstractUI
from view.main_menu import MainMenu


class ConsoleUI(AbstractUI):
    WRONG_VALUE = 'Введено некорректное значение'

    def __init__(self):
        self.run = True
        self.main_menu = MainMenu(self)
        self.presenter = None

    def welcome(self):
        self.display('Добро пожаловать в MyNoteApp!')
        self.display('*****************************' + '\n')
        self.display('Вы можете загрузить базу MyNotes.json.' + '\n')

    def start(self):
        self.welcome()
        while self.run:
            self.print_menu()
            self.execute()

    def set_presenter(self, presenter: PresenterModule):
        self.presenter = presenter

    def display(self, text: str):
        print(text)

    def print_menu(self):
        self.display(self.main_menu.print())

    def execute(self):
        user_input = input('Введите номер команды > ')
        if self.is_int(user_input):
            num_command = int(user_input)
            if self.check_command(num_command):
                self.display('-------------------------------------' + '\n')
                self.main_menu.execute(num_command)

    def is_int(self, value) -> bool:
        if value is None:
            self.display(self.WRONG_VALUE)
            return False
        try:
            int(value)
            return True
        except ValueError:
            self.display(self.WRONG_VALUE)
            return False

    def check_command(self, num_command) -> bool:
        if num_command > self.main_menu.size():
            self.display(self.WRONG_VALUE)
            return False
        return True

    def exit(self):
        self.run = False
        self.display('Завершение работы.')

    def create_text_note(self):
        self.display('Создание текстовой заметки...')
        head = input('Введите тему > ')
        body = input('Введите содержание > ')
        self.presenter.create_text_note(head, body)
        self.display('Заметка создана')

    def create_list_note(self):
        self.display('Создание заметки-списка...')
        head = input('Введите тему > ')
        user_list = input('Введите элементы списка (через запятую) > ')
        body = user_list.split(',')
        self.presenter.create_list_note(head, body)
        self.display('Заметка создана')

    def print_list_notes(self):
        self.presenter.print_list_notes()

    def save_storage(self):
        self.display('Сохранение заметок...')
        path = input('Введите название файла (без расширения) > ')
        path += '.json'
        self.presenter.save_storage(path)

    def load_storage(self):
        self.display('Загрузка заметок...')
        path = input('Введите название файла (без расширения) > ')
        path += '.json'
        self.presenter.load_storage(path)

    def print_note(self):
        id_note = input('Введите ID заметки > ')
        self.presenter.print_note(id_note)

    def edit_note(self):
        self.display('Редактирование заметки...')
        id_note = input('Введите ID заметки > ')
        if self.presenter.has_note(id_note):
            self.presenter.print_note(id_note)
            self.display('Редактируем заметку...')
            if id_note[0] == 't':
                head = input('Введите тему > ')
                body = input('Введите содержание > ')
            else:
                head = input('Введите тему > ')
                user_list = input('Введите элементы списка (через запятую) > ')
                body = user_list.split(',')
            self.presenter.edit_note(id_note, head, body)
        else:
            self.display('Заметка не найдена.')

    def del_note(self):
        self.display('Удаление заметки...')
        id_note = input('Введите ID заметки > ')
        self.presenter.del_note(id_note)
