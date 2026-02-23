A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

# Різниця A без B
C = A.difference(B)
print("A - B:", C)

# Через оператор
C = A - B
print("A - B:", C)

# Зворотна різниця B без A
D = B - A
print("B - A:", D)


# A - B: {1, 2}
# A - B: {1, 2}
# B - A: {6, 7}
