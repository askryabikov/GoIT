import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# 1. Генеральна сукупність (Population)
pop_mean = 30
pop_data = np.random.exponential(scale=pop_mean, size=100000)

# 2. Параметри симуляції
n = 100              # Розмір вибірки
num_samples = 5000   # Кількість вибірок

# Генеруємо вибіркові середні
means = [np.mean(np.random.choice(pop_data, size=n)) for _ in range(num_samples)]

# 3. Побудова графіків
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Графік 1: Генеральна сукупність
sns.histplot(pop_data, bins=30, color='#f08080', edgecolor='black', 
             ax=axes[0], stat='density', alpha=0.7)
axes[0].set_title('Генеральна сукупність\\n(експоненційний розподіл)')
axes[0].set_xlabel('Час (хв)')
axes[0].set_ylabel('Щільність')
axes[0].set_xlim(0, 100)

# Графік 2: Розподіл вибіркових середніх (n=100)
sns.histplot(means, bins=30, color='#ffffe0', edgecolor='black', 
             ax=axes[1], stat='density', alpha=0.7)

# Теоретична нормальна крива
mu_theoretical = pop_mean
sigma_theoretical = pop_mean / np.sqrt(n) # SE = sigma / sqrt(n)
x_range = np.linspace(min(means), max(means), 100)
pdf = stats.norm.pdf(x_range, mu_theoretical, sigma_theoretical)

axes[1].plot(x_range, pdf, 'r-', lw=2, label='Теоретичний нормальний')
axes[1].set_title(f'Розподіл вибіркових середніх\\n(n={n})')
axes[1].set_xlabel('Вибіркове середнє (хв)')
axes[1].set_ylabel('Щільність')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
