import pytest
import numpy as np
from app import dot_product, matrix_product  # Make sure to import the functions correctly

@pytest.mark.parametrize("v1, v2, mode, expected", [
    ([1, 2, 3], [4, 5, 6], "pure", 32),  # Test with lists (1*4 + 2*5 + 3*6)
    ([1, 2, 3], [4, 5, 6], "numpy", 32)  # Test with NumPy
])
def test_dot_product(v1, v2, mode, expected):
    result = dot_product(v1, v2, mode)
    assert result == expected, f"Expected {expected}, but got {result}"

@pytest.mark.parametrize("A, B, mode, expected", [
    ([[1, 2], [3, 4]], [[5, 6], [7, 8]], "pure", [[19, 22], [43, 50]]),  # Test with lists
    ([[1, 2], [3, 4]], [[5, 6], [7, 8]], "numpy", np.array([[19, 22], [43, 50]]))  # Test with NumPy
])
def test_matrix_product(A, B, mode, expected):
    result = matrix_product(A, B, mode)
    if mode == "pure":
        assert result == expected, f"Expected {expected}, but got {result}"
    else:
        assert np.array_equal(result, expected), f"Expected {expected}, but got {result}"

def test_dot_product_invalid_length():
    v1 = [1, 2]
    v2 = [3, 4, 5]  # Different length
    with pytest.raises(ValueError, match="Vectors must have the same length"):
        dot_product(v1, v2, "pure")

def test_matrix_product_invalid_size():
    A = [[1, 2], [3, 4]]
    B = [[5, 6, 7], [8, 9, 10], [11, 12, 13]]  # Incorrect dimensions
    with pytest.raises(ValueError, match="Incompatible matrix dimensions"):
        matrix_product(A, B, "pure")

def test_invalid_mode():
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]

    with pytest.raises(ValueError, match="Invalid mode"):
        dot_product(v1, v2, "invalid_mode")

    with pytest.raises(ValueError, match="Invalid mode"):
        matrix_product(A, B, "invalid_mode")