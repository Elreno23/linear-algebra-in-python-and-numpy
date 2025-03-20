# `06` Determinants and Inverses  

In linear algebra, the **determinant** and the **inverse matrix** are fundamental operations for analyzing matrices and solving systems of equations.


### What is the determinant of a matrix?

The determinant is a number that gives us important information about a matrix. If the determinant of a matrix is 0, it means that the matrix does not have an inverse and cannot be used to solve systems of equations.

The determinant can only be calculated for square matrices (matrices with the same number of rows and columns). Let's see an example with a **\(2 X 2\)** matrix:

$
A =
\begin{bmatrix} 
a & b \\ 
c & d 
\end{bmatrix}
$

The determinant is calculated as follows:

$\text{det}(A) = (1 \cdot 4) - (2 \cdot 3) = 4 - 6 = -2$

✅ Determinant calculation in pure Python (only for 2×2):

```python
def determinant_2x2(A):
    return (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])

A = [[1, 2], [3, 4]]
print(determinant_2x2(A))  # -2
```

✅ Determinant calculation with `NumPy`:

```python
import numpy as np

A = np.array([[1, 2], [3, 4]])
print(np.linalg.det(A))  # -2.0
```

### What is the inverse matrix?

The **inverse matrix** of a matrix \( A \), denoted as $A^{-1}$, is a matrix that satisfies:

$A \times A^{-1} = I$

Where \( I \) is the **identity matrix**, equivalent to "1" in matrices:

$
I =
\begin{bmatrix} 
1 & 0 \\ 
0 & 1 
\end{bmatrix}
$

For a **(2 X 2)** matrix, the inverse is calculated as:

$
A^{-1} = \frac{1}{\text{det}(A)} 
\begin{bmatrix} 
d & -b \\ 
-c & a 
\end{bmatrix}
$

✅ Inverse calculation in pure Python (only 2×2):

```python
def inverse_2x2(A):
    det = determinant_2x2(A)
    if det == 0:
        return "The matrix does not have an inverse"
    
    return [[A[1][1] / det, -A[0][1] / det], 
            [-A[1][0] / det, A[0][0] / det]]

A = [[1, 2], [3, 4]]
print(inverse_2x2(A)) 
```

✅ Inverse calculation with NumPy (supports any matrix size):

```python
import numpy as np

A = np.array([[1, 2], [3, 4]])
print(np.linalg.inv(A))
```
---


## 📝 Instructions

1. Complete the functions `determinant(matrix, mode="pure")` and `inverse_matrix(matrix, mode="pure")` to calculate the determinant and the inverse of a matrix.

    - If `mode="pure"`, use nested lists and manual calculations.
    - If `mode="numpy"`, use `np.linalg.det()` and `np.linalg.inv()`.
    - If the matrix does not have an inverse, return an error message.

2. Test the functions with the example matrix:

    ```python
    matrix = [[1, 2], [3, 4]]

    determinant(matrix, "pure")
    determinant(matrix, "numpy")
    inverse_matrix(matrix, "pure")
    inverse_matrix(matrix, "numpy")
    ```