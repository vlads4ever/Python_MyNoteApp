import itertools
import time

from model.notes.abstract_note import AbstractNote


class TextNote(AbstractNote):
    id_iter = itertools.count()

    def __init__(self, header_note: str, body_note: str):
        self.id_note = 't_' + str(next(self.id_iter))
        self.header_note = header_note
        self.body_note = body_note
        self.creation_time = time.strftime('%d.%m.%Y %H:%M')

    def get_header(self) -> str:
        return self.header_note

    def get_body(self) -> str:
        return self.body_note

    def set_header(self, header_note: str):
        self.header_note = header_note

    def set_body(self, body_note: str):
        self.body_note = body_note

    def time_renew(self):
        self.creation_time = time.strftime('%d.%m.%Y %H:%M')

    def __str__(self) -> str:
        output = f'ID заметки: {self.id_note}\n'
        output += f'Дата заметки: {self.creation_time}\n'
        output += f'Заголовок: {self.header_note}\n'
        output += f'Тело заметки:\n{self.body_note}'
        return output

    def __repr__(self) -> str:
        return f'<id_note: {self.id_note}>' \
               f'<header_note: {self.header_note}>' \
               f'<body_note: {self.body_note}>' \
               f'<creation_time: {self.creation_time}>'
