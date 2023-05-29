from notes.abstract_note import AbstractNote


class ListOfNotes:
    def __init__(self):
        self.list_notes = list()

    def push_note_to_list(self, note: AbstractNote):
        self.list_notes.append(note)
