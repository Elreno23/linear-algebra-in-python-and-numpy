import pytest
import numpy as np
from app import dot_product, matrix_product  # Make sure to import the functions correctly

# --- Dot Product Tests ---

@pytest.mark.it("Correctly computes the dot product in 'pure' mode")
def test_dot_product_pure():
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    expected = 32  # 1*4 + 2*5 + 3*6
    result = dot_product(v1, v2, "pure")
    assert result == expected, f"Expected {expected}, but got {result}"

@pytest.mark.it("Correctly computes the dot product in 'numpy' mode")
def test_dot_product_numpy():
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    expected = 32
    result = dot_product(v1, v2, "numpy")
    assert result == expected, f"Expected {expected}, but got {result}"

# --- Matrix Product Tests ---

@pytest.mark.it("Correctly multiplies two matrices in 'pure' mode")
def test_matrix_product_pure():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    expected = [[19, 22], [43, 50]]
    result = matrix_product(A, B, "pure")
    assert result == expected, f"Expected {expected}, but got {result}"

@pytest.mark.it("Correctly multiplies two matrices in 'numpy' mode")
def test_matrix_product_numpy():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    expected = np.array([[19, 22], [43, 50]])
    result = matrix_product(A, B, "numpy")
    assert np.array_equal(result, expected), f"Expected {expected}, but got {result}"

# --- Error Handling ---

@pytest.mark.it("Raises ValueError when vectors have different lengths in dot product")
def test_dot_product_invalid_length():
    v1 = [1, 2]
    v2 = [3, 4, 5]
    with pytest.raises(ValueError, match="Vectors must have the same length"):
        dot_product(v1, v2, "pure")

@pytest.mark.it("Raises ValueError when matrix dimensions are incompatible")
def test_matrix_product_invalid_size():
    A = [[1, 2], [3, 4]]
    B = [[5, 6, 7], [8, 9, 10], [11, 12, 13]]
    with pytest.raises(ValueError, match="Incompatible matrix dimensions"):
        matrix_product(A, B, "pure")

@pytest.mark.it("Raises ValueError when mode is invalid")
def test_invalid_mode():
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]

    with pytest.raises(ValueError, match="Invalid mode"):
        dot_product(v1, v2, "invalid_mode")

    with pytest.raises(ValueError, match="Invalid mode"):
        matrix_product(A, B, "invalid_mode")