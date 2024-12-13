# Automatically generated functions from generate_drawing_1d.py
from build123d import *
from .poly import BuildPoly

def tangent_arc(end_point: VectorLike, tangent: VectorLike, tangent_from_first: bool = True,mode: Mode = Mode.ADD) -> TangentArc:
    BuildPoly._current_manager.tangent_arc(end_point, tangent, tangent_from_first, mode)
