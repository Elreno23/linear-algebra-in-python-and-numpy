import pytest
import numpy as np
from app import sum_vectors, subtract_vectors  # Make sure to import the functions correctly

@pytest.mark.it("Correctly sums two vectors in 'pure' mode")
def test_sum_vectors_pure():
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    expected = [5, 7, 9]
    result = sum_vectors(v1, v2, "pure")
    assert result == expected, f"Expected {expected}, but got {result}"

@pytest.mark.it("Correctly sums two vectors in 'numpy' mode")
def test_sum_vectors_numpy():
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    expected = np.array([5, 7, 9])
    result = sum_vectors(v1, v2, "numpy")
    assert np.array_equal(result, expected), f"Expected {expected}, but got {result}"



@pytest.mark.it("Correctly subtracts two vectors in 'pure' mode")
def test_subtract_vectors_pure():
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    expected = [-3, -3, -3]
    result = subtract_vectors(v1, v2, "pure")
    assert result == expected, f"Expected {expected}, but got {result}"

@pytest.mark.it("Correctly subtracts two vectors in 'numpy' mode")
def test_subtract_vectors_numpy():
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    expected = np.array([-3, -3, -3])
    result = subtract_vectors(v1, v2, "numpy")
    assert np.array_equal(result, expected), f"Expected {expected}, but got {result}"



@pytest.mark.it("Raises ValueError when vectors have different lengths")
def test_vectors_different_lengths():
    v1 = [1, 2, 3]
    v2 = [4, 5]
    with pytest.raises(ValueError, match="Vectors must have the same length"):
        sum_vectors(v1, v2, "pure")
    with pytest.raises(ValueError, match="Vectors must have the same length"):
        subtract_vectors(v1, v2, "numpy")

@pytest.mark.it("Returns an error message when an invalid mode is passed to sum_vectors")
@pytest.mark.parametrize("invalid_mode", ["invalid", "", None, 123, "matrix", "Pure", "NUMPY"])
def test_sum_vectors_invalid_mode(invalid_mode):
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]

    result = sum_vectors(v1, v2, invalid_mode)

    assert isinstance(result, str), "Expected a string error message from sum_vectors"
    assert "Invalid mode".lower() in result.lower(), f"Expected error message to mention 'Invalid mode', but got: {result}"

@pytest.mark.it("Returns an error message when an invalid mode is passed to subtract_vectors")
@pytest.mark.parametrize("invalid_mode", ["invalid", "", None, 123, "matrix", "Pure", "NUMPY"])
def test_subtract_vectors_invalid_mode(invalid_mode):
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]

    result = subtract_vectors(v1, v2, invalid_mode)

    assert isinstance(result, str), "Expected a string error message from subtract_vectors"
    assert "Invalid mode".lower() in result.lower(), f"Expected error message to mention 'Invalid mode', but got: {result}"