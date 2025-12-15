def say_hello():
		# тіло функції
    print('Привіт, Світ!')

# Кінець функції say_hello()

# виклик функції
say_hello()

# ще один виклик функції
say_hello()


def print_max(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'максимально')

print_max(3, 4)  # пряма передача значень

x = 5
y = 7
print_max(x, y)  # передача змінних у якості аргументів


def print_max(a: int, b: int):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'максимально')

print_max(3, 4)  # пряма передача значень

x = 5
y = 7
print_max(x, y)  # передача змінних у якості аргументів



def add_numbers(num1: int, num2: int) -> int:
    sum = num1 + num2
    return sum
result = add_numbers(5, 10)
print(result)  # Виведе: 15



def is_even(num: int) -> bool:
    return num % 2 == 0
check_even = is_even(4)
print(check_even)  # Виведе: True



def modify_string(original: str) -> str:
    original = "змінено"
    return original
str_var = "оригінал"
print(modify_string(str_var))  # виведе: змінено
print(str_var)                # виведе: оригінал



def modify_list(lst: list) -> None:
    lst.append(4)
my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # виведе: [1, 2, 3, 4]


def string_to_codes(string: str) -> dict:
    # Ініціалізація словника для зберігання кодів
    codes = {}  
    # Перебір кожного символу в рядку
    for ch in string:  
        # Перевірка, чи символ вже є в словнику
        if ch not in codes:
            # Додавання пари символ-код в словник  
            codes[ch] = ord(ch)  
    return codes

result = string_to_codes("Hello world!")
print(result)

{'H': 72, 'e': 101, 'l': 108, 'o': 111, ' ': 32, 'w': 119, 'r': 114, 'd': 100, '!': 33}



x = 50
def func() -> None:
    x = 2
    print('Зміна локального x на', x)  # Зміна локального x на 2
func()
print('Глобальний x як і раніше', x)  # x як і раніше 50
Зміна локального x на 2
Глобальний x як і раніше 50


def  func_outer (): 
    x = 2 

    def  func_inner ():
         nonlocal x 
        x = 5
    func_inner() return x 
result = func_outer()   # 5
    

x = 50
 
def func () :
     global x 
    print( 'x равно' , x)   # x равно 50 
    x = 2 
    print( 'Изменяем глобальное значение x на' , x)   # Изменяем глобальное значение x на 2 
func () 
print( 'Значение x составляет' , x) # Значение x составляет 2

x равно 50 
Изменяем глобальное значение x на 2 
Значение x составляет 2



def  greet ( name, message= "Привет" ):
     print ( f" {message} , {name} !" )
# использует значение по умолчанию для message 
greet ( "Алексей" )  

# передача собственного значения для message 
greet ( "Мария" , message = "Добрый день" )  

Привет, Алексей!
Добрый день, Мария!



def func(a, b =5, c =10):
     print ( 'a равно' , a, ', b равно' , b, ', а c равно' , c)

# a равно 3, b равно 7, а c равно 10
func(3, 7)
# a равно 25, b равно 5, а c равно 24 
func(25, c =24)
# a равно 100, b равно 5, а c равно 50 
func( c =50, a =100)

a равно 3 , b равно 7 , а c равно 10 
a равно 25 , b равно 5 , а c равно 24 
a равно 100 , b равно 5 , а c равно 50


def say (message, times = 1 ):
     print (message * times )
say ( 'Привет' ) 
 say ( 'Мир' , 5 )



def real_cost ( base : int , discount: float = 0 ) -> float :
     return  base * ( 1 - discount )
price_bread = 15 
price_butter = 50 
price_sugar = 60

current_price_bread = real_cost(price_bread)
 current_price_butter = real_cost(price_butter, 0.05 )
 current_price_sugar = real_cost(price_sugar, 0.07 )

print (f 'Новая стоимость хлеба: {current_price_bread}' ) 
print (f 'Новая стоимость масла: {current_price_butter}' ) 
print (f 'Новая стоимость сахара: {current_price_sugar}' )

Новая стоимость хлеба :  15 
Новая стоимость масла :  47.5 
Новая стоимость сахара :  55.8



def  print_all_args ( *args ):
     для arg in args:
         print (arg)
print_all_args( 1 , 'hello' , True )
1
hello
True



def concatenate (*args) -> str:
    result = "" 
    for arg in args:
        result += arg
    return result
print (concatenate( "Hello" , " " , "world" , "!" ))
Hello world!



def greet(**kwargs):
     for key, value in kwargs.items():
         print (f "{key}: {value}" )
greet( name = "Alice" , age =25)
name: Alice
 age:  25



def example_function(*args, **kwargs):
    print("Позиційні аргументи:", args)
    print("Ключові аргументи:", kwargs)
example_function(1, 2, 3, name="Alice", age=25)
Позиційні аргументи: (1, 2, 3)
Ключові аргументи: {'name': 'Alice', 'age': 25}



my_list = [1, 2, 3]
a, b, c = my_list
Игнор:
a, _, c = my_list
Частично:
a, *rest = my_list



def  factorial ( n ):
     if n == 0 : # базовый случай 
        return  1 
    else :
         return n * factorial(n- 1 ) # рекурсивный случай
print (factorial( 5 )) # выведет 120



def  fibonacci ( n ):
     if n <= 1 : # базовый случай 
        return n
     else :
         return fibonacci(n- 1 ) + fibonacci(n- 2 ) # рекурсивный случай
print (fibonacci( 10 )) # выведет 55



def factorial (n):
     print ( "Вызов функции factorial с n = " , n)
     if n == 1 :
         print ( "Базовый случай, n = 1, возврат 1" )
         return  1 
    else :
        result = n * factorial (n- 1 )
         print ( "Возврат результата для n = " , n, ": " , result)
         return result
print ( factorial ( 5 ))
Этот код вычисляет факториал числа 5, равный 5*4*3*2*1=120



