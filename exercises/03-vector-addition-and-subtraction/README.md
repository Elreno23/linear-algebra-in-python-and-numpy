# `03` Vector Addition and Subtraction  

**Vector addition and subtraction** in linear algebra is performed **element by element**. 

If we have the following vectors:  

![vectors1-img](/.learn/assets/vectors1.png)

Then the addition would look like this:  

![vectors2-img](/.learn/assets/vectors2.png)


In Python, we can implement **vector addition and subtraction** in two ways:  

- **Using pure Python lists** (iterating over the elements).

    ```python
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]

    sum_result = [v1[i] + v2[i] for i in range(len(v1))]  # [5, 7, 9]
    ```
- Using `NumPy`, which allows performing the operation directly, it would be like this:

    ```python
    import numpy as np

    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])

    sum_result = v1 + v2
    sub_result = v1 - v2

    print("Sum:", sum_result)  # [5 7 9]
    print("Subtraction:", sub_result)  # [-3 -3 -3]
    ```


## 📝 Instructions

1. Complete the functions `sum_vectors(v1, v2, mode="pure")` and `subtract_vectors(v1, v2, mode="pure")` to perform the addition and subtraction of two vectors.

    - If `mode="pure"`, use lists and loops.
    - If `mode="numpy"`, use NumPy operations.
    - If the vectors have different lengths, raise an error.

2. Test the functions with the vectors [1, 2, 3] and [4, 5, 6] in both modes and display the results in the console.