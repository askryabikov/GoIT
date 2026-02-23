from itertools import product

A = {1, 2}
B = {'x', 'y', 'z'}

cartesian = set(product(A, B))
print("A × B:", cartesian)
print("Кількість елементів:", len(cartesian))

# A × B: {(1, 'z'), (2, 'y'), (1, 'y'), (2, 'x'), (1, 'x'), (2, 'z')}
# Кількість елементів: 6

