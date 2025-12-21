def linear_search(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1

numbers = [1, 3, 5, 7, 9, 11]
print(linear_search(numbers, 7))  # Output: 3
