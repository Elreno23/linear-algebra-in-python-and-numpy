import pytest
import numpy as np
from app import create_matrix  # Make sure to import the function correctly

@pytest.mark.parametrize("n, m, mode, expected_type", [
    (3, 3, "pure", list),  # Matrix in nested lists
    (3, 3, "numpy", np.ndarray),  # Matrix in NumPy
])
def test_create_matrix_type(n, m, mode, expected_type):
    result = create_matrix(n, m, mode)
    assert isinstance(result, expected_type), f"Expected {expected_type}, but got {type(result)}"

def test_create_matrix_shape():
    n, m = 4, 5
    pure_matrix = create_matrix(n, m, "pure")
    numpy_matrix = create_matrix(n, m, "numpy")

    assert len(pure_matrix) == n, "Incorrect number of rows in 'pure' mode"
    assert all(len(row) == m for row in pure_matrix), "Incorrect number of columns in 'pure' mode"

    assert numpy_matrix.shape == (n, m), "Incorrect dimensions in 'numpy' mode"

def test_create_matrix_invalid_mode():
    with pytest.raises(ValueError, match="Invalid mode"):
        create_matrix(3, 3, "invalid_mode")
