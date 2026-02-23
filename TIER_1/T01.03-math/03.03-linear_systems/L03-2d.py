import numpy as np
import matplotlib.pyplot as plt

# Матриця коефіцієнтів та вектор правої частини
A = np.array([
    [2, 1],
    [1, -1]
])
b = np.array([5, 1])

# Розв'язуємо систему
x_solution = np.linalg.solve(A, b)
print(f"Розв'язок системи: x₁ = {x_solution[0]:.2f}, x₂ = {x_solution[1]:.2f}")


# Розв'язок системи: x₁ = 2.00, x₂ = 1.00
