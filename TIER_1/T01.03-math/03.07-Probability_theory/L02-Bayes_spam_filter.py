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

# Приклад 1: Спам-фільтр
p_spam = 0.3           # 30% листів це спам
p_word_in_spam = 0.6   # 60% спам-листів містять слово "безкоштовно"
p_word_in_normal = 0.05 # 5% нормальних листів містять це слово

result_spam = bayes_theorem(p_spam, p_word_in_spam, p_word_in_normal)
print(f"Ймовірність спаму при слові 'безкоштовно': {result_spam:.1%}")
