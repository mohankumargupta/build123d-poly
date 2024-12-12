import pytest
from typing import Tuple
from build123d import Plane, Mode, Line

from build123d_poly import BuildPoly, line

def test_line():
    with BuildPoly(start_point=(1,2)) as poly:
        line((21,2))

    wires = poly.wires()
    vertices = poly.vertices()

    vertices_list = {(vertex.X,vertex.Y,vertex.Z) for vertex in vertices}
    assert len(wires) == 1
    assert len(vertices) == 2
    assert vertices_list == {(21.0,2.0,0.0), (1.0,2.0,0.0)}
 

# def test_buildpoly_initialization():
#     """Test basic initialization of BuildPoly"""
#     # Test default initialization
#     poly = BuildPoly()
#     assert poly.workplane == Plane.XY
#     assert poly.mode == Mode.ADD
#     assert poly.start_point is None
#     assert poly.current_point is None
#     assert poly.close is True

#     # Test initialization with custom parameters
#     start = (1.0, 2.0)
#     poly_custom = BuildPoly(
#         workplane=Plane.XZ, 
#         mode=Mode.SUBTRACT, 
#         start_point=start, 
#         close=False
#     )
#     assert poly_custom.workplane == Plane.XZ
#     assert poly_custom.mode == Mode.SUBTRACT
#     assert poly_custom.start_point == start
#     assert poly_custom.current_point == start
#     assert poly_custom.close is False

# def test_buildpoly_context_management():
#     """Test context management functionality"""
#     # Test that _current_manager is set and reset correctly
#     with BuildPoly() as poly:
#         assert BuildPoly._current_manager == poly
    
#     # Verify _current_manager is reset after context exit
#     assert BuildPoly._current_manager is None

# def test_buildpoly_get_manager_error():
#     """Test error handling for _get_manager when no context is active"""
#     with pytest.raises(RuntimeError, match="No active BuildPoly context"):
#         BuildPoly._get_manager()

# def test_buildpoly_lineto():
#     """Test the lineto method"""
#     start_point = (0.0, 0.0)
#     end_point = (1.0, 2.0)
    
#     with BuildPoly(start_point=start_point) as poly:
#         # Test initial current_point
#         assert poly.current_point == start_point
        
#         # Create a line
#         l = poly.lineto(end_point)
        
#         # Verify line properties
#         assert isinstance(l, Line)
#         assert l.start == start_point
#         assert l.end == end_point
        
#         # Verify current_point is updated
#         assert poly.current_point == end_point

# def test_line_function():
#     """Test the standalone line function"""
#     start_point = (0.0, 0.0)
#     end_point = (1.0, 2.0)
    
#     with BuildPoly(start_point=start_point):
#         # Create line using the function
#         l = line(end_point)
        
#         # Verify line properties
#         assert isinstance(l, Line)
#         assert l.start == start_point
#         assert l.end == end_point

# def test_line_function_no_context():
#     """Test error handling for line function when no context is active"""
#     with pytest.raises(RuntimeError, match="No active BuildPoly context"):
#         line((1.0, 2.0))

# def test_multiple_context_managers():
#     """Test behavior with nested or sequential context managers"""
#     # First context
#     with BuildPoly(start_point=(0.0, 0.0)) as poly1:
#         l1 = poly1.lineto((1.0, 1.0))
#         assert BuildPoly._current_manager == poly1
    
#     # Second context
#     with BuildPoly(start_point=(2.0, 2.0)) as poly2:
#         l2 = poly2.lineto((3.0, 3.0))
#         assert BuildPoly._current_manager == poly2
    
#     # Verify both contexts worked independently
#     assert l1.start == (0.0, 0.0)
#     assert l1.end == (1.0, 1.0)
#     assert l2.start == (2.0, 2.0)
#     assert l2.end == (3.0, 3.0)

# def test_point_type_hints():
#     """Verify type hints for point coordinates"""
#     # Ensure points can be tuples of floats
#     start_point: Tuple[float, float] = (0.0, 0.0)
#     end_point: Tuple[float, float] = (1.0, 2.0)
    
#     with BuildPoly(start_point=start_point) as poly:
#         l = poly.lineto(end_point)
#         assert l.start == start_point
#         assert l.end == end_point

# def test_workplane_mode_coverage():
#     """Test different workplane and mode configurations"""
#     test_configs = [
#         (Plane.XY, Mode.ADD),
#         (Plane.XZ, Mode.SUBTRACT),
#         (Plane.YZ, Mode.INTERSECTION)
#     ]
    
#     for plane, mode in test_configs:
#         poly = BuildPoly(workplane=plane, mode=mode)
#         assert poly.workplane == plane
#         assert poly.mode == mode

