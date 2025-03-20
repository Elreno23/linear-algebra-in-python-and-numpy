# `08` Eigenvalues and Eigenvectors  

In linear algebra, the **eigenvalues** and **eigenvectors** of a square matrix \( A \) are fundamental to understanding how it transforms space.

An **eigenvector** \( v \) of \( A \) is a **non-zero** vector that, when multiplied by \( A \), only changes its **magnitude**, but not its direction:

$
A v = \lambda v
$

Where:
- $ v $ is an **eigenvector**.
- $ \lambda $ is the **eigenvalue** associated with $ v $.
- $ A v $ is simply $ v $ scaled by $ \lambda $.

The eigenvalues indicate **how much the eigenvector is stretched or shrunk** when the transformation \( A \) is applied.

## Calculation of Eigenvalues and Eigenvectors  

To find the eigenvalues, we solve the **characteristic equation**:

$
\det(A - \lambda I) = 0
$

For each eigenvalue \( \lambda \), we find its eigenvector by solving:

$
(A - \lambda I) v = 0
$

**Example with a $2 \times 2$ matrix**  

Given the matrix:

$
A = \begin{bmatrix} 3 & 2 \\ 1 & 4 \end{bmatrix}
$

The eigenvalues and eigenvectors can be calculated manually, but in Python, we use `np.linalg.eig()`.

---

### **In pure Python (manual for $ 2 \times 2$)**
```python
def compute_eigenvalues_2x2(A):
    """Calculates the eigenvalues of a 2x2 matrix."""
    a, b = A[0]
    c, d = A[1]

    # Solve det(A - λI) = 0
    lambda1 = ((a + d) + ((a + d)**2 - 4*(a*d - b*c))**0.5) / 2
    lambda2 = ((a + d) - ((a + d)**2 - 4*(a*d - b*c))**0.5) / 2

    return [lambda1, lambda2]

# Example matrix
A = [[3, 2], [1, 4]]
print("Manual eigenvalues:", compute_eigenvalues_2x2(A))
```

This method only works for 2×2 matrices.

### Using NumPy `np.linalg.eig()`
The most efficient way to calculate eigenvalues and eigenvectors in Python is with `np.linalg.eig(A)`, which returns both directly.

```python
import numpy as np

A = np.array([[3, 2], [1, 4]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors (as columns):")
print(eigenvectors)
```

## 📝 Instructions

1. Complete the function `compute_eigen(A, mode="numpy")` to calculate the eigenvalues and eigenvectors.

    - If `mode="pure"`, calculate only the eigenvalues manually (for 2×2).
    - If `mode="numpy"`, use `np.linalg.eig(A)`.
    - If A is not square, return an error.

2. Test the function with the example matrix:

```python
A = [[3, 2], [1, 4]]
compute_eigen(A, "pure")
compute_eigen(A, "numpy")
```
