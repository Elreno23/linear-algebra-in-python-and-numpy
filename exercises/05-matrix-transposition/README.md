# `05` Matrix Transposition  

**Matrix transposition** is an operation that swaps its rows with columns. If we have a matrix \( A \), its **transposed matrix** is denoted as \( A^T \).  

Suppose we have the following matrix:

![image-matrix1](/.learn/assets/matrix1.png)

The transposed matrix would look like this:

![image-matrix2](/.learn/assets/matrix2.png)

In other words, **the elements of row \( i \) become the elements of column \( i \)**.

✅ In pure Python code (nested lists), it would look like this:

```python
A = [[1, 2, 3], [4, 5, 6]]
transposed = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
print(transposed) # [[1, 4], [2, 5], [3, 6]]
```

✅ Using NumPy (with .T):

```python
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
transposed = A.T
print(transposed)
# [[1 4]
#  [2 5]
#  [3 6]]
```

## 📝 Instructions

1. Complete the function `transpose(matrix, mode="pure")` to calculate the transpose of a matrix.

    - If `mode="pure"`, use nested lists.
    - If `mode="numpy"`, use NumPy.

2. Test the function with the example matrix:

    ```python
    matrix = [[1, 2, 3], [4, 5, 6]]

    transpose(matrix, "pure")
    transpose(matrix, "numpy")
    ```
