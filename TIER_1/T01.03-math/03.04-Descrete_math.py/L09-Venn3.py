#  Розглянемо практичну задачу — 
# аналіз компетенцій у розробників.
#  У нас є команда, і ми хочемо зрозуміти хто 
# якими технологіями володіє.


import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Хто знає які технології
python_devs = {'Марія', 'Іван', 'Олег', 'Анна', 'Дмитро', 'Катя'}
javascript_devs = {'Іван', 'Анна', 'Сергій', 'Ольга', 'Дмитро'}
sql_devs = {'Марія', 'Анна', 'Дмитро', 'Петро', 'Ольга'}

# Будуємо діаграму
venn3([python_devs, javascript_devs, sql_devs], ('Python', 'JavaScript', 'SQL'))
plt.title('Навички розробників у команді')
plt.show()

# Аналіз
print("Знають усі три технології:", python_devs & javascript_devs & sql_devs)
print("Знають тільки Python:", python_devs - javascript_devs - sql_devs)
print("Знають Python і JavaScript, але не SQL:", (python_devs & javascript_devs) - sql_devs)


# Знають усі три технології: {'Анна', 'Дмитро'}
# Знають тільки Python: {'Олег', 'Катя'}
# Знають Python і JavaScript, але не SQL: {'Іван'}
