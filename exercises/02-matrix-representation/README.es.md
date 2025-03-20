# `02` Representación de Matrices 

Una **matriz** en álgebra lineal es una estructura bidimensional organizada en **filas** y **columnas**. Se puede representar en Python usando **listas anidadas** o **arrays de NumPy**. 


### Cómo representar una matriz en Python
- Usando Python puro (listas anidadas)
    ```python
    matriz_pura = [[1, 2, 3], [4, 5, 6]]
    ```
    > Cada fila es una lista, y todas están dentro de otra lista.

- Usando NumPy
    ```python
    import numpy as np

    matriz_numpy = np.array([[1, 2, 3], [4, 5, 6]])
    ```

## 📝 Instrucciones  

1. Completa la función `create_matrix(n, m, mode="pure")` para que genere una matriz de tamaño `n * m` con valores aleatorios.

    - Si `mode="pure"`, genera una lista anidada con números aleatorios.
    - Si `mode="numpy"`, genera un array de NumPy con números aleatorios.
    - Si `mode` no es válido, lanza un error.

2. Prueba la función con una matriz de ejemplo de 3x3 en ambos modos y muestra el resultado en consola.