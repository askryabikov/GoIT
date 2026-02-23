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

# Приклад 3: Урни з кулями
p_urn1 = 0.5              # P(H1) - вибрали першу урну
p_white_from_urn1 = 0.3   # P(A|H1) - біла куля з першої урни
p_white_from_urn2 = 0.6   # P(A|H2) - біла куля з другої урни

# Для першої урни (not H1 означає другу урну)
prob_urn1_given_white = bayes_theorem(p_urn1, p_white_from_urn1, p_white_from_urn2)

# Для другої урни
prob_urn2_given_white = bayes_theorem(0.5, p_white_from_urn2, p_white_from_urn1)

print(f"Ймовірність що біла куля з першої урни: {prob_urn1_given_white:.1%}")
print(f"Ймовірність що біла куля з другої урни: {prob_urn2_given_white:.1%}")

# Ймовірність що біла куля з першої урни: 33.3%
# Ймовірність що біла куля з другої урни: 66.7%


