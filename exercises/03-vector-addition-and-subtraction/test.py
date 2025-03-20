import pytest
import numpy as np
from app import sum_vectors, subtract_vectors  # Make sure to import the functions correctly

@pytest.mark.parametrize("v1, v2, mode, expected", [
    ([1, 2, 3], [4, 5, 6], "pure", [5, 7, 9]),  # Test sum with lists
    ([1, 2, 3], [4, 5, 6], "numpy", np.array([5, 7, 9]))  # Test sum with NumPy
])
def test_sum_vectors(v1, v2, mode, expected):
    result = sum_vectors(v1, v2, mode)
    if mode == "pure":
        assert result == expected, f"Expected {expected}, but got {result}"
    else:  # For NumPy, we use np.array_equal
        assert np.array_equal(result, expected), f"Expected {expected}, but got {result}"

@pytest.mark.parametrize("v1, v2, mode, expected", [
    ([1, 2, 3], [4, 5, 6], "pure", [-3, -3, -3]),  # Test subtraction with lists
    ([1, 2, 3], [4, 5, 6], "numpy", np.array([-3, -3, -3]))  # Test subtraction with NumPy
])
def test_subtract_vectors(v1, v2, mode, expected):
    result = subtract_vectors(v1, v2, mode)
    if mode == "pure":
        assert result == expected, f"Expected {expected}, but got {result}"
    else:  # For NumPy, we use np.array_equal
        assert np.array_equal(result, expected), f"Expected {expected}, but got {result}"

def test_vector_invalid_length():
    v1 = [1, 2, 3]
    v2 = [4, 5]
    with pytest.raises(ValueError, match="Vectors must have the same length"):
        sum_vectors(v1, v2, "pure")
    with pytest.raises(ValueError, match="Vectors must have the same length"):
        subtract_vectors(v1, v2, "numpy")

def test_vector_invalid_mode():
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    with pytest.raises(ValueError, match="Invalid mode"):
        sum_vectors(v1, v2, "invalid_mode")
    with pytest.raises(ValueError, match="Invalid mode"):
        subtract_vectors(v1, v2, "invalid_mode")
