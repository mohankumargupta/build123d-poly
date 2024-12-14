import os
from itertools import permutations
from pathlib import Path
from typing import List


def generate_function_file(module_name: str, output_path: str = None) -> None:
    """
    Generate a Python source file with movement functions.

    Args:
        module_name: Name of the module (e.g., 'polyfuncs').
        output_path: Optional path to save the generated .py file. Defaults to the current directory.
    """
    base_moves = ["up", "down", "left", "right"]

    # Start building the Python source code
    file_lines = [
        f"# Auto-generated module: {module_name}\n",
        "from build123d import *\n",
        "from .line import up, down, left, right\n\n",
        
    ]

    # # Add base movement functions
    # for move in base_moves:
    #     file_lines.append(
    #         f"def {move}(distance: Union[int, float]) -> None:\n"
    #         f"    \"\"\"\n"
    #         f"    Move {move} a specified distance.\n\n"
    #         f"    Args:\n"
    #         f"        distance (int/float): Number of units to move {move}.\n"
    #         f"    \"\"\"\n"
    #         f"    print(f\"Moving {move} {{distance}} units\")\n\n"
    #     )

    # Generate unique compound functions (no repeated directions)
    for combination_length in [2, 3]:  # Double and triple moves
        for combination in permutations(base_moves, combination_length):
            func_name = "_".join(combination)
            params = ", ".join(f"{move}_distance: float" for move in combination)
            doc_args = "\n    ".join(f"{move}_distance (int/float): Distance for {move}" for move in combination)
            calls = "\n    ".join(f"{move}({move}_distance)" for move in combination)

            file_lines.append(
                f"def {func_name}({params}) -> None:\n"
                f"    \"\"\"\n"
                f"    Compound line: {' -> '.join(combination)}\n\n"
                f"    Args:\n"
                f"    {doc_args}\n\n"
                f"    {calls}\n"
                f"    \"\"\"\n"
                f"    {calls}\n\n"
            )

    # Add __all__ for better module exports
    all_functions = [
        f'"{"_".join(combination)}"' for combination_length in [2, 3]
        for combination in permutations(base_moves, combination_length)
    ]
    file_lines.append(f"__all__ = [{', '.join(all_functions)}]\n")

    # Determine the output path for the .py file
    # if output_path is None:
    #     output_path = f"{module_name}.py"
    # else:
    #     output_path = os.path.join(output_path, f"{module_name}.py")

    # Write the .py file
    output_directory = Path(__file__).parent.parent
    output_file = "multi.py"
    output_path = output_directory / output_file

    with open(output_path, "w") as py_file:
        py_file.writelines(file_lines)

    print(f"Python source file generated at {output_path}")


# Generate the Python source file
generate_function_file("polyfuncs_generated")