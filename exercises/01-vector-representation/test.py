import pytest
import numpy as np
from app import create_vector  # Make sure to import the function from the correct file

@pytest.mark.it("Returns a list when mode is 'pure'")
def test_create_vector_pure():
    result = create_vector([1, 2, 3], "pure")
    assert isinstance(result, list), "Expected a list"

@pytest.mark.it("Returns a NumPy array when mode is 'numpy'")
def test_create_vector_numpy():
    result = create_vector([1, 2, 3], "numpy")
    assert isinstance(result, np.ndarray), "Expected a NumPy ndarray"

@pytest.mark.it("Expected error message to mention 'Invalid mode'")
@pytest.mark.parametrize("invalid_mode", ["invalid", "", None, 123, "matrix", "Pure", "NUMPY"])
def test_compute_eigen_returns_error_string_on_invalid_mode(invalid_mode):
    A = [[3, 2], [1, 4]]
    result = create_vector(A, invalid_mode)
    assert isinstance(result, str), "Expected a string error message"
    assert "Invalid mode".lower() in result.lower(), f"Expected error message to mention 'Invalid mode', but got: {result}"
