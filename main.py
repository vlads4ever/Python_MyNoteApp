from saving.json_data_adapter import JSONDataAdapter
from storage.notes_storage import NotesStorage
from notes.list_note import ListNote
from notes.text_note import TextNote

if __name__ == '__main__':
    # text_note = TextNote('Текстовая заметка №1', 'Первая заметка посвящена началу работы над проектом MyNoteApp.')
    # text_note_2 = TextNote('Текстовая заметка №2', 'Вторая заметка посвящена продолжению работы над проектом MyNoteApp.')
    #
    # shoping_list = ["Молоко", "Мясо", "Сыр"]
    # list_note = ListNote('Список покупок №1', shoping_list)
    #
    # notes = NotesStorage()
    # notes.push_to_storage(text_note)
    # notes.push_to_storage(text_note_2)
    # notes.push_to_storage(list_note)




    # JSONDataAdapter.to_json(notes)
    new_notes = JSONDataAdapter.from_json("NyNotes.json")
    print(new_notes.get_str_list())

