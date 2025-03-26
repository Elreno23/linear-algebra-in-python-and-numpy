import pytest
import numpy as np
from app import create_matrix  # Make sure to import the function correctly

@pytest.mark.it("Returns a nested list when mode is 'pure'")
def test_create_matrix_returns_list():
    result = create_matrix(3, 3, "pure")
    assert isinstance(result, list), f"Expected list, but got {type(result)}"

@pytest.mark.it("Returns a NumPy array when mode is 'numpy'")
def test_create_matrix_returns_numpy_array():
    result = create_matrix(3, 3, "numpy")
    assert isinstance(result, np.ndarray), f"Expected np.ndarray, but got {type(result)}"

@pytest.mark.it("Returns a matrix with correct shape in 'pure' mode")
def test_create_matrix_shape_pure():
    n, m = 4, 5
    matrix = create_matrix(n, m, "pure")
    assert len(matrix) == n, "Incorrect number of rows in 'pure' mode"
    assert all(len(row) == m for row in matrix), "Incorrect number of columns in 'pure' mode"

@pytest.mark.it("Returns a matrix with correct shape in 'numpy' mode")
def test_create_matrix_shape_numpy():
    n, m = 4, 5
    matrix = create_matrix(n, m, "numpy")
    assert matrix.shape == (n, m), f"Expected shape ({n}, {m}), but got {matrix.shape}"

@pytest.mark.it("Raises ValueError when mode is invalid")
def test_create_matrix_invalid_mode():
    with pytest.raises(ValueError, match="Invalid mode"):
        create_matrix(3, 3, "invalid_mode")