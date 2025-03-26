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

@pytest.mark.it("Returns an error message when vectors have different lengths in dot_product")
def test_dot_product_invalid_length():
    v1 = [1, 2]
    v2 = [3, 4, 5]
    result = dot_product(v1, v2, "pure")
    assert isinstance(result, str), "Expected a string error message from dot_product"
    assert "same length" in result.lower(), f"Expected error message to mention 'same length', but got: {result}"

@pytest.mark.it("Returns an error message when matrix dimensions are incompatible in matrix_product")
def test_matrix_product_invalid_size():
    A = [[1, 2], [3, 4]]
    B = [[5, 6, 7], [8, 9, 10], [11, 12, 13]]
    result = matrix_product(A, B, "pure")
    assert isinstance(result, str), "Expected a string error message from matrix_product"
    assert "incompatible matrix dimensions" in result.lower(), f"Expected error message to mention 'incompatible matrix dimensions', but got: {result}"

@pytest.mark.it("Returns an error message when an invalid mode is passed to dot_product")
@pytest.mark.parametrize("invalid_mode", ["invalid", "", None, 123, "Dot", "NUMPY"])
def test_dot_product_invalid_mode(invalid_mode):
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    result = dot_product(v1, v2, invalid_mode)
    assert isinstance(result, str), "Expected a string error message from dot_product"
    assert "invalid mode" in result.lower(), f"Expected error message to mention 'Invalid mode', but got: {result}"

@pytest.mark.it("Returns an error message when an invalid mode is passed to matrix_product")
@pytest.mark.parametrize("invalid_mode", ["invalid", "", None, 123, "Product", "PURE"])
def test_matrix_product_invalid_mode(invalid_mode):
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    result = matrix_product(A, B, invalid_mode)
    assert isinstance(result, str), "Expected a string error message from matrix_product"
    assert "invalid mode" in result.lower(), f"Expected error message to mention 'Invalid mode', but got: {result}"