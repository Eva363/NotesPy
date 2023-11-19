
from view import UI
from model import Note

class Basic:
    """
    Класс Basic содержит метод инициализации списка заметок из json файла,
    запуска консольного пользовательского интерфейса
    и сохранения данных на диск по окончании работы программы
    """
    def start():
        t = Note("note.json")
        t.loadNote()
        UI(t).start()
        t.saveNote()

