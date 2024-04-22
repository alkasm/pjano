from dataclasses import dataclass
from . import notes as n


@dataclass(frozen=True)
class Scale:
    notes: tuple[str, ...]


C = Scale((n.C, n.D, n.E, n.F, n.G, n.A, n.B))
G = Scale((n.G, n.A, n.B, n.C, n.D, n.E, n.F.sharp))
D = Scale((n.D, n.E, n.F.sharp, n.G, n.A, n.B, n.C.sharp))
A = Scale((n.A, n.B, n.C.sharp, n.D, n.E, n.F.sharp, n.G.sharp))
E = Scale((n.E, n.F.sharp, n.G.sharp, n.A, n.B, n.C.sharp, n.D.sharp))
B = Scale((n.B, n.C.sharp, n.D.sharp, n.E, n.F.sharp, n.G.sharp, n.A.sharp))
Fsharp = Scale((n.F.sharp, n.G.sharp, n.A.sharp, n.B, n.C.sharp, n.D.sharp, n.E.sharp))
Csharp = Scale(
    (n.C.sharp, n.D.sharp, n.E.sharp, n.F.sharp, n.G.sharp, n.A.sharp, n.B.sharp)
)

F = Scale((n.F, n.G, n.A, n.B.flat, n.C, n.D, n.E))
Bflat = Scale((n.B.flat, n.C, n.D, n.E.flat, n.F, n.G, n.A))
Eflat = Scale((n.E.flat, n.F, n.G, n.A.flat, n.B.flat, n.C, n.D))
Aflat = Scale((n.A.flat, n.B.flat, n.C, n.D.flat, n.E.flat, n.F, n.G))
Dflat = Scale((n.D.flat, n.E.flat, n.F, n.G.flat, n.A.flat, n.B.flat, n.C))
Gflat = Scale((n.G.flat, n.A.flat, n.B.flat, n.C.flat, n.D.flat, n.E.flat, n.F))
Cflat = Scale((n.C.flat, n.D.flat, n.E.flat, n.F.flat, n.G.flat, n.A.flat, n.B.flat))


def _relative_minor(scale: Scale) -> Scale:
    return Scale((*scale.notes[5:], *scale.notes[:5]))


A_m = _relative_minor(C)
E_m = _relative_minor(G)
B_m = _relative_minor(D)
Fsharp_m = _relative_minor(A)
Csharp_m = _relative_minor(E)
Gsharp_m = _relative_minor(B)
Dsharp_m = _relative_minor(Fsharp)
Asharp_m = _relative_minor(Csharp)

D_m = _relative_minor(F)
G_m = _relative_minor(Bflat)
C_m = _relative_minor(Eflat)
F_m = _relative_minor(Aflat)
Bflat_m = _relative_minor(Dflat)
Eflat_m = _relative_minor(Gflat)
Aflat_m = _relative_minor(Cflat)
Dflat_m = Scale((n.D.flat, n.E.flat, n.E, n.G.flat, n.A.flat, n.B.flat, n.B))
Gflat_m = Scale((n.G.flat, n.A.flat, n.A, n.C.flat, n.D.flat, n.E.flat, n.E))
Cflat_m = Scale((n.C.flat, n.D.flat, n.D, n.F.flat, n.G.flat, n.A.flat, n.A))
