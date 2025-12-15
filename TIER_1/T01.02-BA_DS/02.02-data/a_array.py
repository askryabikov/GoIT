import numpy as np

# arr = np.array([1, 2, 'a', 4, 5])
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)  # Output: array([1, 2, 3, 4, 5])
# print(type(arr))  # Output: <class 'numpy.ndarray'>
# #print(arr+2)
# print(arr[2])
# arr[2] = 13
# # arr[2]='13'
# # print(arr)
# print(arr.dtype)
# arr.dtype = np.int16
# print(arr.dtype)
# # print([prop for prop in dir(arr) if not prop.startswith('__')])
# print(arr)  # Output: array([1, 2, 3, 4, 5])

# print([i for i in dir(arr) if not i.startswith('__')])

arr=np.array([0])
arr.dtype=np.int8
arr[0]=1
arr[1]=2
arr[2]=3
arr.dtype=np.int8
print(arr)