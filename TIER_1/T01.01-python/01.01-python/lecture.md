# Лекция: Типы данных в Python

# 1. Переменные, типы и идентификаторы
print(">>> age = 10")
age = 10
print(age)
print(type(age))
print(id(age))

print("\n>>> debt = 1000")
debt = 1000
print(type(debt))
print(id(debt))

print("\n>>> salary")
try:
    print(salary)
except NameError as e:
    print(e)

# 2. Присвоение и неизменяемость (immutable)
print("\n>>> a = 999")
a = 999
print(">>> b = a")
b = a
print(b)
print("id(b) =", id(b))
print(">>> b = 777")
b = 777
print("id(a) =", id(a))
print("id(b) =", id(b))

# 3. Преобразование типов
print("\n>>> int('12')")
print(int("12"))
print("\n>>> int(' 12 ')")
print(int(" 12 "))
print("\n>>> int('asdasd')")
try:
    print(int("asdasd"))
except ValueError as e:
    print(e)
print("\n>>> int('12a')")
try:
    print(int("12a"))
except ValueError as e:
    print(e)
print("\n>>> float('3.123')")
print(float("3.123"))
print("\n>>> float('3,123')")
try:
    print(float("3,123"))
except ValueError as e:
    print(e)

# 4. Булевы значения
print("\n>>> bool(0)", bool(0))
print(">>> bool(1)", bool(1))
print(">>> bool(15)", bool(15))
print(">>> bool(-15)", bool(-15))
print(">>> bool('kjhgfd')", bool("kjhgfd"))
print(">>> bool('k')", bool("k"))
print(">>> bool('')", bool(""))
print(">>> bool(' ')", bool(" "))
print(">>> bool(None)", bool(None))

# 5. Логические операторы
print("\n>>> not False =", not False)
print(">>> False and False =", False and False)
print(">>> True and True =", True and True)
print(">>> True and False =", True and False)
print(">>> False or True =", False or True)
print(">>> True or True =", True or True)
print(">>> False or False =", False or False)

# 6. Пример с условиями
print("\n>>> has_cash = False")
print(">>> is_good_weather = True")
has_cash = False
is_good_weather = True
visit_office = has_cash and is_good_weather
print(">>> visit_office =", visit_office)

# 7. Сложные выражения
print("\n>>> (has_cash or has_loving_wife) and in_good_mood")
has_cash = False
has_loving_wife = True
in_good_mood = True
print((has_cash or has_loving_wife) and in_good_mood)

print(">>> False and True and True and True =", False and True and True and True)
print(">>> False and (True and True) and True =", False and (True and True) and True)
print(">>> True or False and True =", True or False and True)
print(">>> (True or False) and True =", (True or False) and True)

# 8. Именование переменных
print("\n>>> Пример переменных:")
age = 12
email = "test@gmail.com"
students = []
is_verified = False
user_is_not_logged_in = False
inactive_users = []
print("age =", age)
print("email =", email)
print("students =", students)
print("is_verified =", is_verified)
print("user_is_not_logged_in =", user_is_not_logged_in)
print("inactive_users =", inactive_users)

print("\n>>> Стили имён переменных:")
print("snake_case   – стандарт для Python")
print("PascalCase   – для классов")
print("camelCase    – реже")
print("kebab-case   – недопустим в Python")
