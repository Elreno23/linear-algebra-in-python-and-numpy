# --- Determinant Tests ---

@pytest.mark.it("Correctly calculates the determinant in 'pure' mode")
def test_determinant_pure():
    matrix = [[1, 2], [3, 4]]
    expected = -2
    result = determinant(matrix, "pure")
    assert pytest.approx(result) == expected, f"Expected {expected}, but got {result}"

@pytest.mark.it("Correctly calculates the determinant in 'numpy' mode")
def test_determinant_numpy():
    matrix = [[1, 2], [3, 4]]
    expected = -2
    result = determinant(matrix, "numpy")
    assert pytest.approx(result) == expected, f"Expected {expected}, but got {result}"

# --- Inverse Matrix Tests ---

@pytest.mark.it("Correctly returns the inverse matrix in 'pure' mode")
def test_inverse_matrix_pure():
    matrix = [[1, 2], [3, 4]]
    expected = [[-2.0, 1.0], [1.5, -0.5]]
    result = inverse_matrix(matrix, "pure")
    assert result == expected, f"Expected {expected}, but got {result}"

@pytest.mark.it("Correctly returns the inverse matrix in 'numpy' mode")
def test_inverse_matrix_numpy():
    matrix = [[1, 2], [3, 4]]
    expected = np.array([[-2.0, 1.0], [1.5, -0.5]])
    result = inverse_matrix(matrix, "numpy")
    assert np.allclose(result, expected), f"Expected {expected}, but got {result}"

# --- Error Handling ---

@pytest.mark.it("Raises ValueError when the matrix is not invertible")
def test_non_invertible_matrix():
    singular_matrix = [[1, 2], [2, 4]]  # Determinant = 0
    with pytest.raises(ValueError, match="Matrix is not invertible"):
        inverse_matrix(singular_matrix, "pure")

@pytest.mark.it("Raises ValueError when the mode is invalid")
def test_invalid_mode():
    matrix = [[1, 2], [3, 4]]
    with pytest.raises(ValueError, match="Invalid mode"):
        determinant(matrix, "invalid_mode")
    with pytest.raises(ValueError, match="Invalid mode"):
        inverse_matrix(matrix, "invalid_mode")