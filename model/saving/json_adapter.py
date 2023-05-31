import json

from model.notes.list_note import ListNote
from model.notes.text_note import TextNote
from model.saving.abstract_adapter import AbstractAdapter
from model.storage.notes import NotesStorage


class JSONAdapter(AbstractAdapter):
    @staticmethod
    def save(obj, path: str):
        with open(path, "w") as fw:
            if isinstance(obj, NotesStorage):
                json.dump([o.__dict__ for o in obj.notes], fw, indent=5, sort_keys=True)

    @staticmethod
    def load(path) -> NotesStorage:
        with open(path, "r") as fr:
            o = json.load(fr)
            try:
                notes = NotesStorage()
                for item in o:
                    if item['id_note'][0] == 'l':
                        note = ListNote(item['header_note'], item['body_note'])
                    elif item['id_note'][0] == 't':
                        note = TextNote(item['header_note'], item['body_note'])
                    notes.push(note)
                return notes
            except AttributeError:
                print("Wrong loadable structure.")
