import cmd
from .notes import *

PROMPT = "🎹 "

_homerow_char_to_note = {
    "a": OctaveNaiveNote(WholeNote.C, None),
    "w": OctaveNaiveNote(WholeNote.D, FLAT),
    "s": OctaveNaiveNote(WholeNote.D, None),
    "e": OctaveNaiveNote(WholeNote.E, FLAT),
    "d": OctaveNaiveNote(WholeNote.E, None),
    "f": OctaveNaiveNote(WholeNote.F, None),
    "t": OctaveNaiveNote(WholeNote.G, FLAT),
    "g": OctaveNaiveNote(WholeNote.G, None),
    "y": OctaveNaiveNote(WholeNote.A, FLAT),
    "h": OctaveNaiveNote(WholeNote.A, None),
    "u": OctaveNaiveNote(WholeNote.B, FLAT),
    "j": OctaveNaiveNote(WholeNote.B, None),
    "k": OctaveNaiveNote(WholeNote.C, None),
    "o": OctaveNaiveNote(WholeNote.D, FLAT),
    "l": OctaveNaiveNote(WholeNote.D, None),
    "p": OctaveNaiveNote(WholeNote.E, FLAT),
    ";": OctaveNaiveNote(WholeNote.E, None),
    "'": OctaveNaiveNote(WholeNote.F, None),
}
        

class PjanoInterpreter(cmd.Cmd):
    prompt = PROMPT
    def do_chord(self, line: str):
        print(line)

    def do_note(self, line: str):
        note = Note.from_str(line)
        print(note)

    def do_keyboard(self, line: str):
        for c in line:
            note = _homerow_char_to_note.get(c, "?")
            print(note, end=" ")
        print()

    def run(self):
        return self.cmdloop()
        
pjano = PjanoInterpreter()