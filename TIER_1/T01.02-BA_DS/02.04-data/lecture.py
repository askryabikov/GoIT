# Bubble sort

def bubble_sort(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(0, n-i-1): 
            if lst[j] > lst[j+1] :
                lst[j], lst[j+1] = lst[j+1], lst[j] 
    return lst

numbers = [5, 3, 8, 4, 2]
bubble_sort(numbers)



# Insertion sort

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

numbers = [5, 3, 8, 4, 2]
insertion_sort(numbers)


# Selection sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

numbers = [5, 3, 8, 4, 2]
print(selection_sort(numbers))


# Quick sort

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([5, 3, 8, 4, 2]))
# Виведе: [2, 3, 4, 5, 8]


# Merge sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


# Shell sort

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr

numbers = [5, 3, 8, 4, 2]
shell_sort(numbers)


def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        print(f"GAP: =============={gap}===================")
        for i in range(gap, n):
            temp = arr[i]
            j = i
            print(f"i: ----------------- {i} ----------------")
            print(f"Список на початку ітерації {i}: {arr}")
            print(f"j: {j}, temp: {temp}, gap: {gap}")
            print(f"Порівнюємо елементи: {arr[j - gap]} > {temp}")
            while j >= gap and arr[j - gap] > temp:
                print(
                    f"Виконано обмін в циклу while: значення {arr[j - gap]} замінило {arr[j]}"
                )
                arr[j] = arr[j - gap]
								print(f"Список змінився j: {j}: {arr}")
                j -= gap
                print(f"Змінили j вліво: {j}")
            print(f"В кінці циклу for: значення {temp} замінило {arr[j]}")
            arr[j] = temp
            print(f"Список на кінець ітерації {i}: {arr}")
        gap //= 2
        if gap == 0:
            print("Сортування завершено")
    return arr

numbers = [5, 3, 8, 4, 2]
# numbers = [64, 34, 25, 12, 22, 11, 90]
print(shell_sort(numbers))



# Radix sort

def counting_sort(arr, position):
    size = len(arr)
    output = [0] * size
    count = [0] * 10

    # Рахунок входжень певного розряду
    for i in range(0, size):
        index = arr[i] // position % 10
        count[index] += 1

    # Оновлення count[i] так, щоб він показував позицію наступного входження своєї цифри
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Побудова вихідного масиву
    i = size - 1
    while i >= 0:
        index = arr[i] // position % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]

def radix_sort(arr):
    # Визначення максимального числа для визначення кількості розрядів
    max_num = max(arr)
    position = 1
    # Виконання counting_sort для кожного розряду
    while max_num // position > 0:
        counting_sort(arr, position)
        position *= 10

arr = [3, 89, 67, 254, 9, 21, 185, 4, 62]
radix_sort(arr)
print("Відсортований масив:", arr)  # Відсортований масив: [3, 4, 9, 21, 62, 67, 89, 185, 254]
