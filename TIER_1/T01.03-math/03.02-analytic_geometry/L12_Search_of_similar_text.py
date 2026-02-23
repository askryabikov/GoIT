import numpy as np

# Документи як вектори частот
doc1 = np.array([10, 8, 9, 7, 6])    # стаття про машинне навчання
doc2 = np.array([9, 7, 8, 6, 5])     # схожа стаття про машинне навчання
doc3 = np.array([2, 1, 1, 10, 2])    # стаття про дані, але не про ML

# Функція для обчислення косинусної схожості
def cosine_similarity(u, v):
    return (u @ v) / (np.linalg.norm(u) * np.linalg.norm(v))

# Порівнюємо документи
sim_12 = cosine_similarity(doc1, doc2)
sim_13 = cosine_similarity(doc1, doc3)
sim_23 = cosine_similarity(doc2, doc3)

print("Косинусна схожість між документами:")
print(f"  Документ 1 vs Документ 2: {sim_12:.4f}")
print(f"  Документ 1 vs Документ 3: {sim_13:.4f}")
print(f"  Документ 2 vs Документ 3: {sim_23:.4f}")


# Косинусна схожість між документами:
#   Документ 1 vs Документ 2: 0.9997
#   Документ 1 vs Документ 3: 0.6246
#   Документ 2 vs Документ 3: 0.6150
