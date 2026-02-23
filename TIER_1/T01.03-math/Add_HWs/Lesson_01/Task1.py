# Базові операції з векторами
import numpy as np

a = np.array([2, -3, -1])
b = np.array([1, 4, -2])

c = a + b
d = a - b
scalar = a * 3
lin_comb = 1 * a + (-1) * b



print("Sum:", c)
print("Diff:", d)
print("Scalar:", scalar)
print("Linear combination:", lin_comb)