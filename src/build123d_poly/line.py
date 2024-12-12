from typing import Tuple
from build123d import Line
from .poly import BuildPoly

def line(end_point: Tuple[float, float]) -> Line:
    """
    Create a line from the current point to the specified end point.
    
    Args:
        end_point: The destination point of the line
    """
    return BuildPoly._get_manager().lineto(end_point)