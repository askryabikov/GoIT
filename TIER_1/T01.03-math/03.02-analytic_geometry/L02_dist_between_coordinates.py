import numpy as np

# Дві точки на площині (координати)
A = np.array([1, 2])
B = np.array([4, 6])

# Відстань = норма вектора різниці
distance = np.linalg.norm(B - A)

print(f"Точка A: {A}", f"Точка B: {B}")
print(f"Вектор B - A: {B - A}")
print(f"Відстань d(A, B) = ||B - A|| = {distance}")


# Точка A: [1 2] Точка B: [4 6]
# Вектор B - A: [3 4]
# Відстань d(A, B) = ||B - A|| = 5.0
