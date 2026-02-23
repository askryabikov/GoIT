import numpy as np

A = np.array([1e9, 1e9])
B = np.array([1e9 + 3, 1e9 - 4])

print("A shape:", A.shape, "B shape:", B.shape)

diff = B - A
d = np.linalg.norm(diff)

print("B - A =", diff)
print("distance =", d)
