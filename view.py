
import keyboard
from datetime import datetime
from model import Note
    
class UserDialog:
    """
    Класс UserDialog содержит методы для запроса данных от пользователя
    Метод requestNoteData - служит для ввода заголовка и текста заметки
    Метод requestNoteId - служит для ввода идентификатора заметки
    """

    def requestNoteData(msg='Новая заметка', title='', note='') -> dict():
        print(msg)
        keyboard.write(title)
        title = input('Заголовок: ')
        keyboard.write(note)
        note = input('Текст заметки: ') 
        return {'title':title, 'note':note, 'datetime_modify':datetime.now().strftime("%d.%m.%Y %H:%M:%S")}
    
    def requestNoteId(note) -> str:
        id = input('Идентификатор заметки: ')
        if id in note.getDicNote():
            return id 
        else:
            print("Заметка не найдена")
            return None
    def requestNoteDate() -> str:
        date_str = input('Введите дату в формате дд.мм.гггг: ')
        try:
            datetime.strptime(date_str, '%d/%m/%Y')
            return date_str
        except ValueError: 
            print('Неверный формат даты!')
            return ''
        else:
            print("Заметка не найдена")
            return None
class UI:
    """
    Класс UI описывает пользовательский интерфейс консольного ввода команд управления заметками
    Метод showNote служит для вывода списка заметок
    Метод start служит для циклического ввода команд
    """
    def __init__(self, note) -> None:
        self.note = note

    def showNote(self, date_filter='') -> None:
        print('\nСписок заметок:')
        for key, value in self.note.getDicNote().items():
            if date_filter in value['datetime_modify']:        
                print(f"{key} {value['datetime_modify']} {value['title']} {value['note']}")

    def start(self) -> None:
        print("\n" + "-"*50 +"\nПриложение Notes - Заметки\n" + "-"*50)
        while True:
            print("\nИспользуйте команды add, delete, update, list, quit")
            command = input("\n> ")
            print()
            match command:
                case 'quit':
                    input("Завершено")
                    break
                case 'list':
                    self.showNote(UserDialog.requestNoteDate())
                case 'add':
                    self.note.newNote(UserDialog.requestNoteData())
                case 'update':
                    noteId = UserDialog.requestNoteId(self.note)
                    if noteId:
                        dicUpdNote = self.note.getNote(noteId)
                        self.note.updateNote(
                            noteId, 
                            UserDialog.requestNoteData(
                                "Изменение заметки"
                                , dicUpdNote["title"]
                                , dicUpdNote["note"]
                            )
                        )
                case 'delete':
                    noteId = UserDialog.requestNoteId(self.note)
                    if noteId:
                        self.note.deleteNote(noteId)
                case '':
                    continue
                case _:
                    print("Неизвестная команда")
                                        
        