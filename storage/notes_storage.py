from notes.abstract_note import AbstractNote


class NotesStorage:
    def __init__(self):
        self.list_notes = list()

    def push_to_storage(self, note: AbstractNote):
        self.list_notes.append(note)

    def get_str_list(self):
        output = ''
        if len(self.list_notes) > 0:
            for item in self.list_notes:
                output += str(item.id_note) + ': ' + item.header_note + '\n'
        else:
            output += 'Записи отсутствуют'
        return output

