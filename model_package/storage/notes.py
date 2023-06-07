import time

from model_package.notes.abstract_note import AbstractNote


class NotesStorage:
    def __init__(self):
        self.__notes = list()
        self.__index = 0

    def push(self, note: AbstractNote):
        self.__notes.append(note)

    def get_list(self) -> list:
        return self.__notes

    def get_list_on_date(self, start: str, end: str) -> list:
        start_date = time.strptime(start, '%d.%m.%Y %H:%M')
        end_date = time.strptime(end, '%d.%m.%Y %H:%M')
        filtered_list = list()
        for note in self.__notes:
            if start_date <= note.get_time() <= end_date:
                filtered_list.append(note)
        return filtered_list

    def get_note(self, id_note: str) -> str:
        output = ''
        for note in self.__notes:
            if id_note == note.get_id_note():
                output = note
                break
            else:
                output = 'Заметка не найдена.'
        return output

    def del_note(self, id_note: str) -> str:
        output = ''
        for i in reversed(range(len(self.__notes))):
            if id_note == self.__notes[i].get_id_note():
                output = f'Заметка "{self.__notes[i].get_id_note()}" удалена.'
                self.__notes.remove(self.__notes[i])
                break
            else:
                output = 'Заметка не найдена.'
        return output

    def edit_text_note(self, id_note: str, head: str, body: str) -> str:
        output = ''
        for note in self.__notes:
            if id_note == note.get_id_note():
                note.set_header(head)
                note.set_body(body)
                note.time_renew()
                output = 'Заметка изменена.'
                break
            else:
                output = 'Заметка не найдена.'
        return output

    def edit_list_note(self, id_note: str, head: str, body: list) -> str:
        output = ''
        for note in self.__notes:
            if id_note == note.get_id_note():
                note.set_header(head)
                note.set_body(body)
                note.time_renew()
                output = 'Заметка изменена.'
                break
            else:
                output = 'Заметка не найдена.'
        return output

    def has_note(self, id_note: str) -> bool:
        output = False
        for note in self.__notes:
            if id_note == note.get_id_note():
                output = True
                break
        return output

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index == len(self.__notes):
            raise StopIteration
        note = self.__notes[self.__index]
        self.__index += 1
        return note
