# `01` Vector Representation  

A **vector** in linear algebra is a list of numbers that represent a magnitude in a space. In Python, we can work with vectors using **lists** or **NumPy arrays**.  

### What is NumPy?  
NumPy (*Numerical Python*) is a library optimized for mathematical calculations, allowing efficient manipulation of vectors and matrices.  

In this exercise, you will learn to **represent vectors in Python** in two ways:  
- Using Python lists (pure Python).  

    ```python
    pure_vector = [3, 4, 5]
    ```
- Using NumPy arrays, which optimize numerical calculations.

    ```python
    import numpy as np

    numpy_vector = np.array([3, 4, 5])
    ```


## 📝 Instructions  

1. **Complete the function `create_vector(lst, mode="pure")`** so that it receives a list of numbers and returns a vector.  
    - If `mode="pure"`, return a **normal Python list**.  
    - If `mode="numpy"`, return a **NumPy array**.  
    - If `mode` is not valid, raise an error.  

2. **Test the function** with a sample list `[1, 2, 3]` in both modes and display the result in the console.  

