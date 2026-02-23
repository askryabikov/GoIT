import numpy as np

# Визначаємо систему
A = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
], dtype=float)

b = np.array([8, -11, -3], dtype=float)

# Розв'язуємо систему
x = np.linalg.solve(A, b)

print(f"Розв'язок: x = {x}")

# Розв'язок: x = [ 2.  3. -1.]

