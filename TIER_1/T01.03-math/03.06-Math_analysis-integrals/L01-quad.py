# SciPy: численное вычисление определённых интегралов через quad
# quad автоматически подбирает метод и разбиение для высокой точности.

from scipy.integrate import quad

# Синтаксис:
# result, error = quad(f, a, b)
#
# Параметры:
# f     — функция для интегрирования (принимает x и возвращает значение)
# a     — левая граница интегрирования
# b     — правая граница интегрирования
#
# Возвращает:
# result — приближённое значение интеграла
# error  — оценка абсолютной погрешности

# Примеры:

# 1) ∫_0^1 x^2 dx = 1/3
f1 = lambda x: x**2
res1, err1 = quad(f1, 0, 1)
print("∫_0^1 x^2 dx =", res1, "  error≈", err1)

# 2) ∫_0^π sin(x) dx = 2
import numpy as np
f2 = np.sin
res2, err2 = quad(f2, 0, np.pi)
print("∫_0^π sin(x) dx =", res2, "  error≈", err2)

# 3) ∫_1^2 1/x dx = ln(2)
f3 = lambda x: 1/x
res3, err3 = quad(f3, 1, 2)
print("∫_1^2 1/x dx =", res3, "  error≈", err3)
