import pytest
import numpy as np
from app import determinant, inverse_matrix  # Make sure to import the function correctly


# --- Determinant Tests ---

@pytest.mark.it("Correctly calculates the determinant in 'pure' mode")
def test_determinant_pure():
    matrix = [[1, 2], [3, 4]]
    expected = -2
    result = determinant(matrix, "pure")
    assert pytest.approx(result) == expected, f"Expected {expected}, but got {result}"

@pytest.mark.it("Correctly calculates the determinant in 'numpy' mode")
def test_determinant_numpy():
    matrix = [[1, 2], [3, 4]]
    expected = -2
    result = determinant(matrix, "numpy")
    assert pytest.approx(result) == expected, f"Expected {expected}, but got {result}"

# --- Inverse Matrix Tests ---

@pytest.mark.it("Correctly returns the inverse matrix in 'pure' mode")
def test_inverse_matrix_pure():
    matrix = [[1, 2], [3, 4]]
    expected = [[-2.0, 1.0], [1.5, -0.5]]
    result = inverse_matrix(matrix, "pure")
    assert result == expected, f"Expected {expected}, but got {result}"

@pytest.mark.it("Correctly returns the inverse matrix in 'numpy' mode")
def test_inverse_matrix_numpy():
    matrix = [[1, 2], [3, 4]]
    expected = np.array([[-2.0, 1.0], [1.5, -0.5]])
    result = inverse_matrix(matrix, "numpy")
    assert np.allclose(result, expected), f"Expected {expected}, but got {result}"

# --- Error Handling ---

@pytest.mark.it("Returns an error message when the matrix is not invertible")
def test_non_invertible_matrix():
    singular_matrix = [[1, 2], [2, 4]]  # Determinant = 0
    result = inverse_matrix(singular_matrix, "pure")
    assert isinstance(result, str), "Expected a string error message from inverse_matrix"
    assert "not invertible" in result.lower(), f"Expected error message to mention 'not invertible', but got: {result}"

@pytest.mark.it("Returns an error message when an invalid mode is passed to determinant")
@pytest.mark.parametrize("invalid_mode", ["", None, "invalid", 0, "Det", "PURE", "NumPy"])
def test_determinant_invalid_mode(invalid_mode):
    matrix = [[1, 2], [3, 4]]
    result = determinant(matrix, invalid_mode)
    assert isinstance(result, str), "Expected a string error message from determinant"
    assert "invalid mode" in result.lower(), f"Expected error message to mention 'Invalid mode', but got: {result}"

@pytest.mark.it("Returns an error message when an invalid mode is passed to inverse_matrix")
@pytest.mark.parametrize("invalid_mode", ["", None, "invalid", 0, "Inverse", "PURE", "NumPy"])
def test_inverse_matrix_invalid_mode(invalid_mode):
    matrix = [[1, 2], [3, 4]]
    result = inverse_matrix(matrix, invalid_mode)
    assert isinstance(result, str), "Expected a string error message from inverse_matrix"
    assert "invalid mode" in result.lower(), f"Expected error message to mention 'Invalid mode', but got: {result}"