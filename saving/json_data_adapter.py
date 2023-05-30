import json

from notes.list_note import ListNote


class JSONDataAdapter:
    @staticmethod
    def to_json(o):
        if isinstance(o, ListNote):
            return json.dumps({
                "id_note": o.id_note,
                "header_note": o.header_note,
                "body_note": o.body_note,
                "creation_time": o.creation_time
            }, indent=5, sort_keys=True)

    @staticmethod
    def from_json(o):
        o = json.loads(o)

        print(type(o.header_note))
        print(type(o.body_note))

        try:
            list_note = ListNote(o.header_note, o.body_note)
            return list_note
        except AttributeError:
            print("Неверная структура")
