from model.notes.abstract_note import AbstractNote


class NotesStorage:
    def __init__(self):
        self.notes = list()
        self.__index = 0

    def push(self, note: AbstractNote):
        self.notes.append(note)

    def get_str_list(self):
        output = 'Список заметок:' + '\n' + 'ID    Дата заметки:        Тема:' + '\n'
        if len(self.notes) > 0:
            for item in self.notes:
                output += str(item.id_note) + ': ' + '(' + \
                          item.creation_time + ') -> ' + \
                          item.header_note + '\n'
        else:
            output += 'Записи отсутствуют'
        return output

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

    def edit_note(self, id_note: str, head: str, body) -> str:
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
