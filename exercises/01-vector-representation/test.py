import pytest
import numpy as np
from app import create_vector  # Make sure to import the function from the correct file

@pytest.mark.parametrize("lst, mode, expected_type", [
    ([1, 2, 3], "pure", list),  # Test in "pure" mode
    ([1, 2, 3], "numpy", np.ndarray),  # Test in "numpy" mode
])
def test_create_vector(lst, mode, expected_type):
    result = create_vector(lst, mode)
    assert isinstance(result, expected_type), f"Expected {expected_type}, but got {type(result)}"

def test_create_vector_invalid_mode():
    with pytest.raises(ValueError, match="Invalid mode"):
        create_vector([1, 2, 3], "invalid")  # Invalid mode should raise an error
