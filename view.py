
# import keyboard
from model import Note
    
class UserDialog:
    def __init__(self, message) -> None:
        print(message)

    def requestNoteData(msg='Новая заметка', title='', note='') -> dict():
        print(msg)
        title = input('Заголовок: ')
        note = input('Текст заметки: ') 
        return {'title':title, 'note':note}

class Show:
    def __init__(self, dicNote) -> None:
        self.dicNote = dicNote
    def showNote(self, filterData='') -> None:
        for key, value in (self.dicNote).items():        
            print(f'{key} {value["title"]} {value["note"]}')


class UI:
    def start() -> None:
       pass
