import numpy as np

A = np.array([[3, 1], [0, 2]], dtype=float)

# Обчислюємо власні значення та власні вектори
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Власні значення λ:")
print(eigenvalues)
print("Власні вектори (стовпці матриці):")
print(eigenvectors)


# Власні значення λ:
# [3. 2.]

# Власні вектори (стовпці матриці):
# [[ 1.         -0.70710678]
#  [ 0.          0.70710678]]
