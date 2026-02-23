# Але спочатку створимо універсальну функцію, яка дозволяє автоматично 
# визначати тип системи лінійних рівнянь. 
# Вона обчислює ранги матриці коефіцієнтів, розширеної матриці та 
# порівнює їх між собою, роблячи висновок про наявність і 
# кількість розв’язків. Це пряма реалізацією критерію Кронекера–Капеллі.

import numpy as np

def analyze_system(A, b) -> dict:
    """
    Аналізує систему лінійних рівнянь Ax = b.
    
    Returns:
        dict: Словник з інформацією про ситуацію розв'язку:
            - 'compatible': bool - чи сумісна система
            - 'solution_type': 'unique' | 'infinite' | 'none'
            - 'case_description': str - опис випадку
            - 'rank_A': int - ранг матриці A
            - 'rank_Ab': int - ранг розширеної матриці [A|b]
            - 'n': int - кількість невідомих
            - 'm': int - кількість рівнянь
            - 'solution': Optional[np.ndarray] - розв'язок (якщо єдиний)
    """

    


    # Обчислюємо ранг матриці коефіцієнтів A
    rank_A = np.linalg.matrix_rank(A)

    # Створюємо розширену матрицю [A|b] і знаходимо її ранг
    rank_Ab = np.linalg.matrix_rank(np.column_stack([A, b]))

    # Кількість невідомих — це кількість стовпців у A
    n = A.shape[1]
    m = A.shape[0]  # кількість рівнянь

    result = {
        'rank_A': rank_A,
        'rank_Ab': rank_Ab,
        'n': n,
        'm': m,
        'compatible': False,
        'solution_type': 'none',
        'solution': None,
        'case_description': ''
    }

    # Порівнюємо ранги згідно з критерієм Кронекера–Капеллі
    if rank_A == rank_Ab:
        result['compatible'] = True
        
        if rank_A == n:
            # Якщо rank(A) = n, то розв'язок єдиний
            x = np.linalg.solve(A, b)
            result['solution_type'] = 'unique'
            result['solution'] = x
            result['case_description'] = 'Сумісна визначена система - єдиний розвязок'
        else:
            # Якщо rank(A) < n, то розв'язків безліч
            result['solution_type'] = 'infinite'
            result['case_description'] = 'Сумісна система - нескінченно багато розвязків'
    else:
        # Якщо rank(A) < rank([A|b]), система несумісна
        result['compatible'] = False
        result['solution_type'] = 'none'
        result['case_description'] = 'Несумісна система - розвязку немає'

    return result

# rank (A) = rank([A|b])
A1 = np.array([
    [2, 1, -1],
    [1, 3, 2],
    [3, -1, 1]
])
b1 = np.array([8, 13, 5])
# Сумісна визначена система - єдиний розв'язок
# x = [2.6 3.2 0.4]


# rank (A) < rank([A|b]):
A2 = np.array([
    [1, 2],
    [2, 4]
])
b2 = np.array([3, 5])
# Несумісна система - розв'язку немає

# rank (A) = rank([A|b]), але цей ранг менший за кількість 
# невідомих, тому існує нескінченно багато рішень.
A3 = np.array([
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
])
b3 = np.array([4, 8, 12])
# Сумісна система - нескінченно багато розв'язків


# Так звана недовизначена система:
A4 = np.array([
    [1, 2, 1],
    [2, 1, 3]
])
b4 = np.array([5, 8])
# Сумісна система - нескінченно багато розв'язків


result4 = analyze_system(A4, b4)
print(result4['case_description'])
if result4['solution'] is not None:
    print("x =", result4['solution'])
print()



result3 = analyze_system(A3, b3)
print(result3['case_description'])
if result3['solution'] is not None:
    print("x =", result3['solution'])
print()



result2 = analyze_system(A2, b2)
print(result2['case_description'])
if result2['solution'] is not None:
    print("x =", result2['solution'])
print()


result1 = analyze_system(A1, b1)
print(result1['case_description'])
if result1['solution'] is not None:
    print("x =", result1['solution'])
print()

