import numpy as np

# П'ятивимірний вектор
w = np.array([1, -2, 3, 0, 4])
norm_w = np.linalg.norm(w)
print(f"Вектор w = {w}")
print(f"Норма ||w|| = {norm_w:.2f}")


# Вектор w = [ 1 -2  3  0  4]
# Норма ||w|| = 5.48
