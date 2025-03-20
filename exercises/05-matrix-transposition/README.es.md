# `05` Transposición de Matrices  

La **transposición de una matriz** es una operación que intercambia sus filas por columnas. Si tenemos una matriz \( A \), su **matriz transpuesta** se denota como \( A^T \).  


## 📌 ¿Qué es la Matriz Transpuesta?  

Dada una matriz:

\[
A = \begin{bmatrix} 
1 & 2 & 3 \\ 
4 & 5 & 6 
\end{bmatrix}
\]

Su transpuesta \( A^T \) es:

\[
A^T = \begin{bmatrix} 
1 & 4 \\ 
2 & 5 \\ 
3 & 6 
\end{bmatrix}
\]

En otras palabras, **los elementos de la fila \( i \) pasan a la columna \( i \)**.

---

## 📌 Representación en Python  

Podemos transponer una matriz de dos formas:  

- **Usando Python puro (listas anidadas)**:  
  ```python
  A = [[1, 2, 3], [4, 5, 6]]
  transpuesta = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
  print(transpuesta)
  # [[1, 4], [2, 5], [3, 6]]
Usando NumPy (con .T):
python
Copiar código
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
transpuesta = A.T
print(transpuesta)
# [[1 4]
#  [2 5]
#  [3 6]]
📝 Instrucciones
Completa la función transpose(matrix, mode="pure") para calcular la transpuesta de una matriz.

Si mode="pure", usa listas anidadas.
Si mode="numpy", usa NumPy.
Si matrix no es válida, lanza un error.
Prueba la función con la matriz de ejemplo:

python
Copiar código
matrix = [[1, 2, 3], [4, 5, 6]]
transpose(matrix, "pure")
transpose(matrix, "numpy")
