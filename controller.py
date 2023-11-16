
from view import UI
from model import Note

class Basic:
    def start():
        t = Note("note.json")
        t.loadNote()
        UI(t).start()
        t.saveNote()
