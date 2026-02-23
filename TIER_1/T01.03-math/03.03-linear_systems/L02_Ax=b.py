import numpy as np

# Система з 4 рівнянь і 4 невідомих
A = np.array([
    [2, 1, -1, 3],
    [1, 3, 2, -1],
    [3, -1, 1, 2],
    [1, 2, 3, 1]
])

b = np.array([7, 8, 5, 10])

x = np.linalg.solve(A, b)

print(f"Розв'язок:")
for i, val in enumerate(x, 1):
    print(f"  x_{i} = {val:.4f}")

# Перевірка
solution_error = A @ x - b
print(f"Похибка розв'язку: {np.linalg.norm(solution_error):.2e}")

# Розв'язок:
#   x_1 = 1.0000
#   x_2 = 2.0000
#   x_3 = 1.2000
#   x_4 = 1.4000
# Похибка розв'язку: 1.26e-15