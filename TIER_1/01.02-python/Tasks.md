Метод .sort() сортирует список по возрастанию прямо на месте, изменяя оригинальный список.
Если хочешь отсортировать по убыванию — можно добавить параметр

numbers = [1, 2, 12, 13, 12, 3, -1, 2, 41]
numbers.sort()
print(numbers)

ИЛИ:

numbers = [1, 2, 12, 13, 12, 3, -1, 2, 41]
max_number = numbers[0]
for current in numbers:
    if current > max_number:
        max_number = current
print("Max number is", max_number)

ИЛИ:

numbers = [1, 2, 12, 13, 12, 3, -1, 2, 41]
print("Max number is ", max(numbers))
