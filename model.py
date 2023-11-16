
import json
#from view import Show, UserDialog, Show

class Note:
    """ Класс Note содержит поля: 
            nameNote - имя json файла
            dicNote - словарь для хранения заметок
            lenNote - максимальное значение ключа словаря
        Note содержит методы:
            loadNote - загрузка данных в словарь dicNote из файла, имя которого задано в поле nameNote
            newNote - добавление заметки
            deleteNote - удаление заметки
            updateNote - изменение заметки
    """
    def __init__(self, nameNote, dicNote={}, lenNote=0): 
        self.nameNote = nameNote
        self.dicNote = dicNote
        self.lenNote = lenNote

    def loadNote(self) -> dict():
        try:
            with open(self.nameNote, 'r') as f:
                self.dicNote = json.load(f)
        except FileNotFoundError:
            self.dicNote = {}

        if len(self.dicNote)>0:       
            self.lenNote = max(map(int, self.dicNote))
        else:
            self.lenNote = 0
        return self.dicNote

    def saveNote(self, reg='w'):
        with open(self.nameNote, reg) as f:
            json.dump(self.dicNote,f, indent=4)

    def newNote(self, t):
        self.lenNote += 1
        self.dicNote[str(self.lenNote)] = t

    def deleteNote(self, id):
        del self.dicNote[id]
    
    def updateNote(self, id, t):
        self.dicNote[id] = t
    

if __name__ == '__main__':
    # t = Note("note.json")
    # d = t.loadNote()
    # t.newNote(UserDialog.requestNoteData())
    # t.newNote(UserDialog.requestNoteData())
    # t.deleteNote('1')
    # t.updateNote('2', UserDialog.requestNoteData())
    # s = Show(d)
    # s.showNote()
    # t.saveNote()
    pass