from notes.list_note import ListNote
from notes.text_note import TextNote

text_note = TextNote('Текстовая заметка', 'Первая заметка посвящена началу работы над проектом MyNoteApp.')
print(text_note)
print()

shoping_list = ["Молоко", "Мясо", "Сыр"]
list_note = ListNote('Список покупок', shoping_list)
print(list_note)
