from model.saving.json_adapter import JSONAdapter
from model.service import Service
from presenter_package.presenter_module import PresenterModule
from view.console_ui import ConsoleUI

if __name__ == '__main__':
    # text_note = TextNote('Текстовая заметка №1', 'Первая заметка посвящена началу работы над проектом MyNoteApp.')
    # text_note_2 = TextNote('Текстовая заметка №2', 'Вторая заметка посвящена продолжению работы над проектом MyNoteApp.')
    # shoping_list = ["Молоко", "Мясо", "Сыр"]
    # list_note = ListNote('Список покупок №1', shoping_list)
    #
    # notes = NotesStorage()
    # notes.push(text_note)
    # notes.push(text_note_2)
    # notes.push(list_note)
    #
    # JSONAdapter.save(notes, "MyNotes.json")
    # new_notes = JSONAdapter.load("MyNotes.json")
    # print(new_notes.get_str_list())
    # print(new_notes.list_notes[0])

    # save_adapter = JSONAdapter()
    # service = Service(save_adapter)
    # shoping_list = ["Молоко", "Мясо", "Сыр"]
    # service.create_list_note('Список покупок №1', shoping_list)
    # service.create_text_note('Текстовая заметка №1', 'Первая заметка посвящена началу работы над проектом MyNoteApp.')
    # service.create_text_note('Текстовая заметка №2', 'Вторая заметка посвящена продолжению работы над проектом MyNoteApp.')
    # print(service.get_list_notes())
    # print(service.get_note('t_0'))
    # print(service.del_note('t_0'))
    # print(service.get_list_notes())
    # shoping_list = ["Морковь", "Томаты", "Цукини"]
    # service.edit_note('l_0', 'Список покупок №1', shoping_list)
    # print(service.get_note('l_0'))

    view = ConsoleUI()
    save_adapter = JSONAdapter()
    service = Service(save_adapter)
    presenter = PresenterModule(view, service)
    view.start()
