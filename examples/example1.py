from build123d import *
from build123d_poly import *
from ocp_vscode import show_object

# https://build123d.readthedocs.io/en/latest/introductory_examples.html
# 8. Polylines

(L, H, W, t) = (100.0, 20.0, 20.0, 1.0)

with BuildPart() as beam:
    with BuildSketch(Plane.XZ) as profile:
        with BuildPoly(start_point=(0,-H/2)) as p:
            up(H)
            right_down_left(W/2, t, W/2 - t*2)
            down(H/2-t)
            mirror(about=Plane.XZ)
            mirror(about=Plane.YZ)
        make_face(p.edges())
    extrude(amount=L)

part = beam.part
show_object(part)

# with BuildPart() as club:
#     with BuildSketch() as example_6:
#         with BuildLine() as club_outline:
#             l0 = Line((0, -188), (76, -188))
#             b0 = Bezier(l0 @ 1, (61, -185), (33, -173), (17, -81))
#             b1 = Bezier(b0 @ 1, (49, -128), (146, -145), (167, -67))
#             b2 = Bezier(b1 @ 1, (187, 9), (94, 52), (32, 18))
#             b3 = Bezier(b2 @ 1, (92, 57), (113, 188), (0, 188))
#             mirror(about=Plane.YZ)
#         make_face()
#     extrude(amount=10)

#show(club)

