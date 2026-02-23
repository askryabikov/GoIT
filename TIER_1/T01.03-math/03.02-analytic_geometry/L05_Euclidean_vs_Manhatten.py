import numpy as np

v = np.array([3, -4])

# Евклідова
norm_L2 = np.linalg.norm(v)
# або явно з параметром ord=2 np.linalg.norm(v, ord=2)

# Мангеттенська
norm_L1 = np.linalg.norm(v, ord=1)

# Максимуму
norm_Linf = np.linalg.norm(v, ord=np.inf)

print(f"Вектор: v = {v}")
print(f"Евклідова норма: {norm_L2}")
print(f"Мангеттенська норма: {norm_L1}")
print(f"Норма максимуму: {norm_Linf}")


# Вектор: v = [ 3 -4]

# Евклідова норма: 5.0
# Мангеттенська норма: 7.0
# Норма максимуму: 4.0
