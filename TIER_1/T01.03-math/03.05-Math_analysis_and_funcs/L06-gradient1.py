import numpy as np
from scipy.optimize import approx_fprime

# Функція f(x, y) = x^2 + y^2
def f(coords):
    x, y = coords
    return x**2 + y**2

# Точка, в якій обчислюємо частинні похідні
point = np.array([1.0, 2.0])

# Чисельне обчислення градієнта
epsilon = 1e-8
gradient_numerical = approx_fprime(point, f, epsilon)

print("Чисельні частинні похідні:")
print(f"∂f/∂x(1, 2) ≈ {gradient_numerical[0]:.10f}")
print(f"∂f/∂y(1, 2) ≈ {gradient_numerical[1]:.10f}")


# Чисельні частинні похідні:
# ∂f/∂x(1, 2) ≈ 2.0000000000
# ∂f/∂y(1, 2) ≈ 4.0000000000
