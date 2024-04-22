from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Interval:
    semitones: int

    def __add__(self, other: Interval) -> Interval:
        return Interval(self.semitones + other.semitones)


unison = Interval(0)
half_step = minor_second = Interval(1)
whole_step = major_second = Interval(2)
minor_third = Interval(3)
major_third = Interval(4)
perfect_fourth = Interval(5)
augmented_fourth = diminished_fifth = tritone = Interval(6)
perfect_fifth = Interval(7)
minor_sixth = augmented_fifth = Interval(8)
major_sixth = diminished_seventh = Interval(9)
minor_seventh = Interval(10)
major_seventh = Interval(11)
octave = Interval(12)
