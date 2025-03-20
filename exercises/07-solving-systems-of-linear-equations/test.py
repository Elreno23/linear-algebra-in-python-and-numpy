import pytest
import numpy as np
from app import solve_system

@pytest.mark.parametrize("A, b, mode, expected", [
    ([[2, 3], [4, -1]], [5, 1], "pure", [2, -1]),  # Test with lists
    ([[2, 3], [4, -1]], [5, 1], "numpy", np.array([2, -1]))  # Test with NumPy
])
def test_solve_system(A, b, mode, expected):
    """Verify that solve_system returns the correct solution in both modes."""
    result = solve_system(A, b, mode)
    if mode == "pure":
        assert result == expected, f"Expected {expected}, but got {result}"
    else:
        assert np.allclose(result, expected), f"Expected {expected}, but got {result}"

def test_solve_system_singular_matrix():
    """Verify that an error is raised if the matrix is not invertible (determinant = 0)."""
    singular_A = [[1, 2], [2, 4]]  # Determinant = 0
    b = [3, 6]
    with pytest.raises(ValueError, match="Matrix is not invertible"):
        solve_system(singular_A, b, "pure")

def test_solve_system_invalid_mode():
    """Verify that an error is raised if the mode is invalid."""
    A = [[2, 3], [4, -1]]
    b = [5, 1]
    with pytest.raises(ValueError, match="Invalid mode"):
        solve_system(A, b, "invalid_mode")
