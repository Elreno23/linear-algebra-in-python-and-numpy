# `08` Autovalores y Autovectores  

En álgebra lineal, los **autovalores** y **autovectores** de una matriz cuadrada \( A \) son fundamentales para entender cómo esta transforma el espacio.

Un **autovector** \( v \) de \( A \) es un vector **no nulo** que, al multiplicarse por \( A \), solo cambia su **magnitud**, pero no su dirección:

$
A v = \lambda v
$

Donde:
- $ v $ es un **autovector**.
- $ \lambda $ es el **autovalor** asociado a $ v $.
- $ A v$ es simplemente $ v $ escalado por $ \lambda $.

Los autovalores indican **cuánto se estira o encoge** el autovector cuando se aplica la transformación $ A$.



## Cálculo de Autovalores y Autovectores  

Para encontrar los autovalores, resolvemos la **ecuación característica**:

$
\det(A - \lambda I) = 0
$

Para cada autovalor \( \lambda \), encontramos su autovector resolviendo:

$
(A - \lambda I) v = 0
$

**Ejemplo con una matriz $2 \times 2$**  

Dada la matriz:

$
A = \begin{bmatrix} 3 & 2 \\ 1 & 4 \end{bmatrix}
$

Los autovalores y autovectores se pueden calcular manualmente, pero en Python usamos `np.linalg.eig()`.

---


### **En Python puro (manual para $ 2 \times 2$**
```python
def compute_eigenvalues_2x2(A):
    """Calcula los autovalores de una matriz 2x2."""
    a, b = A[0]
    c, d = A[1]

    # Resolvemos det(A - λI) = 0
    lambda1 = ((a + d) + ((a + d)**2 - 4*(a*d - b*c))**0.5) / 2
    lambda2 = ((a + d) - ((a + d)**2 - 4*(a*d - b*c))**0.5) / 2

    return [lambda1, lambda2]

# Matriz de ejemplo
A = [[3, 2], [1, 4]]
print("Autovalores manuales:", compute_eigenvalues_2x2(A))
```

Este método solo funciona para matrices 2×2.

###  Usando NumPy `np.linalg.eig()`
La forma más eficiente de calcular autovalores y autovectores en Python es con `np.linalg.eig(A)`, que devuelve ambos directamente.

```python
import numpy as np

A = np.array([[3, 2], [1, 4]])

# Calculamos autovalores y autovectores
autovalores, autovectores = np.linalg.eig(A)

print("Autovalores:", autovalores)
print("Autovectores (como columnas):")
print(autovectores)
```

## 📝 Instrucciones

1. Completa la función `compute_eigen(A, mode="numpy")` para calcular los autovalores y autovectores.

    - Si `mode="pure"`, calcula solo los autovalores manualmente (para 2×2).
    - Si `mode="numpy"`, usa `np.linalg.eig(A)`.
    - Si A no es cuadrada, retorna un error.

2. Prueba la función con la matriz de ejemplo:

```python
A = [[3, 2], [1, 4]]
compute_eigen(A, "pure")
compute_eigen(A, "numpy")
```