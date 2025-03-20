# `02` Matrix Representation

A **matrix** in linear algebra is a two-dimensional structure organized in **rows** and **columns**. It can be represented in Python using **nested lists** or **NumPy arrays**.

### How to represent a matrix in Python
- Using pure Python (nested lists)
    ```python
    pure_matrix = [[1, 2, 3], [4, 5, 6]]
    ```
    > Each row is a list, and all rows are within another list.

- Using NumPy
    ```python
    import numpy as np

    numpy_matrix = np.array([[1, 2, 3], [4, 5, 6]])
    ```

## 📝 Instructions

1. Complete the function `create_matrix(n, m, mode="pure")` to generate a matrix of size `n * m` with random values.

    - If `mode="pure"`, generate a nested list with random numbers.
    - If `mode="numpy"`, generate a NumPy array with random numbers.
    - If `mode` is not valid, raise an error.

2. Test the function with a sample 3x3 matrix in both modes and display the result in the console.
