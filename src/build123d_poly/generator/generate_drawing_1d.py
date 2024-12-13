import inspect
import os
import typing
from jinja2 import Environment, FileSystemLoader, Template
from build123d_poly.runtime import mark
from build123d_poly import BuildPoly
from pathlib import Path

def generate_1d_functions(cls, decorator, template_directory, template_file, output_directory, output_file):
    """
    Generate drawing_1d.py with free functions matching decorated class methods using Jinja2.
    
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
            hints = typing.get_type_hints(member)
             
            params_string = inspect.getattr_static(member, '__mark_params_string')
            return_string = inspect.getattr_static(member, '__mark_return_string')

            print(params_string)
            print(return_string)

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
                ),
                'params_string': params_string,
                'return_string':  return_string
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
    
    env = Environment(loader=FileSystemLoader(template_directory))
    template = env.get_template(template_file)
    rendered_content = template.render(methods=decorated_methods)

    output = Path(output_directory) / output_file

    with open(output, 'w') as f:
        f.write(rendered_content)
    
    print(f"Generated drawing_1d.py with {len(decorated_methods)} functions")

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


output_directory = Path(__file__).parent.parent
output_file = "drawing_1d.py"
template_file = "generate_1d.j2"
template_directory = Path(__file__).parent / "templates" 
generate_1d_functions(BuildPoly, mark, template_directory, template_file, output_directory, output_file)