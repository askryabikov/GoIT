import numpy as np

A = np.array([
    [2, 1, -1],
    [1, 3, 2],
    [-1, 2, 1]
], dtype=float)

det_A = np.linalg.det(A)
print(f"Визначник det(A) = {det_A:.4f}")

if abs(det_A) > 1e-10:
    print("Обернена матриця існує")
    
    A_inv = np.linalg.inv(A)
    print("Обернена матриця:")
    print(A_inv)
    
    # Розв'язуємо систему
    b = np.array([8, 13, 5])
    x = A_inv @ b
    
    print(f"Розв'язок системи через обернену матрицю:")
    print(f"x = {x}")
    
    # Порівняємо з np.linalg.solve
    x_solve = np.linalg.solve(A, b)
    print(f"Розв'язок через np.linalg.solve:")
    print(f"x = {x_solve}")
    
    print(f"Різниця між методами: {np.linalg.norm(x - x_solve):.2e}")


# Визначник det(A) = -10.0000
# Обернена матриця існує

# Обернена матриця:
# [[ 0.1  0.3 -0.5]
#  [ 0.3 -0.1  0.5]
#  [-0.5  0.5 -0.5]]

# Розв'язок системи через обернену матрицю:
# x = [2.2 3.6 0. ]

# Розв'язок через np.linalg.solve:
# x = [ 2.2  3.6 -0. ]

# Різниця між методами: 9.93e-16
