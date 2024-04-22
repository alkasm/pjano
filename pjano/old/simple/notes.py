from __future__ import annotations
from typing import Sequence


flat = "♭"
natural = "♮"
sharp = "♯"


class Note(str):
    @property
    def flat(self) -> Note:
        return Note(self + flat)

    @property
    def natural(self) -> Note:
        return Note(self + natural)

    @property
    def sharp(self) -> Note:
        return Note(self + sharp)


A = Note("A")
B = Note("B")
C = Note("C")
D = Note("D")
E = Note("E")
F = Note("F")
G = Note("G")
