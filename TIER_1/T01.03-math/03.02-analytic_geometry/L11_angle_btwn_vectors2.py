import numpy as np

# Випадок 1: Співнапрямлені вектори
u1 = np.array([1, 2])
v1 = np.array([2, 4])  # v1 = 2 * u1

angle1 = np.arccos((u1 @ v1) / (np.linalg.norm(u1) * np.linalg.norm(v1)))
print("Співнапрямлені вектори:")
print(f"  u = {u1}, v = {v1}")
print(f"  Кут: {np.degrees(angle1):.2f} градусів")

# Випадок 2: Перпендикулярні вектори 
u2 = np.array([1, 0])
v2 = np.array([0, 1])

angle2 = np.arccos((u2 @ v2) / (np.linalg.norm(u2) * np.linalg.norm(v2)))
print("Перпендикулярні вектори:")
print(f"  u = {u2}, v = {v2}")
print(f"  Кут: {np.degrees(angle2):.2f} градусів")

# Випадок 3: Протилежно напрямлені
u3 = np.array([1, 2])
v3 = np.array([-1, -2])

angle3 = np.arccos((u3 @ v3) / (np.linalg.norm(u3) * np.linalg.norm(v3)))
print("Протилежно напрямлені вектори:")
print(f"  u = {u3}, v = {v3}")
print(f"  Кут: {np.degrees(angle3):.2f} градусів")


# Співнапрямлені вектори:
#   u = [1 2], v = [2 4]
#   Кут: 0.00 градусів

# Перпендикулярні вектори:
#   u = [1 0], v = [0 1]
#   Кут: 90.00 градусів

# Протилежно напрямлені вектори:
#   u = [1 2], v = [-1 -2]
#   Кут: 180.00 градусів