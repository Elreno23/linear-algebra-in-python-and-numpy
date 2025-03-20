# `06` Determinantes e Inversas  

En álgebra lineal, el **determinante** y la **matriz inversa** son operaciones fundamentales para analizar matrices y resolver sistemas de ecuaciones.


### ¿Qué es la determinante de una matriz?

El determinante es un número que nos dice información importante sobre una matriz. Si el determinante de una matriz es 0, significa que la matriz no tiene inversa y no se puede usar para resolver sistemas de ecuaciones. 

El determinante solo se puede calcular para matrices cuadradas (matrices con el mismo número de filas y columnas). Veamos un ejemplo con una matriz **\(2 X 2\)**:

$
A =
\begin{bmatrix} 
a & b \\ 
c & d 
\end{bmatrix}
$

El determinante se calcula así:

$\text{det}(A) = (1 \cdot 4) - (2 \cdot 3) = 4 - 6 = -2$

✅ Cálculo del determinante en Python puro (solo para 2×2):

```python
def determinante_2x2(A):
    return (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])

A = [[1, 2], [3, 4]]
print(determinante_2x2(A))  # -2
```

✅ Cálculo del determinante con `NumPy`:

```python
import numpy as np

A = np.array([[1, 2], [3, 4]])
print(np.linalg.det(A))  # -2.0
```

### ¿Qué es la matriz inversa?

La **matriz inversa** de una matriz \( A \), denotada como $A^{-1}$, es una matriz que cumple:

$A \times A^{-1} = I$

Donde \( I \) es la **matriz identidad**, equivalente al "1" en matrices:

$
I =
\begin{bmatrix} 
1 & 0 \\ 
0 & 1 
\end{bmatrix}
$

Para una matriz **(2 X 2)**, la inversa se calcula como:

$
A^{-1} = \frac{1}{\text{det}(A)} 
\begin{bmatrix} 
d & -b \\ 
-c & a 
\end{bmatrix}
$

✅ Cálculo de la inversa en Python puro (solo 2×2):

```python
def inversa_2x2(A):
    det = determinante_2x2(A)
    if det == 0:
        return "La matriz no tiene inversa"
    
    return [[A[1][1] / det, -A[0][1] / det], 
            [-A[1][0] / det, A[0][0] / det]]

A = [[1, 2], [3, 4]]
print(inversa_2x2(A)) 
```

✅ Cálculo de la inversa con NumPy (soporta cualquier tamaño de matriz):

```python
import numpy as np

A = np.array([[1, 2], [3, 4]])
print(np.linalg.inv(A))
```
---


## 📝 Instrucciones

1. Completa las funciones `determinant(matrix, mode="pure")` y `inverse_matrix(matrix, mode="pure")` para calcular el determinante y la inversa de una matriz.

    - Si `mode="pure"`, usa listas anidadas y cálculos manuales.
    - Si `mode="numpy"`, usa `np.linalg.det()` y `np.linalg.inv()`.
    - Si la matriz no tiene inversa, retorna un mensaje de error.

2. Prueba las funciones con la matriz de ejemplo:

    ```python
    matrix = [[1, 2], [3, 4]]

    determinant(matrix, "pure")
    determinant(matrix, "numpy")
    inverse_matrix(matrix, "pure")
    inverse_matrix(matrix, "numpy")
    ```