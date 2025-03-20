import pytest
import numpy as np
from app import transpose  # Make sure to import the function correctly

@pytest.mark.parametrize("matrix, mode, expected", [
    ([[1, 2, 3], [4, 5, 6]], "pure", [[1, 4], [2, 5], [3, 6]]),  # Test with lists
    ([[1, 2, 3], [4, 5, 6]], "numpy", np.array([[1, 4], [2, 5], [3, 6]]))  # Test with NumPy
])
def test_transpose(matrix, mode, expected):
    """Verify that transpose returns the correct transposed matrix in both modes."""
    result = transpose(matrix, mode)
    if mode == "pure":
        assert result == expected, f"Expected {expected}, but got {result}"
    else:
        assert np.array_equal(result, expected), f"Expected {expected}, but got {result}"

def test_transpose_invalid_matrix():
    """Verify that an error is raised if the matrix is invalid."""
    invalid_matrix = [[1, 2], [3]]  # Rows of different lengths
    with pytest.raises(ValueError, match="Invalid matrix"):
        transpose(invalid_matrix, "pure")

def test_transpose_invalid_mode():
    """Verify that an error is raised if the mode is invalid."""
    matrix = [[1, 2, 3], [4, 5, 6]]
    with pytest.raises(ValueError, match="Invalid mode"):
        transpose(matrix, "invalid_mode")
