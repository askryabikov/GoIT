# Пошук коефіцієнтів лінійної комбінаці
import numpy as np

e1 = np.array([1, 0])
e2 = np.array([0, 1])
target = np.array([5, -3])


# коэффициенты
c1 = target[0]
c2 = target[1]

# проверка
result = c1*e1 + c2*e2

print("c1 =", c1, "c2 =", c2)
print("result:", result)
print("check:", np.array_equal(result, target))