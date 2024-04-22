from __future__ import annotations
from typing import Sequence
from .notes import *
from dataclasses import dataclass

@dataclass
class Interval:
    half_steps: int
    def __add__(self, other: Interval) -> Interval:
        return Interval(self.half_steps + other.half_steps)
    
HALF = Interval(1)
WHOLE = Interval(2)

@dataclass
class Scale:
    intervals: Sequence[Interval]

class MajorScale(Scale):
    intervals = (WHOLE, WHOLE, HALF, WHOLE, WHOLE, WHOLE)

class MinorScale(Scale):
    intervals = (WHOLE, HALF, WHOLE, WHOLE, HALF, WHOLE)

class HarmonicMinorScale(Scale):
    intervals = (WHOLE, HALF, WHOLE, WHOLE, HALF, Interval(3))

