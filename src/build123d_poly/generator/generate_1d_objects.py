from jinja2 import Template
import inspect
from typing import Type
from build123d_poly import BuildPoly

def generate_pyi_with_jinja(cls: Type, template_file: str, output_file: str):
    # Extract marked methods and their signatures
    methods = [
        (name, str(inspect.signature(method)))
        for name, method in inspect.getmembers(cls, predicate=inspect.isfunction)
        if getattr(method, "_is_marked", False)
    ]
    
    # Load and render the template
    with open(template_file, "r") as f:
        template = Template(f.read())
    
    rendered = template.render(class_name=cls.__name__, methods=methods)
    
    # Write the rendered content to the output file
    with open(output_file, "w") as f:
        f.write(rendered)

# Generate the stub file using Jinja2
generate_pyi_with_jinja(BuildPoly, "pyi.j2", "generated_functions.pyi")
