from dataclasses import dataclass
from . import scales


@dataclass
class Chord:
    name: str
    notes: tuple[str, ...]


def triad(
    scale: scales.Scale,
    suffix: str = "",
) -> Chord:
    return Chord(
        scale.notes[0] + suffix, (scale.notes[0], scale.notes[2], scale.notes[4])
    )


# major chords
C = triad(scales.C)
G = triad(scales.G)
D = triad(scales.D)
A = triad(scales.A)
E = triad(scales.E)
B = triad(scales.B)
Fsharp = triad(scales.Fsharp)
Csharp = triad(scales.Csharp)
F = triad(scales.F)
Bflat = triad(scales.Bflat)
Eflat = triad(scales.Eflat)
Aflat = triad(scales.Aflat)
Dflat = triad(scales.Dflat)
Gflat = triad(scales.Gflat)
Cflat = triad(scales.Cflat)

# minor chords
C_m = triad(scales.C_m, "m")
G_m = triad(scales.G_m, "m")
D_m = triad(scales.D_m, "m")
A_m = triad(scales.A_m, "m")
E_m = triad(scales.E_m, "m")
B_m = triad(scales.B_m, "m")
Fsharp_m = triad(scales.Fsharp_m, "m")
Csharp_m = triad(scales.Csharp_m, "m")
F_m = triad(scales.F_m, "m")
Bflat_m = triad(scales.Bflat_m, "m")
Eflat_m = triad(scales.Eflat_m, "m")
Aflat_m = triad(scales.Aflat_m, "m")
Dflat_m = triad(scales.Dflat_m, "m")
Gflat_m = triad(scales.Gflat_m, "m")
Cflat_m = triad(scales.Cflat_m, "m")


def make_seventh(chord: Chord, suffix: str, seventh: str) -> Chord:
    return Chord(chord.name + suffix, chord.notes + (seventh,))


# Dominant 7th (major triad + minor 7th)
C_7 = make_seventh(C, "7", scales.C_m.notes[6])
G_7 = make_seventh(G, "7", scales.G_m.notes[6])
D_7 = make_seventh(D, "7", scales.D_m.notes[6])
A_7 = make_seventh(A, "7", scales.A_m.notes[6])
E_7 = make_seventh(E, "7", scales.E_m.notes[6])
B_7 = make_seventh(B, "7", scales.B_m.notes[6])
Fsharp_7 = make_seventh(Fsharp, "7", scales.Fsharp_m.notes[6])
Csharp_7 = make_seventh(Csharp, "7", scales.Csharp_m.notes[6])
F_7 = make_seventh(F, "7", scales.F_m.notes[6])
Bflat_7 = make_seventh(Bflat, "7", scales.Bflat_m.notes[6])
Eflat_7 = make_seventh(Eflat, "7", scales.Eflat_m.notes[6])
Aflat_7 = make_seventh(Aflat, "7", scales.Aflat_m.notes[6])
Dflat_7 = make_seventh(Dflat, "7", scales.Dflat_m.notes[6])
Gflat_7 = make_seventh(Gflat, "7", scales.Gflat_m.notes[6])
Cflat_7 = make_seventh(Cflat, "7", scales.Cflat_m.notes[6])

# Major 7th (major triad + major 7th)
C_M7 = make_seventh(C, "7", scales.C.notes[6])
G_M7 = make_seventh(G, "7", scales.G.notes[6])
D_M7 = make_seventh(D, "7", scales.D.notes[6])
A_M7 = make_seventh(A, "7", scales.A.notes[6])
E_M7 = make_seventh(E, "7", scales.E.notes[6])
B_M7 = make_seventh(B, "7", scales.B.notes[6])
Fsharp_M7 = make_seventh(Fsharp, "7", scales.Fsharp.notes[6])
Csharp_M7 = make_seventh(Csharp, "7", scales.Csharp.notes[6])
F_M7 = make_seventh(F, "7", scales.F.notes[6])
Bflat_M7 = make_seventh(Bflat, "7", scales.Bflat.notes[6])
Eflat_M7 = make_seventh(Eflat, "7", scales.Eflat.notes[6])
Aflat_M7 = make_seventh(Aflat, "7", scales.Aflat.notes[6])
Dflat_M7 = make_seventh(Dflat, "7", scales.Dflat.notes[6])
Gflat_M7 = make_seventh(Gflat, "7", scales.Gflat.notes[6])
Cflat_M7 = make_seventh(Cflat, "7", scales.Cflat.notes[6])

# Minor 7th (minor triad + minor 7th)
C_m7 = make_seventh(C_m, "7", scales.C_m.notes[6])
G_m7 = make_seventh(G_m, "7", scales.G_m.notes[6])
D_m7 = make_seventh(D_m, "7", scales.D_m.notes[6])
A_m7 = make_seventh(A_m, "7", scales.A_m.notes[6])
E_m7 = make_seventh(E_m, "7", scales.E_m.notes[6])
B_m7 = make_seventh(B_m, "7", scales.B_m.notes[6])
Fsharp_m7 = make_seventh(Fsharp_m, "7", scales.Fsharp_m.notes[6])
Csharp_m7 = make_seventh(Csharp_m, "7", scales.Csharp_m.notes[6])
F_m7 = make_seventh(F_m, "7", scales.F_m.notes[6])
Bflat_m7 = make_seventh(Bflat_m, "7", scales.Bflat_m.notes[6])
Eflat_m7 = make_seventh(Eflat_m, "7", scales.Eflat_m.notes[6])
Aflat_m7 = make_seventh(Aflat_m, "7", scales.Aflat_m.notes[6])
Dflat_m7 = make_seventh(Dflat_m, "7", scales.Dflat_m.notes[6])
Gflat_m7 = make_seventh(Gflat_m, "7", scales.Gflat_m.notes[6])
Cflat_m7 = make_seventh(Cflat_m, "7", scales.Cflat_m.notes[6])
