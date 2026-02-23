# Бібліотека SciPy надає функцію approx_fprime з модуля scipy.optimize 
# для чисельного обчислення похідних. Ця функція обчислює градієнт функції, 
# тому для функції однієї змінної потрібно обгорнути аргумент у масив.

import numpy as np
from scipy.optimize import approx_fprime

# Функція
def f(x):
    """Функція для диференціювання"""
    return np.sin(x[0])  # x — це масив, беремо перший елемент

x_point = np.array([np.pi / 4])  # Обгортаємо в масив

# Чисельна похідна через SciPy
# epsilon — крок для обчислення похідної
f_prime_scipy = approx_fprime(x_point, f, epsilon=1e-5)[0]

# Аналітична похідна
f_prime_analytic = np.cos(np.pi / 4)

print(f"Аналітична похідна: {f_prime_analytic:.10f}")
print(f"SciPy похідна: {f_prime_scipy:.10f}")
print(f"Похибка: {abs(f_prime_analytic - f_prime_scipy):.2e}")


# Аналітична похідна: 0.7071067812
# SciPy похідна: 0.7071032456
# Похибка: 3.54e-06

# Функція approx_fprime приймає три параметри:
# 1. x_point — точка, в якій обчислюємо похідну. Має бути масивом NumPy.
# 2. f — функція, яка приймає масив і повертає число.
# 3. epsilon — крок для обчислення різниці.

