from .notes import *
from typing import Sequence

class KeySignature:
    notes: Sequence[OctaveNaiveNote]

"""
A -> Db Ab Bb Eb ->
E -> Ab Bb Eb ->
B -> Bb Eb ->
F -> Eb ->
C -> == ->
G -> Gb
D -> Fb Gb 
"""