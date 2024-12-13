from functools import wraps
from build123d import *

def mark(params_string: str, return_string: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        
        if not hasattr(wrapper, '__drawing1d__'):
            wrapper.__drawing1d__ = set()
        wrapper.__drawing1d__.add(mark)
        
        # Store the parameters
        wrapper.__mark_params_string = params_string
        wrapper.__mark_return_string = return_string
        
        return wrapper
    return decorator

@mark("end_point: VectorLike, tangent: VectorLike, tangent_from_first: bool = True,mode: Mode = Mode.ADD", "TangentArc")
def tangent_arc(self, end_point: VectorLike, tangent: VectorLike, tangent_from_first: bool = True, mode: Mode = Mode.ADD) -> TangentArc:
    pts = [self.current_point, end_point]
    return TangentArc(pts, tangent, tangent_from_first, mode)

# To retrieve the parameters later
import inspect

params_string = inspect.getattr_static(tangent_arc, '__mark_params_string')
return_string = inspect.getattr_static(tangent_arc, '__mark_return_string')
print(f"Parameter 1: {params_string}")
print(f"Parameter 2: {return_string}")
