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

@pytest.mark.it("Raises ValueError when matrix rows have different lengths")
def test_transpose_invalid_matrix():
    invalid_matrix = [[1, 2], [3]]  # Irregular row lengths
    with pytest.raises(ValueError, match="Invalid matrix"):
        transpose(invalid_matrix, "pure")

@pytest.mark.it("Raises ValueError when mode is invalid")
def test_transpose_invalid_mode():
    matrix = [[1, 2, 3], [4, 5, 6]]
    with pytest.raises(ValueError, match="Invalid mode"):
        transpose(matrix, "invalid_mode")
