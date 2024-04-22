from dataclasses import dataclass

@dataclass
class Interval:
    semitones: int

HALF = Interval(1)
WHOLE = Interval(2)
MINOR_THIRD = Interval(3)
MAJOR_THIRD = Interval(4)
FOURTH = Interval(5)
FIFTH = Interval(7)
MINOR_SEVENTH = Interval(10)
MAJOR_SEVENTH = Interval(11)

@dataclass
class Scale:
    root: str
    intervals: tuple[Interval, ...]

@dataclass
class MajorScale(Scale):
    intervals: tuple[Interval, ...] = (WHOLE, WHOLE, HALF, WHOLE, WHOLE, WHOLE, HALF)


@dataclass
class MinorScale(Scale):
    intervals: tuple[Interval, ...] = (WHOLE, HALF, WHOLE, WHOLE, HALF, WHOLE, WHOLE)

Am = MinorScale(root="A")

