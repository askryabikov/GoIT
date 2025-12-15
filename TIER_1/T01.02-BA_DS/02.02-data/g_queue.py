from queue import Queue

# Створюємо чергу
q = Queue()

# Додаємо елементи
q.put('a')
q.put('b')
q.put('c')

print(q.queue)  # Output: deque(['a', 'b', 'c'])

q.put('d')

print(q.queue)  

print(q.get())
print(q.queue) 