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
