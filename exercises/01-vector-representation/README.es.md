# `01` Representación de Vectores  

Un **vector** en álgebra lineal es una lista de números que representan una magnitud en un espacio. En Python, podemos trabajar con vectores usando **listas** o **arrays de NumPy**.  

### ¿Qué es NumPy?  
NumPy (*Numerical Python*) es una biblioteca optimizada para cálculos matemáticos, que permite manipular vectores y matrices de manera eficiente.  


En este ejercicio, aprenderás a **representar vectores en Python** de dos maneras:  
- Usando listas de Python (Python puro).  

   ```python
   pure_vector = [3, 4, 5]
   ```
- Usando arrays de NumPy, que optimizan los cálculos numéricos.

   ```python
   import numpy as np

   numpy_vector = np.array([3, 4, 5])
   ```


## 📝 Instrucciones  

1. **Completa la función `create_vector(lst, mode="pure")`** para que reciba una lista de números y devuelva un vector.  
   - Si `mode="pure"`, retorna una **lista normal** de Python.  
   - Si `mode="numpy"`, retorna un **array de NumPy**.  

2. **Prueba la función** con una lista de ejemplo `[1, 2, 3]` en ambos modos y muestra el resultado en consola.  
