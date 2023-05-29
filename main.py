from list_of_notes.list_of_notes import ListOfNotes
from notes.list_note import ListNote
from notes.text_note import TextNote

text_note = TextNote('Текстовая заметка', 'Первая заметка посвящена началу работы над проектом MyNoteApp.')
text_note_2 = TextNote('Текстовая заметка №2', 'Вторая заметка посвящена продолжению работы над проектом MyNoteApp.')
print(text_note)
print()
print(text_note_2)
print()

shoping_list = ["Молоко", "Мясо", "Сыр"]
list_note = ListNote('Список покупок', shoping_list)
print(list_note)
print()

list_of_notes = ListOfNotes()
list_of_notes.push_note_to_list(text_note)
list_of_notes.push_note_to_list(text_note_2)
list_of_notes.push_note_to_list(shoping_list)
print(list_of_notes.get_list_of_all_notes())
