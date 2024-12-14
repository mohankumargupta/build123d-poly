from build123d import *
from build123d_poly import *

# https://build123d.readthedocs.io/en/latest/introductory_examples.html
# 8. Polylines

(L, H, W, t) = (100.0, 20.0, 20.0, 1.0)

with BuildPart() as beam:
    with BuildPoly(Plane.XZ) as profile:
        right_down_left(W/2, t, -W/2)
        down_right(H-2*t, W/2 - t/2)
    mirror()
    extrude(amount=L)

part = beam.part
