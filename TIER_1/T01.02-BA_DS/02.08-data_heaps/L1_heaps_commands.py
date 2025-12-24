import heapq

nums = [ 4 , 10 , 3 , 5 , 1 ]
heapq.heapify(nums)
print (nums)   # Output: [1, 4, 3, 5, 10]


# Функция heappush(heap, elem)добавляет элемент в кучу и перестраивает кучу.
heapq .heappush (nums, 0 )
print (nums) # Output: [ 0 , 4 , 1 , 5 , 10 , 3 ]



# Функция heappop(heap)удаляет и возвращает наименьший элемент.
min_elem = heapq.heappop(nums)
print (min_elem)   # Output: 0 
print (nums)   # Output: [1, 4, 3, 5, 10]


# Функция heappushpop(heap, elem)добавляет элемент в кучу, 
# а затем удаляет и возвращает наименьший элемент.
min_elem = heapq.heappushpop(nums, 2 )
print (min_elem)   # Output: 1 
print (nums)   # Output: [2, 4, 3, 5, 10]


# Функция heapreplace(heap, elem)удаляет и возвращает наименьший элемент, 
# затем добавляет новый элемент.
min_elem = heapq.heapreplace(nums, 0 )
print (min_elem)   # Output: 2 
print (nums)   # Output: [0, 4, 3, 5, 10]



# Функции n largest (n, iterable, key=None) и n smallest(n, iterable, key=None) возвращают n наибольших
# и n наименьших элементов из итерабельного объекта соответственно.
largest_three = heapq.nlargest( 3 , nums)
smallest_three = heapq.nsmallest( 3 , nums)
print (largest_three)   # Output: [10, 5, 4] 
print (smallest_three)   # Output: [0, 3, 4] 
print (nums)   # [0, 4, 3, 5, 10]




