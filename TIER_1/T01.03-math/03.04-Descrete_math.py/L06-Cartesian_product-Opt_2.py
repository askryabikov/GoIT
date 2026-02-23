A = {1, 2}
B = {'x', 'y', 'z'}

cartesian = {(a, b) for a in A for b in B}
print("A × B:", cartesian)


# A × B: {(1, 'z'), (2, 'y'), (1, 'y'), (2, 'x'), (1, 'x'), (2, 'z')}
