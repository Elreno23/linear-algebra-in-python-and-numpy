# `04` Producto Escalar y Producto Matricial  

En álgebra lineal, existen dos tipos de productos fundamentales:

- **Producto escalar**: Multiplicación de dos vectores, resultando en un número. Entre dos vectores del mismo tamaño se obtiene el producto escalar, sumando el producto de sus elementos correspondientes.  

    ![image-vector](/.learn/assets/vectors1.png)

    Entonces, su producto escalar es:

    ![image-result](/.learn/assets/vectors3.png)


    ✅ En código de Python puro (usando un bucle o comprensión de listas) se veria así:

    ```python
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]

    dot_product = sum(v1[i] * v2[i] for i in range(len(v1)))
    print(dot_product)  # 32
    ```

    ✅ Con NumPy (más eficiente y sin bucles explícitos):

    ```python
    import numpy as np

    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])

    dot_product = np.dot(v1, v2)
    print(dot_product)  # 32
    ```



- **Producto matricial**: Multiplicación entre matrices compatibles, es decir, cuando el número de columnas de la primera matriz coincide con el número de filas de la segunda y esto da como resultado una nueva matriz.  

    ![image-vector2](/.learn/assets/vectors4.png)

    El producto A×B se calcula así:

    ![image-result2](/.learn/assets/vectors5.png)


    ✅ En Python puro (sin NumPy):

    ```python
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]

    result = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
    print(result)  # [[19, 22], [43, 50]]
    ```

    ✅ Con NumPy (usando np.dot):

    ```python
    import numpy as np

    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    result = np.dot(A, B)
    print(result)  # [[19 22] [43 50]]
    ```

## 📝 Instrucciones

1. Completa las funciones `dot_product(v1, v2, mode="pure")` y `matrix_product(A, B, mode="pure")` para realizar el producto escalar y el producto matricial.

    - Si `mode="pure"`, usa listas y bucles.
    - Si `mode="numpy"`, usa `np.dot()`.
    - Si los tamaños de los vectores o matrices no son compatibles, lanza un error.

2. Prueba las funciones con los siguientes valores y muestra los resultados en consola