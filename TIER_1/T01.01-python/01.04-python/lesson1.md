
# Тройные кавычки, если больше одной строки
text = """This is first line
And second line
Last third line"""

song = '''Jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
В одном лошади оставляется sleigh'''


# Перенос с помощью /
one_line_text = "Textual data in Python is handled with str objects, or strings. Strings are immutable sequences of Unicode code points. String literals are written in a variety of ways: single quotes, double quotes, triple quoted."

one_line_text = "Textual data in Python is handled with str objects," \
                " or strings. Strings are immutable sequences of Unicode" \
                " code points. String literals are written in a variety " \
                " of ways: single quotes, double quotes, triple quoted."


# Неявная конкатенация, когда два строчных литерала рядом
( "spam "  "eggs" ) == "spam eggs"   # True

one_line_text = ( "Textual data in Python is handled with str objects," 
                " or strings. Strings are immutable sequences of Unicode" 
                " code
                 points
 .


# Неявная конкатенация помогает при создании SQL-запросов
query = (" SELECT * " 
         " FROM some_table " 
         " WHERE condition1 = True  " 
         " AND condition2 = False ")


# символ \n отвечает за перенос строки (line break)
print ( "Hello\nWorld" )

Hello 
World


# горизонтальная табуляция \t (tab): - При выводе между словами будет символ табуляции:
print ( "Hello\tWorld" )
 Hello	World

# символ \r, возвращает к началу строки и продолжает вывод.
print ( "Hello my little\rsister" )
# !!! \r не удаляет старый текст — он просто возвращает курсор в начало, 
# и всё, что ты печатаешь потом, замещает существующие символы только на своём месте.

# Управляющий символ \b ушиба (backspace)
print ( "Hello\bWorld" )

HellWorld

# Также если нам нужно выполнить выведение обратной косой черты.
print ( "Hello\\World" )

Hello \World

# Чтобы экранировать одинарные и двойные кавычки и разрешить использовать кавычки внутри строчных литералов.
print ( 'It's a beautiful day' ) 
print ( "He said, \"Hello\"" )

It's a beautiful day 
He said, "Hello"



# Поиск в строке
s = "Hi there!"
start = 0
end = 7
print (s. find ( "er" , start, end)) # 5
 print (s. find ( "q" )) # -1

5
 -1


# Поиск через find
s= 'Some words'
print (s. find ( "o" ))
 print (s.rfind( 'o' ))

1
6
# rfind - ищет с конца


# Поиск через индекс
s= 'Some words'
print (s.index( "o" ) )
 print (s.rindex( 'o' ) )

1
6
# rindex - ищет с конца


# SPLIT
str.split( separator = None, maxsplit =-1)

separator- разделитель, по которому следует разделять строчку. Если не указано, строка разделяется по любому пробелу.

maxsplit– максимальное количество разделений. Значение -1означает "без ограничений".

text = "hello world" 
result = text . split ()
print( result )  
# Выведет: ['hello', 'world']


text = "apple,banana,cherry" 
result = text . split ( ',' )
print( result )  
# Выведет: ['apple', 'banana', 'cherry']


# JOIN
string . join (iterable)
string- строка разделителя, которая будет вставлена ​​между элементами последовательности.
iterable- последовательность, список или кортеж строк, которые необходимо объединить.

list_of_strings = [ 'Hello' , 'world' ]
 result  =  ''' . join (list_of_strings)
print( result ) 
# Выведет: 'Hello world'

elements = [ 'earth' , 'air' , 'fire' , 'water' ]
 result  =  ',' . join (elements)
print( result ) 
# Выведет: 'earth, air, fire, water'


# STRIP
clean = ' spacious ' .strip()
 print (clean) # spacious

"левый",  lstrip, удаляет только пробелы в начале строки;
и "правый",  rstrip, удаляет только пробелы в конце строки.



# REPLACE
str. replace (old, new , count = -1 )
old- подстроку, которую нужно заменить.
new- подстрока, на которую нужно заменить.
count- счетчик максимального количества замен. Если не указано или указано , заменяются все входы.-1

text = "Hello world" 
new_text = text .replace ( "world" , "Python" )
 print (new_text) 
Hello Python


text = "one fish, 2 fish, red fish, blue fish" 
new_text = text .replace ( "fish" , "bird" , 2 )
 print (new_text)  
one bird, 2 bird, red fish, blue fish


text = "Hello, world!" 
new_text = text .replace ( "world" , "" )
 print (new_text)
Hello, !



# REMOVEPREFIX
print ( 'TestHook' .removeprefix( 'Test' )) # Hook 
print ( 'TestHook' .removeprefix( 'Hook' )) # TestHook
Hook
TestHook


# REMOVESUFFIX
print ( 'TestHook' .removesuffix( 'Test' ) )
 print ( 'TestHook' .removesuffix( 'Hook' ) )
TestHook
 Test




<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>

url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')
print(query)

q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t

# Переменная url_search– это наш начальный URL. Далее операция url_search.split('?')разделяет URL на две части: до знака ?и после. Поскольку нас интересует только часть после ?, мы используем символ _ для игнорирования части URL до ?. Но получаем переменную query строку, содержащую необходимые нам параметры запроса.

# Теперь в переменной query хранится:
["q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t"]


obj_query = {}
for el in query.split('&'):
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ')})
print(obj_query)

# 1 query.split('&')
Делит строку по символу &.
# 2 for el in query.split('&')
Проходим по каждому элементу списка:
el = 'q=Cat+and+dog'
el = 'ie=utf-8'
el = 'oe=utf-8'
el = 'aq=t'
# 3 key, value = el.split('=')
Делим каждую пару по знаку =:
# 4 value.replace('+', ' ')
В URL пробелы записываются как +.
Поэтому Cat+and+dog превращается в Cat and dog.
# 5 obj_query.update({key: value})
Добавляем в словарь новую пару ключ–значение.

q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t
{'q': 'Cat and dog', 'ie': 'utf-8', 'oe': 'utf-8', 'aq': 't'}

Итого, простыми словами:
Делим ссылку по ?, чтобы отделить адрес от параметров.
Потом делим параметры по &, чтобы получить каждую пару отдельно.
Потом делим каждую пару по =, чтобы получить ключ и значение.
Меняем + на пробел (потому что так кодируются пробелы в URL).
Собираем всё в словарь, где:
ключ = имя параметра,
значение = его значение.
Получаем Python-словарь, который удобно использовать:
print(obj_query['q'])   # Cat and dog
print(obj_query['ie'])  # utf-8



# ISDIGIT
number = "12345"
print(number.isdigit())  # Виведе: True

text = "Number123"
print(text.isdigit())  # Виведе: False


# проверка ввел ли пользователь число
user_input = input("Введіть число: ")
if user_input.isdigit():
    print("Це дійсно число!")
else:
    print("Це не число!")


# проверка на цифры в строке
for char in "Hello 123":
    if char.isdigit():
        print(f"'{char}' - це цифра")
    else:
        print(f"'{char}' - не цифра")
'H' - не цифра
'e' - не цифра
'l' - не цифра
'l' - не цифра
'o' - не цифра
' ' - не цифра
'1' - це цифра
'2' - це цифра
'3' - це цифра


