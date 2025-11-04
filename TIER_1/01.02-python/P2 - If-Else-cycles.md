if < условие > :
     < тело  if-блока >
else:
    < тело  else-блока >


num = 15   # пример значение для num
if  num > 10 :
     print ( "num больше 10" )
 else :
     print ( "num не более 10" )


x = int ( input ( 'Введите число:' ))
if  x % 2 == 0 :
     print ( "Число x является четным." )
 else :
     print ( "Число x является нечетным." )


a = input ( 'Введите число' ) 
a = int ( a ) 
if  a > 0 :
     print ( 'Число положительное' ) 
elif  a < 0 :
     print ( "Число отрицательное" ) 
else :
     print ( 'Это число - ноль' )



a = input ( 'Введите число' ) 
a = int ( a )
if  a > 0 :
     print ( 'Число положительное' ) 
elif  a == 1 :
     print ( 'Число равно 1' ) 
else :
     print ( "a <= 0" )


a = input ( 'Введите число' ) 
a = int ( a )

if  a == 1 :
     print ( 'Число равно 1' ) 
elif  a > 0 :
     print ( 'Число положительное' ) 
else :
     print ( "a <= 0" )


money = 0 
if  money :
     print ( f "You have {money} on your bank account" ) 
else :
     print ( "You have no money and no debts" )


result = None 
if  result :
     print ( result ) 
else :
     print ( "Результат is None, do something" )


user_name = input ( "Enter your name: " )
if  user_name :
     print ( f "Hello {user_name}" ) 
else :
     print ( "Hi Anonym!" )


num = int ( input ( "Введите число:" ))
length = len( str (num))
if  length == 2  and num % 2 == 0 :
     print ( "Парное двузначное число" )
 else :
     print ( "Нет" )



x = int(input("X: "))
y = int(input("Y: "))
if x == 0:
    print("X can`t be equal to zero")
    x = int(input("X: "))
result = y / x


if x >= 0:
    if y >= 0:  # x > 0, y > 0
        print("Перша чверть")
    else:  # x > 0, y < 0
        print("Четверта чверть")
else:
    if y >= 0:  # x < 0, y > 0
        print("Друга чверть")
    else:  # x < 0, y < 0
        print("Третя чверть")



is_nice = True
state = "nice" if is_nice else "not nice"

is_nice = True
if is_nice:
    state = "nice"
else:
    state = "not nice"


some_data = None
if some_data:
    msg = some_data
else:
    msg = "Не було повернено даних"


match змінна:
    case шаблон1:
        # виконати код для шаблону 1
    case шаблон2:
        # виконати код для шаблону 2
    case _:
        # виконати код, якщо не знайдено відповідностей


fruit = "apple"
match fruit:
    case "apple":
        print("This is an apple.")
    case "banana":
        print("This is a banana.")
    case "orange":
        print("This is an orange.")
    case _:
        print("Unknown fruit.")


point = (1, 0)

match point:
    case (0, 0):
        print("Точка в центрі координат")  
    case (0, y):
        print(f"Точка лежить на осі Y: y={y}")  
    case (x, 0):
        print(f"Точка лежить на осі X: x={x}") 
    case (x, y):
        print(f"Точка має координати:  x={x}, y={y}") 
    case _:
        print("Це не точка")


pets = ["dog", "fish", "cat"]
match pets:
    case ["dog", "cat", _]:
        # Випадок, коли є і собака, і кіт
        print("There's a dog and a cat.")
    case ["dog", _, _]:
        # Випадок, коли є тільки собака
        print("There's a dog.")
    case _:
        # Випадок для інших комбінацій
        print("No dogs.")


for element in sequence:
    # виконувати дії з element

while condition:
    # виконувати дії, поки condition є True


fruit = 'apple'
for char in fruit:
    print(char)
a
p
p
l
e


alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    print(char, end=" ")
 a b c d e f g h i j k l m n o p q r s t u v w x y z


some_iterable = ["a", "b", "c"]
for i in some_iterable:
    print(i)
a
b
c


odd_numbers = [1, 3, 5, 7, 9]
for i in odd_numbers:
    print(i ** 2)
1
9
25
49
81


# Зчитування рядка від користувача
user_input = input("Введіть рядок: ")

# Ініціалізація змінних для підрахунку символів та пробілів
total_chars = len(user_input)  # загальна кількість символів у рядку
space_count = 0  # кількість пробілів

# Підрахунок кількості пробілів
for char in user_input:
    if char == " ":
        space_count += 1

# Виведення результатів
print(f"Загальна кількість символів у рядку: {total_chars}")
print(f"Кількість пробілів у рядку: {space_count}")


k = 0
while k < 10:
    k = k + 1
	print(k)


a = 0
while True:
    print(a)
    if a >= 20:
        break
    a = a + 1


while True:
    user_input = input()
    print(user_input)
    if user_input == "exit":
        break


a = 0
while a < 6:
    a = a + 1
    if not a % 2:
        continue
    print(a)
1
3
5


for i in range(1, 10):
  if i % 2 == 0:
     print(f”{i} є парним числом.“)
  else:
     print(f”{i} є непарним числом.“)


while True:
    number = input("number = ")
    number = int(number)
    while True:
        print(number)
        number = number - 1
        if number < 0:
            break


for i in range(1, 10):
    if i % 2 == 0:
        print(f”{i} є парним числом.“)
    else:
        print(f”{i} є непарним числом.“)


for  i  in  range ( 5 ):
     print ( i )


for i in range ( 2 , 10 ):
     print (i)


Итерауия с шагом:
for i in range( 0 , 10 , 2 ):
     print (i)


some_list = [ "apple" , "banana" , "cherry" ]
 for  index , value in enumerate(some_list):
     print ( index , value)
0 apple
 1 banana
 2 cherry


list1 = ["зелене", "стигла", "червоний"]
list2 = ["яблуко", "вишня", "томат"]
for number, letter in zip(list1, list2):
    print(number, letter)
зелене яблуко
стигла вишня
червоний томат


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e']
for number, letter in zip(list1, list2):
    print(number, letter)
1 a
2 b
3 c


numbers = {
    1: "one",
    2: "two",
    3: "three"
}
for key in numbers.keys():
    print(key)
1
2
3
И ЕЩЕ:
for val in numbers.values():
    print(val)
one
two
tree
И ОБА:
for key, value in numbers.items():
    print(key, value)
1 one
2 two
3 three


val = 'a' 
try :
     val = int ( val ) 
except  ValueError :
     print ( f "val { val is not a number" ) 
else :
     print ( val > 0 ) 
finally :
     print ( " This will be printed anyway" )

