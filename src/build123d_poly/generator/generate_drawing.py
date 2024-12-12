import inspect
from typing import Any, List, Type
from build123d_poly import BuildPoly
from build123d_poly.runtime import mark

def get_decorated_members(cls: Type[Any], decorator: Any) -> List[str]:
    """
    Retrieve names of class members decorated with a specific decorator.
    
    Args:
        cls (Type): The class to inspect
        decorator (Any): The decorator to look for
    
    Returns:
        List[str]: Names of members with the specified decorator
    """
    decorated_members = []
    
    # Inspect class members
    for name, member in inspect.getmembers(cls):
        # Check if the member has the specified decorator
        if hasattr(member, '__drawing1d__'):
            if decorator in member.__drawing1d__:
                decorated_members.append(name)
    
    return decorated_members

# Get members with the custom marker
decorated_methods = get_decorated_members(BuildPoly, mark)
print(decorated_methods)  # Should print ['method1', 'method2']