import numpy as np
import matplotlib.pyplot as plt

# Генеральна сукупність: 100,000 користувачів
# Час розподілений рівномірно від 0 до 60 хвилин, тому μ = 30
population = np.random.uniform(0, 60, 100000)
true_mean = 30

# Будемо додавати користувачів по одному і рахувати поточне середнє
sample_sizes = range(1, 10001)
cumulative_means = []

for n in sample_sizes:
    current_sample = population[:n]  # беремо перших n користувачів
    cumulative_means.append(np.mean(current_sample))

# Виведемо значення для різних розмірів вибірки
print(f"Вибіркове середнє для n=10:    {cumulative_means[9]:.2f} хв")
print(f"Вибіркове середнє для n=100:   {cumulative_means[99]:.2f} хв")
print(f"Вибіркове середнє для n=1000:  {cumulative_means[999]:.2f} хв")
print(f"Вибіркове середнє для n=10000: {cumulative_means[9999]:.2f} хв")
print(f"Справжнє μ:                    {true_mean:.2f} хв")


# Вибіркове середнє для n=10:    28.80 хв
# Вибіркове середнє для n=100:   28.67 хв
# Вибіркове середнє для n=1000:  30.27 хв
# Вибіркове середнє для n=10000: 29.84 хв
# Справжнє μ:                    30.00 хв
