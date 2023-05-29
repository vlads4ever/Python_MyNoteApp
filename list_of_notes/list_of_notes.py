from notes.abstract_note import AbstractNote


class ListOfNotes:
    def __init__(self):
        self.list_notes = list()

    def push_note_to_list(self, note: AbstractNote):
        self.list_notes.append(note)

    def get_list_of_all_notes(self):
        output = ''
        if len(self.list_notes) > 0:
            for item in self.list_notes:
                output += item.note.__str__() + '\n'
        else:
            output += 'Записи отсутствуют'
        return output

