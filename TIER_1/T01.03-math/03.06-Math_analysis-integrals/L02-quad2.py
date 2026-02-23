# Пример 1.
# Вычислим интеграл: ∫_0^2 x^2 dx
# Аналитически: [x^3/3]_0^2 = 8/3 ≈ 2.666666...

import numpy as np
from scipy.integrate import quad

# Функція
def f(x):
    return x**2

# Обчислення інтеграла
result, error = quad(f, 0, 2)

print(f"Результат: {result}")
print(f"Похибка: {error:.2e}")


# Результат: 2.666666666666667
# Похибка: 2.96e-14
