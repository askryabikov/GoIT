def bayes_theorem(p_h, p_evidence_given_h, p_evidence_given_not_h):
    """
    Обчислює апостеріорну ймовірність гіпотези за теоремою Байєса.
    
    Параметри:
    p_h: P(H) - апріорна ймовірність гіпотези
    p_evidence_given_h: P(E|H) - ймовірність спостереження за умови що гіпотеза вірна
    p_evidence_given_not_h: P(E|not H) - ймовірність спостереження за умови що гіпотеза хибна
    
    Повертає:
    P(H|E) - апостеріорна ймовірність гіпотези після спостереження
    """
    # Апріорна ймовірність протилежної гіпотези
    p_not_h = 1 - p_h
    
    # Повна ймовірність спостереження (evidence)
    p_evidence = p_h * p_evidence_given_h + p_not_h * p_evidence_given_not_h
    
    # Апостеріорна ймовірність за теоремою Байєса
    p_h_given_evidence = (p_h * p_evidence_given_h) / p_evidence
    
    return p_h_given_evidence


# Приклад 2: Медичний тест
p_disease = 0.01        # P(D) - базова частота хвороби 1%
sensitivity = 0.99      # P(T|D) - чутливість тесту 99%
false_positive = 0.05   # P(T|not D) - хибнопозитивний результат 5%

result = bayes_theorem(p_disease, sensitivity, false_positive)

print(f"Апріорна ймовірність хвороби: {p_disease:.1%}")
print(f"Апостеріорна ймовірність після позитивного тесту: {result:.1%}")

# Апріорна ймовірність хвороби: 1.0%
# Апостеріорна ймовірність після позитивного тесту: 16.7%