from __future__ import annotations
from dataclasses import dataclass
from types import SimpleNamespace
from enum import Enum


class Symbols(SimpleNamespace):
    flat = "♭"
    natural = "♮"
    sharp = "♯"


@dataclass
class Modifier:
    semitones: int

    def flat(self) -> Modifier:
        return Modifier(self.semitones - 1)

    def sharp(self) -> Modifier:
        return Modifier(self.semitones + 1)

    def natural(self) -> Modifier:
        return NATURAL
    
    def __str__(self) -> str:
        if self.semitones > 0:
            return Symbols.sharp * self.semitones
        return Symbols.flat * abs(self.semitones)


FLAT = Modifier(-1)
NATURAL = Modifier(0)
SHARP = Modifier(+1)


@dataclass
class AbsolutePitch:
    frequency: float

@dataclass
class TwelveTETPitch(AbsolutePitch):
    _REFERENCE_FREQUENCY = 440.0
    _REFERENCE_SEMITONES_ABOVE_C4 = 9

    """Semitones relative to the reference frequency (A4)."""
    semitones: int
    
    def semitones_above_c4(self) -> int:
        return self.semitones + self._REFERENCE_SEMITONES_ABOVE_C4

    @classmethod
    def from_semitones(cls, semitones: int) -> TwelveTETPitch:
        f = cls._REFERENCE_FREQUENCY * (2 ** (semitones/12))
        return cls(frequency=f, semitones=semitones)

    @classmethod
    def from_semitones_above_c4(cls, semitones: int) -> TwelveTETPitch:
        semitones_above_ref = semitones - cls._REFERENCE_SEMITONES_ABOVE_C4
        return cls.from_semitones(semitones_above_ref)

class NoteName(str, Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"

def _count_flats(s: str) -> int:
    return s.count("b") + s.count("flat") + s.count(Symbols.flat)

def _count_sharps(s: str) -> int:
    return s.count("#") + s.count("sharp") + s.count(Symbols.sharp)

def _contains_natural(s: str) -> int:
    return "nat" in s or Symbols.natural in s


class PitchClass(Enum):
    pc0 = 0
    pc1 = 1
    pc2 = 2
    pc3 = 3
    pc4 = 4
    pc5 = 5
    pc6 = 6
    pc7 = 7
    pc8 = 8
    pc9 = 9
    pc10 = 10
    pc11 = 11

@dataclasse
class PitchClass:
    

    @classmethod
    def from_str(cls, s: str) -> PitchClass:
        """from_str('Bb') -> PitchClass(NoteName('B'), Modifier(-1))"""
        flats = _count_flats(s)
        sharps = _count_sharps(s)
        natural = _contains_natural(s)
        modifier: Modifier | None = None
        if flats > 0:
            if natural or sharps > 0:
                raise ValueError("Cannot combine flats with sharps or naturals")
            modifier = Modifier(-flats)
        elif sharps > 0:
            if natural:
                raise ValueError("Cannot combine sharps with naturals")
            modifier = Modifier(sharps)
        elif natural:
            modifier = NATURAL
        note_name = s[0]
        return cls(NoteName(note_name), modifier)
    
    def to_pitch(self, octave: int) -> Pitch:
        return Pitch(self, octave)

    def __str__(self) -> str:
        if self.modifier is not None:
            return f"{self.note_name}{self.modifier}"
        return self.note_name.value

@dataclass
class Pitch:
    pitch_class: PitchClass
    octave: int

    @classmethod
    def from_str(cls, s: str) -> Pitch:
        """from_str('Bb2') -> Pitch(PitchClass(NoteName('B'), Modifier(-1)), 2)"""
        pitch_class = PitchClass.from_str(s)
        octave = int(s[-1])
        return cls(pitch_class, octave)

    def __str__(self) -> str:
        return f"{self.pitch_class}{self.octave}"

    def absolute_pitch(self) -> AbsolutePitch:
        pc = self.pitch_class
        ref = 0 if pc.modifier is None else pc.modifier.semitones
        above_octave_ref = pc.half_steps_above_c() + ref
        semis_above_c4 = 12 * (self.octave - 4) + above_octave_ref
        return TwelveTETPitch.from_semitones_above_c4(semis_above_c4)

    def enharmonic_equivalent(self, other: Pitch) -> bool:
        return self.absolute_pitch() == other.absolute_pitch()
