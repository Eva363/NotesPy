
import keyboard
from model import Note
    
class UserDialog:
    """
    Абстрактный класс UserDialog содержит методы для запроса данных от пользователя
    Метод requestNoteData - служит для ввода заголовка и текста заметки
    Метод requestNoteId - служит для ввода идентификатора заметки
    """
    # def __init__(self, message) -> None:
    #     print(message)

    def requestNoteData(msg='Новая заметка', title='', note='') -> dict():
        print(msg)
        keyboard.write(title)
        title = input('Заголовок: ')
        keyboard.write(note)
        note = input('Текст заметки: ') 
        return {'title':title, 'note':note}
    
    def requestNoteId(note) -> str:
        id = input('Идентификатор заметки: ')
        if id in note.getDicNote():
            return id 
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

    def showNote(self, filterData='') -> None:
        for key, value in self.note.getDicNote().items():        
            print(f'{key} {value["title"]} {value["note"]}')

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
                    self.showNote()
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
                                        
        