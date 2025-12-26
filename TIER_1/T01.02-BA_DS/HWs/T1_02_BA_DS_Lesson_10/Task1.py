import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Max_production", pulp.LpMaximize)

# Визначення змінних
Limonade = pulp.LpVariable("Limonade", lowBound=0, cat="Integer")    # Кількість продукту А
Juice = pulp.LpVariable("Juice", lowBound=0, cat="Integer")          # Кількість продукту Б

# Функція цілі (Максимізація виробництва)
model += Limonade + Juice, "Total_Products"


model += 2 * Limonade + 1 * Juice <= 100   # Обмеження для Води
model += 1 * Limonade <= 50                # Обмеження для Цукру
model += 1 * Limonade <= 30                # Обмеження для Лимонного соку          
model += 2 * Juice <= 40                   # Обмеження для Фруктового пюре

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Виробляти продуктів з Лімонаду:", Limonade.varValue)
print("Виробляти продуктів з Соку:", Juice.varValue)