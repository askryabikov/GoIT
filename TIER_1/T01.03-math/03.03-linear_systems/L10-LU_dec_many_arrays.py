import numpy as np
from scipy import linalg

A = np.array([[2, 1, -1], [4, -1, 2], [-2, 2, 1]], dtype=float)

# Обчислюємо LU-розклад один раз
P, L, U = linalg.lu(A)

# Розв'язуємо для п'яти різних правих частин
b_vectors = [
    np.array([3, 13, 4]),
    np.array([1, 5, 2]),
    np.array([0, 0, 1]),
    np.array([7, 3, -2]),
    np.array([2, 8, 5])
]

print("Розв'язуємо 5 систем з однією матрицею A:")
for i, b in enumerate(b_vectors, 1):
    Pb = P @ b
    y = linalg.solve_triangular(L, Pb, lower=True)
    x = linalg.solve_triangular(U, y, lower=False)
    print(f"Система {i}: b = {b}, x = {x}")

# Розв'язуємо 5 систем з однією матрицею A:
# Система 1: b = [ 3 13  4], x = [2.08333333 2.33333333 3.5       ]
# Система 2: b = [1 5 2], x = [0.75 1.   1.5 ]
# Система 3: b = [0 0 1], x = [-0.04166667  0.33333333  0.25      ]
# Система 4: b = [ 7  3 -2], x = [ 1.91666667  1.66666667 -1.5       ]
# Система 5: b = [2 8 5], x = [1.20833333 2.33333333 2.75      ]



