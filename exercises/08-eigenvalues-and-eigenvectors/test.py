import pytest
import numpy as np
from app import compute_eigen  # Make sure to import the function correctly

@pytest.mark.parametrize("A, mode, expected_eigenvalues", [
    ([[3, 2], [1, 4]], "pure", [5, 2]),  # Test with lists (manual eigenvalues)
    ([[3, 2], [1, 4]], "numpy", np.array([5, 2]))  # Test with NumPy
])
def test_compute_eigen(A, mode, expected_eigenvalues):
    """Verify that compute_eigen returns the correct eigenvalues in both modes."""
    eigenvalues, eigenvectors = compute_eigen(A, mode)
    
    if mode == "pure":
        assert pytest.approx(eigenvalues) == expected_eigenvalues, f"Expected {expected_eigenvalues}, but got {eigenvalues}"
        assert eigenvectors is None, "In 'pure' mode, eigenvectors should not be returned"
    else:
        assert np.allclose(eigenvalues, expected_eigenvalues), f"Expected {expected_eigenvalues}, but got {eigenvalues}"
        assert isinstance(eigenvectors, np.ndarray), "Eigenvectors should be a NumPy array"

def test_compute_eigen_non_square():
    """Verify that an error is raised if the matrix is not square."""
    non_square_A = [[1, 2, 3], [4, 5, 6]]
    with pytest.raises(ValueError, match="Matrix must be square"):
        compute_eigen(non_square_A, "pure")

def test_compute_eigen_invalid_mode():
    """Verify that an error is raised if the mode is invalid."""
    A = [[3, 2], [1, 4]]
    with pytest.raises(ValueError, match="Invalid mode"):
        compute_eigen(A, "invalid_mode")
