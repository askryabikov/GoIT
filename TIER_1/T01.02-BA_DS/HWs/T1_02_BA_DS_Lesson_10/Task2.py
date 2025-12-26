import random
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


# 1. Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа


# 2. Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()


# 3. Монте Карло
def is_inside(x, y):
    """
    Перевіряє, чи точка (x, y) знаходиться "під графіком" функції
    Якщо y <= f(x), то точка під кривою
    """
    return y <= f(x)


def monte_carlo_integral(a, b, num_points=15000, num_experiments=100):
    """
    Оцінюємо інтеграл методом Монте-Карло:
    1. Будуємо прямокутник: x ∈ [a, b], y ∈ [0, y_max]
    2. Генеруємо випадкові точки (x, y) в цьому прямокутнику
    3. M = кількість точок під кривою, N = загальна кількість точок
    4. Площа під кривою ≈ (M/N) * площа прямокутника
    5. Повторюємо експеримент num_experiments разів та усереднюємо результат
    """
    # Для однакових результатів в терміналі і readme:
    random.seed(42)   

    # Максимальне значення функції на відрізку [a, b]
    # Для x^2 на [0,2] максимум у точці x=b
    y_max = f(b)

    # Площа прямокутника, в якому ми "кидаємо" точки
    rect_area = (b - a) * y_max

    average_area = 0.0

    for _ in range(num_experiments):
        # Генеруємо num_points випадкових точок у прямокутнику
        points = [(random.uniform(a, b), random.uniform(0, y_max)) for _ in range(num_points)]

        # Відбираємо точки, які потрапили під криву
        inside_points = [p for p in points if is_inside(p[0], p[1])]

        # M - під кривою, N - всього
        M = len(inside_points)
        N = len(points)

        # Оцінка площі під кривою
        area = (M / N) * rect_area
        average_area += area

    # Усереднюємо по кількості експериментів
    return average_area / num_experiments



# 4. Порівняння Монте-Карло з quad (SciPy)
mc_result = monte_carlo_integral(a, b, num_points=15000, num_experiments=100)

# quad рахує інтеграл чисельно більш точним детермінованим методом
quad_result, quad_error = spi.quad(f, a, b)

# Абсолютна різниця між оцінками
abs_diff = abs(mc_result - quad_result)

print("Monte Carlo integral:", mc_result)
print("quad integral:", quad_result)
print("quad abs error estimate:", quad_error)
print("Absolute difference |MC - quad|:", abs_diff)

# Простий висновок для перевірки
if abs_diff < 0.01:
    print("Conclusion: Monte Carlo is close to quad for these parameters")
else:
    print("Conclusion: Increase num_points / num_experiments to get closer to quad")