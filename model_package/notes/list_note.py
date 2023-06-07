import itertools
import time

from model_package.notes.abstract_note import AbstractNote


class ListNote(AbstractNote):
    id_iter = itertools.count()

    def __init__(self, header_note: str, body_note: list, provided_time=None):
        self.__id_note = 'l_' + str(next(self.id_iter))
        self.__header_note = header_note
        self.__body_note = body_note
        if provided_time is None:
            self.__creation_time = time.strftime('%d.%m.%Y %H:%M')
        else:
            self.__creation_time = provided_time

    def get_id_note(self) -> str:
        return self.__id_note

    def get_header(self) -> str:
        return self.__header_note

    def get_body(self) -> list:
        return self.__body_note

    def get_creation_time(self) -> str:
        return self.__creation_time

    def get_time(self) -> time.struct_time:
        return time.strptime(self.__creation_time, '%d.%m.%Y %H:%M')

    def set_header(self, header_note: str):
        self.__header_note = header_note

    def set_body(self, body_note: list):
        self.__body_note = body_note

    def time_renew(self):
        self.__creation_time = time.strftime('%d.%m.%Y %H:%M')

    @staticmethod
    def body_to_str(item_list: list) -> str:
        output = ''
        for item in item_list:
            output += '* ' + item + '\n'
        return output

    def __str__(self) -> str:
        output = f'ID заметки: {self.__id_note}\n'
        output += f'Дата заметки: {self.__creation_time}\n'
        output += f'Заголовок: {self.__header_note}\n'
        output += self.body_to_str(self.__body_note)
        return output

    def __repr__(self) -> str:
        return f'<id_note: {self.__id_note}>' \
               f'<header_note: {self.__header_note}>' \
               f'<body_note: {self.__body_note}>' \
               f'<creation_time: {self.__creation_time}>'
