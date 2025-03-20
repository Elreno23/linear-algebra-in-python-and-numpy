import numpy as np  # Import NumPy to use it later
import random  # To generate random values in pure Python

def create_matrix(n, m, mode="pure"):
    """
    Generates an n x m matrix with random values.

    Parameters:
    - n: int -> Number of rows.
    - m: int -> Number of columns.
    - mode: str -> "pure" for Python lists, "numpy" for NumPy arrays.

    Returns:
    - A matrix in the specified format.
    """
    # TODO: Implement the logic to generate the matrix in the selected mode.
    pass  # Remove this line when the function is implemented

# Test the function with the following values:
matrix1 = create_matrix(3, 3, "pure")
matrix2 = create_matrix(3, 3, "numpy")

print("Matrix in pure Python:", matrix1)
print("Matrix in NumPy:\n", matrix2)
