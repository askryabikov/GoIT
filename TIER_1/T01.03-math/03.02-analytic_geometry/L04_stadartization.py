import numpy as np

# Довільний вектор
v = np.array([3, 4])
print(f"Оригінальний вектор: v = {v}")
print(f"Норма: ||v|| = {np.linalg.norm(v)}")

# Нормалізація
v_normalized = v / np.linalg.norm(v)
print(f"Нормалізований вектор: v̂ = {v_normalized}")
print(f"Норма нормалізованого: ||v̂|| = {np.linalg.norm(v_normalized)}")

# Перевірка: нормалізований вектор має норму 1
print(f"Норма дорівнює 1? {np.isclose(np.linalg.norm(v_normalized), 1.0)}")


# Оригінальний вектор: v = [3 4]
# Норма: ||v|| = 5.0

# Нормалізований вектор: v̂ = [0.6 0.8]
# Норма нормалізованого: ||v̂|| = 1.0
# Норма дорівнює 1? True
