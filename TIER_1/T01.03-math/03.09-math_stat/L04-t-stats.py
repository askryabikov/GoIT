from scipy import stats

t_statistic = 1.33
degrees_of_freedom = 99

# Для двостороннього тесту множимо на 2
p_value = 2 * (1 - stats.t.cdf(t_statistic, degrees_of_freedom))

print(f"Тестова статистика: t = {t_statistic}")
print(f"p-value = {p_value:.3f}")


# Тестова статистика: t = 1.33
# p-value = 0.187
