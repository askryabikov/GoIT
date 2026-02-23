# Базовий вектор
import numpy as np
v = np.array([2, 3])

# Множення на різні скаляри
scalars = [0.5, 1, 2, -1]
results = {}

print("Множення вектора v = [2, 3] на різні скаляри:\\n")
for alpha in scalars:
    result = alpha * v
    results[alpha] = result
    print(f"  {alpha} × v = {result}")


# Множення вектора v = [2, 3] на різні скаляри:

#   0.5 × v = [1.  1.5]
#   1 × v = [2 3]
#   2 × v = [4 6]
#   -1 × v = [-2 -3]
