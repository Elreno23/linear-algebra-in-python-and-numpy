# `07` Resolución de Sistemas de Ecuaciones Lineales  

Un **sistema de ecuaciones lineales** es un conjunto de ecuaciones que comparten incógnitas. Resolverlo significa encontrar los valores de esas incógnitas que satisfacen todas las ecuaciones al mismo tiempo.

### ¿Cómo se representa un sistema de ecuaciones con matrices?  

Un sistema de ecuaciones lineales en dos variables, por ejemplo:

$
\begin{cases} 
2x + 3y = 5 \\ 
4x - y = 1 
\end{cases}
$

se puede expresar en **forma matricial** como:

$
Ax = b
$

Donde:

$
A = \begin{bmatrix} 2 & 3 \\ 4 & -1 \end{bmatrix}, \quad
x = \begin{bmatrix} x \\ y \end{bmatrix}, \quad
b = \begin{bmatrix} 5 \\ 1 \end{bmatrix}
$

Aquí:
- \( A \) es la **matriz de coeficientes**.
- \( x \) es el **vector de incógnitas**.
- \( b \) es el **vector de resultados**.

La solución del sistema busca un vector \( x \) que satisfaga la ecuación **\( Ax = b \)**.



### Interpretación geométrica  

En el caso de un sistema \( 2 X 2 \), cada ecuación representa una **recta** en el plano. Resolver el sistema significa encontrar el punto donde **ambas rectas se cruzan**.  

En un sistema **\( 3 X 3 \)**, cada ecuación representa un **plano en el espacio**, y la solución es el **punto donde los tres planos se intersectan**.


## Métodos de Resolución  

### **Método manual (para comprensión)**  

Si \( A \) es **invertible**, la solución se obtiene como:

$
x = A^{-1} b
$

Donde $A^{-1}$ es la **matriz inversa** de \( A \).

Para el sistema:

$$
\begin{bmatrix} 2 & 3 \\ 4 & -1 \end{bmatrix} 
\begin{bmatrix} x \\ y \end{bmatrix} 
= 
\begin{bmatrix} 5 \\ 1 \end{bmatrix}
$$

Calculamos la inversa de \( A \) y la multiplicamos por \( b \) para obtener \( x \).



### **Usando NumPy (`np.linalg.solve()` 🚀)**  

La mejor forma de resolver **\( Ax = b \)** en Python es con `np.linalg.solve(A, b)`, que encuentra directamente la solución sin necesidad de calcular la inversa de la matriz (más eficiente y estable).

```python
import numpy as np

# Definir la matriz de coeficientes A y el vector de resultados b
A = np.array([[2, 3], [4, -1]])
b = np.array([5, 1])

# Resolver el sistema Ax = b
x = np.linalg.solve(A, b)

print("Solución:", x)
```

---

## 📝 Instrucciones  

1. **Completa la función `solve_system(A, b, mode="numpy")`** para resolver \( Ax = b \).  
   - Si `mode="pure"`, usa la inversa de \( A \) para calcular \( x \).  
   - Si `mode="numpy"`, usa `np.linalg.solve(A, b)`.  
   - Si \( A \) no es invertible, retorna un mensaje de error.  

2. **Prueba la función** con el sistema de ecuaciones:

   ```python
   A = [[2, 3], [4, -1]]
   b = [5, 1]

   solve_system(A, b, "pure")
   solve_system(A, b, "numpy")
   ```