# `07` Solving Systems of Linear Equations  

A **system of linear equations** is a set of equations that share unknowns. Solving it means finding the values of those unknowns that satisfy all the equations simultaneously.

### How is a system of equations represented with matrices?  

A system of linear equations in two variables, for example:

$
\begin{cases} 
2x + 3y = 5 \\ 
4x - y = 1 
\end{cases}
$

can be expressed in **matrix form** as:

$
Ax = b
$

Where:

$
A = \begin{bmatrix} 2 & 3 \\ 4 & -1 \end{bmatrix}, \quad
x = \begin{bmatrix} x \\ y \end{bmatrix}, \quad
b = \begin{bmatrix} 5 \\ 1 \end{bmatrix}
$

Here:
- \( A \) is the **coefficient matrix**.
- \( x \) is the **vector of unknowns**.
- \( b \) is the **result vector**.

The solution of the system seeks a vector \( x \) that satisfies the equation **\( Ax = b \)**.



### Geometric Interpretation  

In the case of a \( 2 X 2 \) system, each equation represents a **line** in the plane. Solving the system means finding the point where **both lines intersect**.  

In a **\( 3 X 3 \)** system, each equation represents a **plane in space**, and the solution is the **point where the three planes intersect**.


## Solution Methods  

### **Manual Method (for understanding)**  

If \( A \) is **invertible**, the solution is obtained as:

$
x = A^{-1} b
$

Where $A^{-1}$ is the **inverse matrix** of \( A \).

For the system:

$$
\begin{bmatrix} 2 & 3 \\ 4 & -1 \end{bmatrix} 
\begin{bmatrix} x \\ y \end{bmatrix} 
= 
\begin{bmatrix} 5 \\ 1 \end{bmatrix}
$$

We calculate the inverse of \( A \) and multiply it by \( b \) to obtain \( x \).



### **Using NumPy (`np.linalg.solve()` 🚀)**  

The best way to solve **\( Ax = b \)** in Python is with `np.linalg.solve(A, b)`, which directly finds the solution without needing to calculate the inverse of the matrix (more efficient and stable).

```python
import numpy as np

# Define the coefficient matrix A and the result vector b
A = np.array([[2, 3], [4, -1]])
b = np.array([5, 1])

# Solve the system Ax = b
x = np.linalg.solve(A, b)

print("Solution:", x)
```

---

## 📝 Instructions  

1. **Complete the function `solve_system(A, b, mode="numpy")`** to solve \( Ax = b \).  
    - If `mode="pure"`, use the inverse of \( A \) to calculate \( x \).  
    - If `mode="numpy"`, use `np.linalg.solve(A, b)`.  
    - If \( A \) is not invertible, return an error message.  

2. **Test the function** with the system of equations:

    ```python
    A = [[2, 3], [4, -1]]
    b = [5, 1]

    solve_system(A, b, "pure")
    solve_system(A, b, "numpy")
    ```