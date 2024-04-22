from __future__ import annotations
from dataclasses import dataclass
from types import SimpleNamespace
from typing import Sequence, TypeVar
from . import intervals, pitch, keys

T = TypeVar("T")


def _rotate_tuple(t: Sequence[T]) -> Sequence[T]:
    return tuple((*t[1:], t[0]))


class scale_intervals(SimpleNamespace):
    major = ionian = (
        intervals.unison,
        intervals.major_second,
        intervals.major_third,
        intervals.perfect_fourth,
        intervals.perfect_fifth,
        intervals.major_sixth,
        intervals.major_seventh,
    )
    dorian = _rotate_tuple(ionian)
    phrygian = _rotate_tuple(dorian)
    lydian = _rotate_tuple(phrygian)
    mixolydian = _rotate_tuple(lydian)
    natural_minor = minor = aeolian = _rotate_tuple(mixolydian)
    locrian = _rotate_tuple(aeolian)
    harmonic_minor = (
        intervals.unison,
        intervals.major_second,
        intervals.minor_third,
        intervals.perfect_fourth,
        intervals.perfect_fifth,
        intervals.minor_sixth,
        intervals.major_seventh,  # major 7th vs minor 7th of natural minor
    )


@dataclass
class Scale:
    root: pitch.PitchClass
    intervals: Sequence[intervals.Interval]


@dataclass
class ScaleInKey(Scale):
    key: keys.Key

    def __str__(self) -> str:
        return " ".join(
            str(s)
            for s in self.key.spell_pitch_classes(self.root + i for i in self.intervals)
        )


class DiatonicScale(Scale):
    @property
    def first(self) -> pitch.PitchClass:
        return self.root

    @property
    def second(self) -> pitch.PitchClass:
        return self.root + self.intervals[1]

    @property
    def third(self) -> pitch.PitchClass:
        return self.root + self.intervals[2]

    @property
    def fourth(self) -> pitch.PitchClass:
        return self.root + self.intervals[3]

    @property
    def fifth(self) -> pitch.PitchClass:
        return self.root + self.intervals[4]

    @property
    def sixth(self) -> pitch.PitchClass:
        return self.root + self.intervals[5]

    @property
    def seventh(self) -> pitch.PitchClass:
        return self.root + self.intervals[6]


@dataclass
class MajorScale(ScaleInKey, DiatonicScale):

    @classmethod
    def from_key(cls, root: pitch.PitchClass, key: keys.Key) -> MajorScale:
        return cls(root, scale_intervals.major, key)

    def fifth_up(self) -> MajorScale:
        """Go up the circle of fifths.

        Sharp the fourth, then play starting at the fifth.

        E.g. C.fifth_up() -> G:
            C  D  E  F  G  A  B    spelling in C
            0  2  4  5  7  9  11   pitch classes for C Maj
            G  A  B  C  D  E  F#   spelling in G
            7  9  11 0  2  4  6    pitch classes for G Maj

        """
        new_spelling = dict(self.key.spelling)
        fourth_spelling = new_spelling.pop(self.fourth)
        new_spelling[self.fourth + 1] = fourth_spelling.sharp()
        new_key = keys.Key(new_spelling)
        return MajorScale(self.root + intervals.perfect_fifth, self.intervals, new_key)

    def fifth_down(self) -> MajorScale:
        """Go down the circle of fifths.

        Flat the seventh, then play starting a fifth down.

        E.g. G.fifth_down() -> C:
            G  A  B  C  D  E  F#   spelling in G
            7  9  11 0  2  4  6    pitch classes for G Maj
            C  D  E  F  G  A  B    spelling in C
            0  2  4  5  7  9  11   pitch classes for C Maj
        """
        new_spelling = dict(self.key.spelling)
        seventh_spelling = new_spelling.pop(self.seventh)
        new_spelling[self.seventh - 1] = seventh_spelling.flat()
        new_key = keys.Key(new_spelling)
        return MajorScale(self.root - intervals.perfect_fifth, self.intervals, new_key)


class scales(SimpleNamespace):
    C = MajorScale.from_key(root=pitch.PitchClass.pc0, key=keys.keys.C)

    # sharp keys (fifths up from C)
    G = C.fifth_up()
    D = G.fifth_up()
    A = D.fifth_up()
    E = A.fifth_up()
    B = E.fifth_up()
    Fsharp = B.fifth_up()
    Csharp = Fsharp.fifth_up()

    # flat keys (fifths down from C)
    F = C.fifth_down()
    Bflat = F.fifth_down()
    Eflat = Bflat.fifth_down()
    Aflat = Eflat.fifth_down()
    Dflat = Aflat.fifth_down()
    Gflat = Dflat.fifth_down()
    Cflat = Gflat.fifth_down()
