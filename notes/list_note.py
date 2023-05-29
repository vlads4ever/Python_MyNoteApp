import itertools
import time

from notes.abstract_note import AbstractNote


class ListNote(AbstractNote):
    id_iter = itertools.count()

    def __init__(self, header_note: str, body_note: list):
        self.id_note = next(self.id_iter)
        self.header_note = header_note
        self.body_note = body_note
        self.creation_time = time.strftime('%d.%m.%Y %H:%M')

    def get_header_note(self) -> str:
        return self.header_note

    def get_body_note(self) -> list:
        return self.body_note

    @staticmethod
    def get_for_print_body_note(item_list: list) -> str:
        output = ''
        for item in item_list:
            output += '* ' + item + '\n'
        return output

    def __str__(self) -> str:
        output = f'ID заметки: {self.id_note}\n'
        output += f'Дата заметки: {self.creation_time}\n'
        output += f'Заголовок: {self.header_note}\n'
        output += self.get_for_print_body_note(self.body_note)
        return output
