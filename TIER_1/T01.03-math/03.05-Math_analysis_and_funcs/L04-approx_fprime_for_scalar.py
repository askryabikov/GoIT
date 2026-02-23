# Якщо ваша функція вже написана та приймає скаляр, а не масив, 
# можна створити просту обгортку, 
# яка перетворює масив у скаляр перед викликом функції.

import numpy as np
from scipy.optimize import approx_fprime

# Функція, що приймає скаляр
def f_scalar(x):
    return np.sin(x)

# Обгортка для approx_fprime
def f_vector(x):
    return f_scalar(x[0])

x_point = np.array([np.pi / 4])
f_prime = approx_fprime(x_point, f_vector, epsilon=1e-5)[0]

print(f"Похідна: {f_prime:.10f}")


# Похідна: 0.7071032456
