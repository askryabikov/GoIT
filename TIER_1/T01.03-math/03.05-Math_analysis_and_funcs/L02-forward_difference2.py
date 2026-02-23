import numpy as np
import matplotlib.pyplot as plt

def numerical_derivative(f, x, h):
    return (f(x + h) - f(x)) / h

f = np.sin
x_point = np.pi / 4
f_prime_analytic = np.cos(x_point)

# Перевіримо широкий діапазон значень h
h_values = np.logspace(-10, -1, 100)
errors = []

for h in h_values:
    f_prime_num = numerical_derivative(f, x_point, h)
    error = abs(f_prime_num - f_prime_analytic)
    errors.append(error)

plt.figure(figsize=(9, 5))
plt.loglog(h_values, errors, 'b-', linewidth=2)
plt.xlabel('Крок h')
plt.ylabel('Абсолютна похибка')
plt.title('Залежність похибки від кроку h (метод forward difference)')
plt.grid(True, which='both', alpha=0.3)
plt.show()
