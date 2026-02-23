import numpy as np

# Система 4 рівняння, 4 невідомих
A_4d = np.array([
    [1, 2, -1, 3],
    [2, -1, 1, 1],
    [1, 1, 1, -1],
    [3, 1, -2, 2]
])
b_4d = np.array([5, 4, 6, 7])

# Розв'язуємо
x_sol_4d = np.linalg.solve(A_4d, b_4d)

print(f"Розв'язок:")
for i, val in enumerate(x_sol_4d, 1):
    print(f"  x_{i} = {val:.4f}")

# Перевірка розв'язку
residual = A_4d @ x_sol_4d - b_4d
print(f"Похибка: {np.linalg.norm(residual):.2e}")


# Розв'язок:
#   x_1 = 2.5455
#   x_2 = 2.0909
#   x_3 = 1.1818
#   x_4 = -0.1818
# Похибка: 1.26e-15