import time


class Note:
    def __init__(self, header_note: str, body_note: str):
        self.header_note = header_note
        self.body_note = body_note
        self.creation_time = time.strftime('%d.%m.%Y %H:%M')

    def __str__(self):
        output = f'Дата заметки: {self.creation_time}\n'
        output += f'Заголовок: {self.header_note}\n'
        output += f'Тело заметки:\n{self.body_note}'
        return output
