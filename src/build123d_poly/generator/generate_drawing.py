import inspect
import os
from jinja2 import Template
from build123d_poly.runtime import mark
from build123d_poly import BuildPoly

def generate_boo_py(cls, decorator):
    """
    Generate boo.py with free functions matching decorated class methods using Jinja2.
    
    Args:
        cls (Type): The class to inspect
        decorator (Any): The decorator to look for
    """
    # Collect decorated methods
    decorated_methods = []
    for name, member in inspect.getmembers(cls):
        if (callable(member) and 
            hasattr(member, '__drawing1d__') and 
            decorator in member.__drawing1d__):
            
            # Get signature information
            sig = inspect.signature(member)
            
            # Remove 'self' parameter for free function
            free_func_params = list(sig.parameters.values())[1:]
            new_sig = sig.replace(parameters=free_func_params)
            
            # Prepare parameter details
            params = []
            parameters = new_sig.parameters
            for param in parameters:

                param_name = parameters[param].name
                annotation = parameters[param].annotation
                annotation_name = annotation.__name__
                default = parameters[param].default

                param_info = {
                    'name': param_name,
                    'annotation': (
                        annotation_name
                        if annotation is not inspect.Parameter.empty
                        else None
                    ),
                    'default': (
                        repr(default) 
                        if default is not inspect.Parameter.empty 
                        else None
                    )
                }
                params.append(param_info)
            
            decorated_methods.append({
                'name': name,
                'params': params,
                'return_annotation': (
                    sig.return_annotation.__name__ 
                    if sig.return_annotation is not inspect.Signature.empty 
                    else None
                )
            })
    
    # Jinja2 template
    template_str = """# Automatically generated functions

from build123d import *
from typing import Union

{% for method in methods %}
def {{ method.name }}({% for param in method.params -%}
    {{ param.name }}{% if param.annotation %}: {{ param.annotation }}{% endif %}{% if param.default %} = {{ param.default }}{% endif %}{% if not loop.last %}, {% endif %}
{%- endfor %}){%- if method.return_annotation %} -> {{ method.return_annotation }}{% endif %}:
    pass

{% endfor %}"""
    
    # Create Jinja2 template
    template = Template(template_str)
    
    # Render template
    rendered_content = template.render(methods=decorated_methods)
    
    # Write to boo.py
    with open('boo.py', 'w') as f:
        f.write(rendered_content)
    
    print(f"Generated boo.py with {len(decorated_methods)} functions")

# Custom marker decorator
def custom_marker(func):
    if not hasattr(func, '__decorators__'):
        func.__decorators__ = set()
    func.__decorators__.add(custom_marker)
    return func

# Example class with typed methods
class MyClass:
    @custom_marker
    def method1(self, x: int, y: str = 'default') -> bool:
        """Example method with annotations"""
        return True
    
    @custom_marker
    def method2(self, a: float, b: float) -> float:
        """Another example method"""
        return a + b
    
    def method3(self):
        """Undecorated method"""
        pass

# Generate boo.py
generate_boo_py(BuildPoly, mark)