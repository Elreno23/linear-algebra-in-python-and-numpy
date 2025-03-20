# `03` Suma y resta de vectores  

La **suma y resta de vectores** en álgebra lineal se realiza **elemento a elemento**. 

Si tenemos los siguientes vectores:  

![vectors1-img](/.learn/assets/vectors1.png)

Entonces la suma seria algo así:  

![vectors2-img](/.learn/assets/vectors2.png)


En python, podemos implementar la **suma y resta de vectores** de dos formas:  

- **Usando listas en Python puro** (iterando sobre los elementos).

    ```python
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]

    sum_result = [v1[i] + v2[i] for i in range(len(v1))]  # [5, 7, 9]
    ```
- Usando `NumPy`, que permite realizar la operación directamente, seria asi:

    ```python
    import numpy as np

    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])

    sum_result = v1 + v2
    sub_result = v1 - v2

    print("Suma:", sum_result)  # [5 7 9]
    print("Resta:", sub_result)  # [-3 -3 -3]
    ```


## 📝 Instrucciones

1. Completa las funciones `sum_vectors(v1, v2, mode="pure")` y `subtract_vectors(v1, v2, mode="pure")` para realizar la suma y resta de dos vectores.

    - Si `mode="pure"`, usa listas y bucles.
    - Si `mode="numpy"`, usa operaciones de NumPy.
    - Si los vectores tienen diferentes longitudes, lanza un error.

2. Prueba las funciones con los vectores [1, 2, 3] y [4, 5, 6] en ambos modos y muestra los resultados en consola.