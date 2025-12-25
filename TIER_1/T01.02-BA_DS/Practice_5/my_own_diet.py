import pulp as pl


data = {
    'Картопля фрі': {'Б': 3.4, 'Ж': 15,  'В': 41},
    'Котлетка': {'Б': 14.1, 'Ж': 15.7, 'В':      6.6},
    'Білий хліб': {'Б': 8.8, 'Ж': 3.3, 'В':  46.7},
    'Помідор': {'Б': 1.1,  'Ж': 0.2, 'В': 3.8},
    'Молочний коктель': {'Б': 6, 'Ж': 5, 'В': 45},
    'Огірок': {'Б': 0.8, 'Ж': 0.1, 'В': 2.5},
}


# Задаємо яка ціль дієти
needed = {'Б': 30, 'Ж': 25, 'В': 60}

# Їсти щось менше 10 гр не бажаємо
MIN = 0.1
# Подумали, що їсти більше 150 гр. теж не хочемо (можна задати окремо по стравам)
MAX = 1.5


prob = pl.LpProblem("The Nutrients Problem", pl.LpMinimize)
# Змінні для меню
food = pl.LpVariable.dicts('Food', data, MIN, MAX)
for nutrient in list('БЖВ'):
    # Умови для макроелементів
    prob += pl.lpSum([data[k][nutrient] * food[k]
                      for k in data]) == needed[nutrient]

prob.writeLP("Nutrients.lp")
prob.solve()

# "Їсти" в мінус чогось не можемо, додаємо обмеження
if any((v.varValue or 0) < 0 for v in prob.variables()) is False:
    for v in prob.variables():
        if not v.varValue:
            continue
        name = v.name.replace('Food_', '')
        weight = int(v.varValue*100)
        print(f'{name}: {weight} гр.')