from scipy.integrate import quad
import numpy as np

def f(x):
    return np.exp(-x)

# Нескінченна верхня межа
result, error = quad(f, 0, np.inf)

print(f"Чисельно: {result}")
print(f"Похибка: {error:.2e}")


# Чисельно: 1.0000000000000002
# Похибка: 5.84e-11
