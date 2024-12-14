from build123d import *
from build123d_poly import *
from ocp_vscode import show

# https://build123d.readthedocs.io/en/latest/introductory_examples.html
# 8. Polylines

(L, H, W, t) = (100.0, 20.0, 20.0, 1.0)

with BuildPart() as beam:
    with BuildSketch(Plane.XZ) as profile:
        with BuildPoly(start_point=(-t/2,0)) as p:
            up_left(H/2-t, W/2-t/2)
            up_right_down(t, W, t)
            left_down(W/2-t/2, H/2-t)
            mirror(about=Plane.XZ)
        make_face(p.edges())
    extrude(amount=L)

part = beam.part
show(part)
export_stl(part, "example1.stl")
