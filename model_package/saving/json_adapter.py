import json

from model_package.notes.list_note import ListNote
from model_package.notes.text_note import TextNote
from model_package.saving.abstract_adapter import AbstractAdapter
from model_package.storage.notes import NotesStorage


class JSONAdapter(AbstractAdapter):
    @staticmethod
    def save(obj, path: str):
        with open(path, "w") as fw:
            if isinstance(obj, NotesStorage):
                json.dump([o.__dict__ for o in obj.get_list()], fw, indent=5, sort_keys=True)

    @staticmethod
    def load(path) -> NotesStorage:
        with open(path, "r") as fr:
            o = json.load(fr)
            try:
                notes = NotesStorage()
                for item in o:
                    if item.__contains__('_ListNote__id_note'):
                        note = ListNote(item['_ListNote__header_note'],
                                        item['_ListNote__body_note'],
                                        item['_ListNote__creation_time'])
                    elif item.__contains__('_TextNote__id_note'):
                        note = TextNote(item['_TextNote__header_note'],
                                        item['_TextNote__body_note'],
                                        item['_TextNote__creation_time'])
                    notes.push(note)
                return notes
            except AttributeError:
                print("Wrong loadable structure.")
