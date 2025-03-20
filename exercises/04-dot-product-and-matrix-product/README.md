# `04` Dot Product and Matrix Product  

In linear algebra, there are two fundamental types of products:

- **Dot product**: Multiplication of two vectors, resulting in a number. The dot product is obtained by summing the product of their corresponding elements for two vectors of the same size.  

    ![image-vector](/.learn/assets/vectors1.png)

    Thus, their dot product is:

    ![image-result](/.learn/assets/vectors3.png)


    ✅ In pure Python code (using a loop or list comprehension), it would look like this:

    ```python
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]

    dot_product = sum(v1[i] * v2[i] for i in range(len(v1)))
    print(dot_product)  # 32
    ```

    ✅ With NumPy (more efficient and without explicit loops):

    ```python
    import numpy as np

    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])

    dot_product = np.dot(v1, v2)
    print(dot_product)  # 32
    ```



- **Matrix product**: Multiplication between compatible matrices, meaning when the number of columns of the first matrix matches the number of rows of the second, resulting in a new matrix.  

    ![image-vector2](/.learn/assets/vectors4.png)

    The product A×B is calculated as follows:

    ![image-result2](/.learn/assets/vectors5.png)


    ✅ In pure Python (without NumPy):

    ```python
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]

    result = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
    print(result)  # [[19, 22], [43, 50]]
    ```

    ✅ With NumPy (using np.dot):

    ```python
    import numpy as np

    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    result = np.dot(A, B)
    print(result)  # [[19 22] [43 50]]
    ```

## 📝 Instructions

1. Complete the functions `dot_product(v1, v2, mode="pure")` and `matrix_product(A, B, mode="pure")` to perform the dot product and matrix product.

    - If `mode="pure"`, use lists and loops.
    - If `mode="numpy"`, use `np.dot()`.
    - If the sizes of the vectors or matrices are not compatible, raise an error.

2. Test the functions with the following values and display the results in the console.