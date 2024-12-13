from typing import Any, Iterable, Optional, Self, Tuple, Type, TypeVar, Union
from build123d import *
from .runtime import mark

T = TypeVar('T', bound='BuildPoly')

class BuildPoly(BuildLine):
    # Class variable with Optional type
    _current_manager: Optional[Self] = None

    def __init__(
        self, 
        workplane: Plane = Plane.XY, 
        mode: Mode = Mode.ADD, 
        start_point: Optional[Tuple[float, float]] = None, 
        close: bool = True
    ):
        # Explicitly type annotate instance variables
        self.start_point: Optional[Tuple[float, float]] = start_point
        self.current_point: Optional[Tuple[float, float]] = self.start_point
        self.close: bool = close
        
        # Call parent constructor with explicit type checking
        super().__init__(workplane, mode)

    def __enter__(self: Self) -> Self:
        # Ensure type safety for context manager entry
        super().__enter__()
        BuildPoly._current_manager = self
        return self
    
    def __exit__(
        self, 
        exception_type: Optional[Type[BaseException]], 
        exception_value: Optional[BaseException], 
        traceback: Optional[Any]
    ) -> Optional[bool]:
        return super().__exit__(exception_type, exception_value, traceback)

    def lineto(self, end_point: Tuple[float, float]) -> Line:
        """
        Create a line to the specified end point
        
        Args:
            end_point: Destination point of the line
        """
        l = Line(end_point, self.current_point)
        self.current_point = end_point
        return l
    
    @mark
    def tangent_arc(self, end_point: VectorLike, tangent: VectorLike, tangent_from_first: bool = True,mode: Mode = Mode.ADD)->TangentArc:
        pts = [self.current_point, end_point]
        return TangentArc(pts, tangent, tangent_from_first, mode)
        
    @classmethod
    def _get_manager(cls: Type[T]) -> T:
        """
        Get the current active BuildPoly context manager.
        
        Returns:
            The current active context manager
        
        Raises:
            RuntimeError: If no active context manager exists
        """
        if cls._current_manager is None:
            raise RuntimeError("No active BuildPoly context. Use 'with BuildPoly() as poly:' first.")
        return cls._current_manager

