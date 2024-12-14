from typing import Tuple
from build123d import *
from .poly import BuildPoly

def line(end_point: VectorLike) -> Line:
    """
    Create a line from the current point to the specified end point.
    
    Args:
        end_point: The destination point of the line
    """
    return BuildPoly._get_manager().lineto(end_point)

def up(distance: float) -> Line:
    """
    Move up (along positive Y-axis) by the specified distance
    
    Args:
        distance: Distance to move up
    
    Returns:
        The created Line object
    """
    manager = BuildPoly._get_manager()
    x,y = manager.current_point
    return line((x, y + distance))

def down(distance: float) -> Line:
    """
    Move down (along negative Y-axis) by the specified distance
    
    Args:
        distance: Distance to move down
    
    Returns:
        The created Line object
    """
    manager = BuildPoly._get_manager()
    x,y = manager.current_point    
    return line((x, y - distance))

def left(distance: float) -> Line:
    """
    Move left (along negative X-axis) by the specified distance
    
    Args:
        distance: Distance to move left
    
    Returns:
        The created Line object
    """
    manager = BuildPoly._get_manager()
    x,y = manager.current_point   
    return line((x - distance, y))

def right(distance: float) -> Line:
    """
    Move right (along positive X-axis) by the specified distance
    
    Args:
        distance: Distance to move right
    
    Returns:
        The created Line object
    """
    manager = BuildPoly._get_manager()
    x,y = manager.current_point   
    return line((x + distance, y))

