import numpy as np

# Ортогональний базис для R²
v1 = np.array([3, 0])
v2 = np.array([0, 4])

print("Ортогональний базис:")
print(f"  v1 = {v1}, ||v1|| = {np.linalg.norm(v1)}")
print(f"  v2 = {v2}, ||v2|| = {np.linalg.norm(v2)}")

# Нормалізуємо вектори
u1 = v1 / np.linalg.norm(v1)
u2 = v2 / np.linalg.norm(v2)

print("Ортонормований базис:")
print(f"  u1 = {u1}, ||u1|| = {np.linalg.norm(u1):.4f}")
print(f"  u2 = {u2}, ||u2|| = {np.linalg.norm(u2):.4f}")

# Коефіцієнти ортонормованого базису
w = np.array([6, 8])
beta1 = w @ u1
beta2 = w @ u2

print(f"Виразимо w = {w} через ортонормований базис:")
print(f"w = {beta1:.2f}*u1 + {beta2:.2f}*u2")


# Ортогональний базис:
#   v1 = [3 0], ||v1|| = 3.0
#   v2 = [0 4], ||v2|| = 4.0

# Ортонормований базис:
#   u1 = [1. 0.], ||u1|| = 1.0000
#   u2 = [0. 1.], ||u2|| = 1.0000

# Виразимо w = [6 8] через ортонормований базис:
# w = 6.00*u1 + 8.00*u2
