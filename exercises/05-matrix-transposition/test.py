import pytest
import numpy as np
from app import transpose  # Make sure to import the function correctly

@pytest.mark.it("Correctly transposes a matrix in 'pure' mode")
def test_transpose_pure():
    matrix = [[1, 2, 3], [4, 5, 6]]
    expected = [[1, 4], [2, 5], [3, 6]]
    result = transpose(matrix, "pure")
    assert result == expected, f"Expected {expected}, but got {result}"

@pytest.mark.it("Correctly transposes a matrix in 'numpy' mode")
def test_transpose_numpy():
    matrix = [[1, 2, 3], [4, 5, 6]]
    expected = np.array([[1, 4], [2, 5], [3, 6]])
    result = transpose(matrix, "numpy")
    assert np.array_equal(result, expected), f"Expected {expected}, but got {result}"

@pytest.mark.it("Returns an error message when matrix rows have different lengths in transpose")
def test_transpose_invalid_matrix():
    invalid_matrix = [[1, 2], [3]]  # Irregular row lengths
    result = transpose(invalid_matrix, "pure")
    assert isinstance(result, str), "Expected a string error message from transpose"
    assert "invalid matrix" in result.lower(), f"Expected error message to mention 'Invalid matrix', but got: {result}"