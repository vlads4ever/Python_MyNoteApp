from abc import ABCMeta, abstractmethod


class AbstractUI(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def set_presenter(self, presenter):
        pass

    @abstractmethod
    def display(self, text: str):
        pass

    @abstractmethod
    def exit(self):
        pass

    def create_text_note(self):
        pass

    @abstractmethod
    def create_list_note(self):
        pass

    @abstractmethod
    def print_list_notes(self):
        pass

    @abstractmethod
    def print_list_on_date(self):
        pass

    @abstractmethod
    def save_storage(self):
        pass

    @abstractmethod
    def load_storage(self):
        pass

    @abstractmethod
    def print_note(self):
        pass

    @abstractmethod
    def edit_note(self):
        pass

    @abstractmethod
    def del_note(self):
        pass
