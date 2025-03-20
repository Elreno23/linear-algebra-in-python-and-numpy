import pytest
import numpy as np
from app import determinant, inverse_matrix  # Make sure to import the functions correctly

@pytest.mark.parametrize("matrix, mode, expected", [
    ([[1, 2], [3, 4]], "pure", -2),  # Test with lists
    ([[1, 2], [3, 4]], "numpy", -2)  # Test with NumPy
])
def test_determinant(matrix, mode, expected):
    """Verify that determinant returns the correct value in both modes."""
    result = determinant(matrix, mode)
    assert pytest.approx(result) == expected, f"Expected {expected}, but got {result}"

@pytest.mark.parametrize("matrix, mode, expected", [
    ([[1, 2], [3, 4]], "pure", [[-2.0, 1.0], [1.5, -0.5]]),  # Test with lists
    ([[1, 2], [3, 4]], "numpy", np.array([[-2.0, 1.0], [1.5, -0.5]]))  # Test with NumPy
])
def test_inverse_matrix(matrix, mode, expected):
    """Verify that inverse_matrix returns the correct inverse matrix in both modes."""
    result = inverse_matrix(matrix, mode)
    if mode == "pure":
        assert result == expected, f"Expected {expected}, but got {result}"
    else:
        assert np.allclose(result, expected), f"Expected {expected}, but got {result}"

def test_non_invertible_matrix():
    """Verify that an error is raised if the matrix is not invertible (determinant = 0)."""
    singular_matrix = [[1, 2], [2, 4]]  # Determinant = 0
    with pytest.raises(ValueError, match="Matrix is not invertible"):
        inverse_matrix(singular_matrix, "pure")

def test_invalid_mode():
    """Verify that an error is raised if the mode is invalid."""
    matrix = [[1, 2], [3, 4]]
    with pytest.raises(ValueError, match="Invalid mode"):
        determinant(matrix, "invalid_mode")
    with pytest.raises(ValueError, match="Invalid mode"):
        inverse_matrix(matrix, "invalid_mode")
