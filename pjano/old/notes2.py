from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from types import SimpleNamespace
from typing import Iterable, Mapping, Sequence, TypeVar

# ref: https://www.musicca.com/keys

T = TypeVar("T")


def _rotate_tuple(t: tuple[T, ...]) -> tuple[T, ...]:
    return tuple((*t[1:], t[0]))


@dataclass
class AbsolutePitch:
    frequency: float


@dataclass
class TwelveTETPitch(AbsolutePitch):
    REFERENCE_FREQUENCY = 440.0

    """Semitones relative to the reference frequency (A4)."""
    semitones: int

    @classmethod
    def from_semitones(cls, semitones: int) -> TwelveTETPitch:
        f = cls.REFERENCE_FREQUENCY * (2 ** (semitones / 12))
        return cls(frequency=f, semitones=semitones)


class PitchClass(Enum):
    pc0 = 0  # C
    pc1 = 1  # C♯/D♭
    pc2 = 2  # D
    pc3 = 3  # D♯/E♭
    pc4 = 4  # E
    pc5 = 5  # F
    pc6 = 6  # F♯/G♭
    pc7 = 7  # G
    pc8 = 8  # G♯/A♭
    pc9 = 9  # A
    pc10 = 10  # A♯/B♭
    pc11 = 11  # B

    @staticmethod
    def _to_int(other: PitchClass | Interval | int) -> int:
        if isinstance(other, PitchClass):
            return other.value
        elif isinstance(other, Interval):
            return other.semitones
        return other

    def __add__(self, other: PitchClass | Interval | int) -> PitchClass:
        return PitchClass((self.value + self._to_int(other)) % 12)

    def __sub__(self, other: PitchClass | Interval | int) -> PitchClass:
        return PitchClass((self.value - self._to_int(other)) % 12)


PC = [
    PitchClass.pc0,
    PitchClass.pc1,
    PitchClass.pc2,
    PitchClass.pc3,
    PitchClass.pc4,
    PitchClass.pc5,
    PitchClass.pc6,
    PitchClass.pc7,
    PitchClass.pc8,
    PitchClass.pc9,
    PitchClass.pc10,
    PitchClass.pc11,
]


class Symbols(SimpleNamespace):
    flat = "♭"
    natural = "♮"
    sharp = "♯"


@dataclass
class Modifier:
    semitones: int

    def __str__(self) -> str:
        if self.semitones > 0:
            return Symbols.sharp * self.semitones
        if self.semitones < 0:
            return Symbols.flat * abs(self.semitones)
        return Symbols.natural


FLAT = Modifier(-1)
NATURAL = Modifier(0)
SHARP = Modifier(+1)


@dataclass
class Interval:
    semitones: int


SemiTone = Interval(1)
WholeTone = Interval(2)


class ScaleIntervals(SimpleNamespace):
    major = ionian = (
        WholeTone,
        WholeTone,
        SemiTone,
        WholeTone,
        WholeTone,
        WholeTone,
        SemiTone,
    )
    dorian = _rotate_tuple(ionian)
    phrygian = _rotate_tuple(dorian)
    lydian = _rotate_tuple(phrygian)
    mixolydian = _rotate_tuple(lydian)
    minor = aeolian = _rotate_tuple(mixolydian)
    locrian = _rotate_tuple(aeolian)
    harmonic_minor = (
        WholeTone,
        SemiTone,
        WholeTone,
        WholeTone,
        WholeTone,
        WholeTone,
        SemiTone,
    )


@dataclass
class PitchSpelling:
    name: str
    modifier: Modifier | None = None

    def flat(self) -> PitchSpelling:
        if self.modifier is None:
            return PitchSpelling(self.name, FLAT)
        return PitchSpelling(self.name, Modifier(self.modifier.semitones - 1))

    def sharp(self) -> PitchSpelling:
        if self.modifier is None:
            return PitchSpelling(self.name, SHARP)
        return PitchSpelling(self.name, Modifier(self.modifier.semitones + 1))

    def natural(self) -> PitchSpelling:
        return PitchSpelling(self.name, NATURAL)

    def drop_modifiers(self) -> PitchSpelling:
        return PitchSpelling(self.name, None)

    # TODO: enharmonic equivalence
    # TODO: mapping pc <-> spelling


class pitch(SimpleNamespace):
    A = PitchSpelling("A")
    B = PitchSpelling("B")
    C = PitchSpelling("C")
    D = PitchSpelling("D")
    E = PitchSpelling("E")
    F = PitchSpelling("F")
    G = PitchSpelling("G")


@dataclass
class Scale:
    intervals: Sequence[Interval]
    spelling: Sequence[PitchSpelling]
    # TODO: enharmonic simplify (e.g. C# Major -> Db Major)


@dataclass
class Key:
    spelling: Sequence[tuple[PitchClass, PitchSpelling]]


"""
* "key" is a sequence of pitch classes and a specific spelling of those pitch classes
* "scale" is a sequence of pitch classes (within a key?)
* major keys are associated to each other via circle of fifths
* major keys are associated to their major scale
* major keys are associated to their modes
* major keys are associated to their relative minor (the Aeolian mode)
* major keys are associated to the chords within the key (e.g. I, V, IVm7, ...)
* chord classes are sets of pitch classes
* chords are sequences of pitches, spelled within a key
"""

"""
- scales are a sequence of pitch classes
- keys are how you spell a group of pitch classes
- keys (spellings) are related to each other by circle of fifths
    - scales, too
- scales can generate chord sequences
- maybe associate scales to notes? e.g. take A -> get A minor triad, A dom 7, etc.



things i'd like to do:

- computer tells me to play a Gdom7
- I play the notes of Gdom7 in any inversion, comp shows the inversion and gives me a check

- computer tells me a major/minor/mode scale, tells me to play the I, iv, II chord
- I play the notes in any inversion, comp shows the inversion and gives me a check

- computer tells me a scale, number of octaves for the scales, play singles or octave
- I play the notes in order, it gives me a check

- computer gives me a root note and a chord (visual or audio) and I tell it which chord it is (e.g. IV)


"""


class Key_:
    pitch_classes: Sequence[PitchClass]
    spelling: Sequence[PitchSpelling]

class Mode_(Key_):
    pass

class Modes_:
    ionian: Mode_
    dorian: Mode_
    phrygian: Mode_
    lydian: Mode_
    mixolydian: Mode_
    aeolian: Mode_
    locrian: Mode_


class MajorKey_(Key_):
    def fifth_up(self) -> Key_: ...
    def fifth_down(self) -> Key_: ...
    def scale(self) -> Scale: ...
    def relative_minor(self) -> Key_: ...
    def modes(self) -> Modes_: ...

class Scale:
    pitch_classes: Sequence[PitchClass]
    key: Key

class ChordClass_:  
    pitch_classes: set[PitchClass]

class Chord_:
    pitch_classes: Sequence[PitchClass]
    spelling: Sequence[PitchSpelling]

@dataclass
class MajorKey(Key):
    def fifth_up(self) -> MajorKey:
        """Go up the circle of fifths.

        Sharp the fourth, then play starting at the fifth.

        E.g. C.fifth_up() -> G:

            1 2 3 4 5 6 7
        G = G A B C D E F#
        C = C D E F G A B
        """
        pc4, sp4 = self.spelling[4]
        sharp_4 = (pc4 + 1, sp4.sharp())
        return MajorKey([*self.spelling[4:], *self.spelling[:3], sharp_4])

    def fifth_down(self) -> MajorKey:
        """Go down the circle of fifths.

        Flat the seventh, then play starting at the fourth.

        E.g. G.fifth_down() -> C:

            1 2 3 4 5 6 7
        G = G A B C D E F#
        C = C D E F G A B
        """

        pc7, sp7 = self.spelling[6]
        flat_7 = (pc7 - 1, sp7.flat())
        return MajorKey([*self.spelling[3:6], flat_7, *self.spelling[:3]])


C_Major_key = MajorKey(
    [
        (PC[0], pitch.C),
        (PC[2], pitch.D),
        (PC[4], pitch.E),
        (PC[5], pitch.F),
        (PC[7], pitch.G),
        (PC[9], pitch.A),
        (PC[11], pitch.B),
    ]
)


@dataclass
class MajorScale(Scale):
    intervals: Sequence[Interval] = ScaleIntervals.major

    def fifth_up(self) -> MajorScale:
        """Create a new scale by traversing the circle of fifths up a fifth."""
        # start at the fifth and wrap around, then sharp the seventh
        spelling = [*self.spelling[4:], *self.spelling[:4]]
        spelling.append(spelling.pop().sharp())
        return MajorScale(spelling=spelling)


C_Major = MajorScale(
    spelling=(pitch.C, pitch.D, pitch.E, pitch.F, pitch.G, pitch.A, pitch.B)
)
