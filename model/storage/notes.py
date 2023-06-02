import time

from model.notes.abstract_note import AbstractNote


class NotesStorage:
    def __init__(self):
        self.notes = list()
        self.__index = 0

    def push(self, note: AbstractNote):
        self.notes.append(note)

    def get_list(self) -> list:
        return self.notes

    def get_list_on_date(self, start: str, end: str) -> list:
        start_date = time.strptime(start, '%d.%m.%Y %H:%M')
        end_date = time.strptime(end, '%d.%m.%Y %H:%M')
        filtered_list = list()
        for note in self.notes:
            if start_date <= note.get_time() <= end_date:
                filtered_list.append(note)
        return filtered_list

    def get_note(self, id_note: str) -> str:
        output = ''
        for note in self.notes:
            if id_note == note.id_note:
                output = note
                break
            else:
                output = 'Заметка не найдена.'
        return output

    def del_note(self, id_note: str) -> str:
        output = ''
        for i in reversed(range(len(self.notes))):
            if id_note == self.notes[i].id_note:
                output = f'Заметка "{self.notes[i].id_note}" удалена.'
                self.notes.remove(self.notes[i])
                break
            else:
                output = 'Заметка не найдена.'
        return output

    def edit_text_note(self, id_note: str, head: str, body: str) -> str:
        output = ''
        for note in self.notes:
            if id_note == note.id_note:
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
        for note in self.notes:
            if id_note == note.id_note:
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
        for note in self.notes:
            if id_note == note.id_note:
                output = True
                break
        return output

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index == len(self.notes):
            raise StopIteration
        note = self.notes[self.__index]
        self.__index += 1
        return note
