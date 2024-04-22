from __future__ import annotations
from dataclasses import dataclass
from types import SimpleNamespace
from typing import Iterable, Mapping

from . import pitch


@dataclass
class Key:
    spelling: Mapping[pitch.PitchClass, pitch.PitchSpelling]

    def spell_pitch_classes(
        self, pitch_classes: Iterable[pitch.PitchClass]
    ) -> Iterable[pitch.PitchSpelling]:
        for pc in pitch_classes:
            yield self.spelling[pc]

    def __str__(self) -> str:
        return " ".join(str(s) for s in self.spelling.values())


class keys(SimpleNamespace):
    C = Key(
        spelling={
            pitch.PitchClass.pc0: pitch.PitchSpelling("C"),
            pitch.PitchClass.pc2: pitch.PitchSpelling("D"),
            pitch.PitchClass.pc4: pitch.PitchSpelling("E"),
            pitch.PitchClass.pc5: pitch.PitchSpelling("F"),
            pitch.PitchClass.pc7: pitch.PitchSpelling("G"),
            pitch.PitchClass.pc9: pitch.PitchSpelling("A"),
            pitch.PitchClass.pc11: pitch.PitchSpelling("B"),
        }
    )
