# На практиці не завжди можна обчислити похідну аналітично. 
# Функція може бути задана тільки таблицею значень, 
# або її аналітичний вираз занадто складний. 
# У таких випадках використовують чисельне диференціювання.

import numpy as np

def numerical_derivative(f, x, h=1e-5):
    """
    Чисельне обчислення похідної функції f в точці x методом forward difference
    """
    return (f(x + h) - f(x)) / h

# Функція f(x) = sin(x)
f = np.sin
x_point = np.pi / 4

# Аналітична похідна: f'(x) = cos(x)
f_prime_analytic = np.cos(x_point)

# Чисельна похідна
f_prime_numerical = numerical_derivative(f, x_point)

print(f"Аналітична похідна f'(π/4) = {f_prime_analytic:.10f}")
print(f"Чисельна похідна f'(π/4) ≈ {f_prime_numerical:.10f}")
print(f"Абсолютна похибка: {abs(f_prime_analytic - f_prime_numerical):.2e}")
