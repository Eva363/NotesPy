from view import UI, Show, UserDialog
from model import Note

class Basic:
    def start():
        # UI()
        t = Note("note.json")
        d = t.loadNote()
        t.newNote(UserDialog.requestNoteData())
        t.newNote(UserDialog.requestNoteData())
        #t.deleteNote('1')
        t.updateNote('2', UserDialog.requestNoteData("Изменение заметки"))
        s = Show(d)
        s.showNote()
        t.saveNote() 
    