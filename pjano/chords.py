from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, Sequence
from . import intervals, keys, pitch


@dataclass(frozen=True)
class Chord:
    root: pitch.PitchClass
    intervals: Sequence[intervals.Interval]
    """Intervals should contain unison if the root note is in the chord."""

    def pitch_classes(self) -> Iterable[pitch.PitchClass]:
        pc = self.root
        for i in self.intervals:
            pc += i
            yield pc

    def spell(self, key: keys.Key) -> Iterable[pitch.PitchSpelling]:
        yield from key.spell_pitch_classes(self.pitch_classes())


ThreeIntervals = tuple[intervals.Interval, intervals.Interval, intervals.Interval]
FourIntervals = tuple[
    intervals.Interval, intervals.Interval, intervals.Interval, intervals.Interval
]


@dataclass(frozen=True)
class MajorTriad(Chord):
    intervals: ThreeIntervals = (
        intervals.unison,
        intervals.major_third,
        intervals.perfect_fifth,
    )


@dataclass(frozen=True)
class MinorTriad(Chord):
    intervals: ThreeIntervals = (
        intervals.unison,
        intervals.minor_third,
        intervals.perfect_fifth,
    )


@dataclass(frozen=True)
class DiminishedTriad(Chord):
    intervals: ThreeIntervals = (
        intervals.unison,
        intervals.minor_third,
        intervals.diminished_fifth,
    )


@dataclass(frozen=True)
class AugmentedTriad(Chord):
    intervals: ThreeIntervals = (
        intervals.unison,
        intervals.major_third,
        intervals.augmented_fifth,
    )


@dataclass(frozen=True)
class MajorSixth(Chord):
    intervals: FourIntervals = (
        *MajorTriad.intervals,
        intervals.major_sixth,
    )


@dataclass(frozen=True)
class MinorSixth(Chord):
    intervals: FourIntervals = (
        *MinorTriad.intervals,
        intervals.major_sixth,
    )


@dataclass(frozen=True)
class SuspendedFourth(Chord):
    intervals: ThreeIntervals = (
        intervals.unison,
        intervals.perfect_fourth,
        intervals.perfect_fifth,
    )


@dataclass(frozen=True)
class SuspendedSecond(Chord):
    intervals: ThreeIntervals = (
        intervals.unison,
        intervals.major_second,
        intervals.perfect_fifth,
    )


@dataclass(frozen=True)
class DominantSeventhSuspendedFourth(Chord):
    intervals: FourIntervals = (
        *SuspendedFourth.intervals,
        intervals.minor_seventh,
    )


@dataclass(frozen=True)
class DominantSeventh(Chord):
    intervals: FourIntervals = (
        *MajorTriad.intervals,
        intervals.minor_seventh,
    )


@dataclass(frozen=True)
class MajorSeventh(Chord):
    intervals: FourIntervals = (
        *MajorTriad.intervals,
        intervals.major_seventh,
    )


@dataclass(frozen=True)
class MinorSeventh(Chord):
    intervals: FourIntervals = (
        *MinorTriad.intervals,
        intervals.major_seventh,
    )


@dataclass(frozen=True)
class HalfDiminishedSeventh(Chord):
    intervals: FourIntervals = (
        *DiminishedTriad.intervals,
        intervals.minor_seventh,
    )


@dataclass(frozen=True)
class DiminishedSeventh(Chord):
    intervals: FourIntervals = (
        *DiminishedTriad.intervals,
        intervals.diminished_seventh,
    )


@dataclass(frozen=True)
class CommonChords:
    root: pitch.PitchClass
    major_triad: MajorTriad
    minor_triad: MinorTriad
    diminished_triad: DiminishedTriad
    augmented_triad: AugmentedTriad
    major_sixth: MajorSixth
    minor_sixth: MinorSixth
    suspended_fourth: SuspendedFourth
    suspended_second: SuspendedSecond
    dominant_seventh_suspended_fourth: DominantSeventhSuspendedFourth
    dominant_seventh: DominantSeventh
    major_seventh: MajorSeventh
    minor_seventh: MinorSeventh
    half_diminished_seventh: HalfDiminishedSeventh
    diminished_seventh: DiminishedSeventh

    @classmethod
    def from_root(cls, root: pitch.PitchClass) -> CommonChords:
        return cls(
            root,
            MajorTriad(root),
            MinorTriad(root),
            DiminishedTriad(root),
            AugmentedTriad(root),
            MajorSixth(root),
            MinorSixth(root),
            SuspendedFourth(root),
            SuspendedSecond(root),
            DominantSeventhSuspendedFourth(root),
            DominantSeventh(root),
            MajorSeventh(root),
            MinorSeventh(root),
            HalfDiminishedSeventh(root),
            DiminishedSeventh(root),
        )
