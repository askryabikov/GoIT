import numpy as np

A = np.array([
    [1, 1],
    [2, 1],
    [3, 1]
], dtype=float)

b = np.array([2, 3, 5], dtype=float)

# Розв'язуємо методом найменших квадратів
result = np.linalg.lstsq(A, b, rcond=None)

x_hat = result[0]
residuals = result[1]

print(f"Розв'язок {x_hat}")
print(f"Сума квадратів похибок: {residuals[0]:.6f}")



# Розв'язок [1.5        0.33333333]
# Сума квадратів похибок: 0.166667
