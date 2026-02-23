# Вычислим интеграл: ∫_0^2 x^2 dx.
# Аналитическое значение: 8/3 ≈ 2.6666666667.


from scipy.integrate import quad
import numpy as np

def f(x):
    return np.sin(x)

result, error = quad(f, 0, np.pi)

print(f"Чисельно: {result}")
print(f"Оцінка похибки: {error:.2e}")


# Чисельно: 2.0
# Оцінка похибки: 2.22e-14
