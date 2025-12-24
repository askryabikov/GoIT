import heapq

def heap_sort_desc(iterable):
    h = []
    # Вставляємо в купу від'ємні значення
    for value in iterable:
        heapq.heappush(h, -value)
    
    # Витягуємо елементи і міняємо знаки для відновлення оригінальних значень
    return [-heapq.heappop(h) for _ in range(len(h))]

arr = [12, 11, 13, 5, 6, 7]
sorted_arr_desc = heap_sort_desc(arr)
print("Відсортований масив (за спаданням):", sorted_arr_desc)
