import pytest
import numpy as np
from app import solve_system

# --- Solve System Tests ---

@pytest.mark.it("Correctly solves a linear system in 'pure' mode")
def test_solve_system_pure():
    A = [[2, 3], [4, -1]]
    b = [5, 1]
    expected = [2, -1]
    result = solve_system(A, b, "pure")
    assert result == expected, f"Expected {expected}, but got {result}"

@pytest.mark.it("Correctly solves a linear system in 'numpy' mode")
def test_solve_system_numpy():
    A = [[2, 3], [4, -1]]
    b = [5, 1]
    expected = np.array([2, -1])
    result = solve_system(A, b, "numpy")
    assert np.allclose(result, expected), f"Expected {expected}, but got {result}"

# --- Error Handling ---

@pytest.mark.it("Raises ValueError when the coefficient matrix is not invertible")
def test_solve_system_singular_matrix():
    A = [[1, 2], [2, 4]]  # Determinant = 0
    b = [3, 6]
    with pytest.raises(ValueError, match="Matrix is not invertible"):
        solve_system(A, b, "pure")

@pytest.mark.it("Raises ValueError when the mode is invalid")
def test_solve_system_invalid_mode():
    A = [[2, 3], [4, -1]]
    b = [5, 1]
    with pytest.raises(ValueError, match="Invalid mode"):
        solve_system(A, b, "invalid_mode")