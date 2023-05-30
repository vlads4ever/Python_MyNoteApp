import json

from notes.list_note import ListNote
from notes.text_note import TextNote
from storage.notes_storage import NotesStorage


class JSONDataAdapter:
    @staticmethod
    def to_json(o):
        with open("NyNotes.json", "w") as fw:
            if isinstance(o, NotesStorage):
                json.dump([o.__dict__ for o in o.list_notes], fw, indent=5, sort_keys=True)

    @staticmethod
    def from_json(fw):
        with open(fw, "r") as fr:
            o = json.load(fr)
            print(type(o))
            try:
                list_notes = NotesStorage()
                for item in o:
                    if item['id_note'][0] == 'l':
                        note = ListNote(item['header_note'], item['body_note'])
                    elif item['id_note'][0] == 't':
                        note = TextNote(item['header_note'], item['body_note'])
                    list_notes.push_to_storage(note)
                return list_notes
            except AttributeError:
                print("Неверная структура")
