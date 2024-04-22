from __future__ import annotations
from dataclasses import dataclass
from enum import Enum

from . import intervals, symbols


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
    def _to_int(other: PitchClass | intervals.Interval | int) -> int:
        if isinstance(other, PitchClass):
            return other.value
        elif isinstance(other, intervals.Interval):
            return other.semitones
        return other

    def __add__(self, other: PitchClass | intervals.Interval | int) -> PitchClass:
        return PitchClass((self.value + self._to_int(other)) % 12)

    def __sub__(self, other: PitchClass | intervals.Interval | int) -> PitchClass:
        return PitchClass((self.value - self._to_int(other)) % 12)



@dataclass
class Modifier:
    semitones: int

    def __str__(self) -> str:
        if self.semitones > 0:
            return symbols.sharp * self.semitones
        if self.semitones < 0:
            return symbols.flat * abs(self.semitones)
        return symbols.natural


FLAT = Modifier(-1)
NATURAL = Modifier(0)
SHARP = Modifier(+1)


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

    def __str__(self) -> str:
        if self.modifier is not None:
            return self.name + str(self.modifier)
        return self.name

    # TODO: enharmonic equivalence


"""
need to be able to "spell" pitch classes to spell a scale or chord

need a key signature to spell

major & minor scales have a natural key signature

sometimes multiple key signatures make sense for a specific piece of music
e.g. C Major ~ D Dorian but D Dorian may be annotated as D Major with accidentals in-situ
"""
