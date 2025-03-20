# `05` Transposición de Matrices  

La **transposición de una matriz** es una operación que intercambia sus filas por columnas. Si tenemos una matriz \( A \), su **matriz transpuesta** se denota como \( A^T \).  


Supongamos que tenemos la siguiente matriz:

![image-matrix1](/.learn/assets/matrix1.png)


La matriz transpuesta se veria así:

![image-matrix2](/.learn/assets/matrix2.png)


En otras palabras, **los elementos de la fila \( i \) pasan a la columna \( i \)**.


✅ En código de Python puro (listas anidadas) se veria asi:

  ```python
  A = [[1, 2, 3], [4, 5, 6]]
  transpuesta = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
  print(transpuesta) # [[1, 4], [2, 5], [3, 6]]
  ```
✅ Usando NumPy (con .T):
  ```python
  import numpy as np

  A = np.array([[1, 2, 3], [4, 5, 6]])
  transpuesta = A.T
  print(transpuesta)
  # [[1 4]
  #  [2 5]
  #  [3 6]]
  ```


## 📝 Instrucciones

1. Completa la función `transpose(matrix, mode="pure")` para calcular la transpuesta de una matriz.

    - Si `mode="pure"`, usa listas anidadas.
    - Si `mode="numpy"`, usa NumPy.
    - Si matrix no es válida, lanza un error.

2. Prueba la función con la matriz de ejemplo:

  ```python
  matrix = [[1, 2, 3], [4, 5, 6]]

  transpose(matrix, "pure")
  transpose(matrix, "numpy")
  ```
