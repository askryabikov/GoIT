lst = [1, 2, 'a', [4, 5]]
print(lst)  # Output: array([1, 2, 3, 4, 5])
print(type(lst))  # Output: <class 'numpy.ndarray'>
# print(lst+2)
print(lst[2])
lst[2] = 3
print(lst)
print([prop for prop in dir(lst) if not prop.startswith('__')])