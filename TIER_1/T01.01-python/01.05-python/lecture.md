

"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exist
In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)


Character   Meaning
'r' open for reading (default)
'w' open for writing, truncating the file first
'x' create a new file and open it for writing
'a' open for writing, appending to the end of the file if it exists
'b' binary mode
't' text mode (default)
'+' open a disk file for updating (reading and writing)

! Создают новые файлы только append и write








----WRITE

Создаст файл здесь в папке 
users = []
file = open("users.txt", mode="w")
file.write("Oleh Andrus")
file.close()


В ЧЕМ РАЗНИЦА:
СПОСОБ 1:
users = []
try:
    file = open("users.txt", mode="w")
    age = 30
    name = "Oleh Andrus"
    info = name + age
    file.write("Oleh Andrus")
except TypeError as e:
    print(e)
finally:
    file.close()

СПОСОБ 2:
(программа может упасть, но сам файл закроется):
users = []
with open("users.txt", mode="w") as file:
    age = 30
    name = "Oleh Andrus"
    info = name + age
    file.write("Oleh Andrus")
# т.е. он пишется без try/finally и file.close, но сам закроется


ЕЩЕ РАЗ В ЧЕМ РАЗНИЦА:
СПОСОБ 1:
try:
    file = open("users.txt", mode="r")
    data = file.read  
finally:
    file.close()

СПОСОБ 2:
with open("users.txt", mode="r") as file:
    data = file.read()
    print(data)
# Эти коды аналогичны друг другу




----APPEND

users = []
with open("users.txt", mode="a") as file:
    file.write("Ivan")
будет дописывать информацию c конца строки

users = []
with open("users.txt", mode="a") as file:
    file.write("\nIvan")
будет дописывать информацию с новой строки



----- TELL / READ

Tell - указывает позицию курсора
Read - читает с начала и потом откуда закончили

"To be or not to be"
with open("users.txt", mode="r") as file:
    print(file.tell())    # Tell показыввет на какой позиции курсор - здесь на 0
    print(file.read(5))   # Read читает с начала и потом откуда закончили
    print(file.tell())    # После прочтения курсор остался на пятой позиции
    print(file.read(2))   # Прочел еще 2 символа
    print(file.tell())    # И Курсор сдвинулся еще на 2 позиции
0
To be
5
 o
7


Еще пример работы:
"To be or not to be"
with open("users.txt", mode="r") as file:
    print(file.read())  # не указано количество симоволов на прочтение - прочтет все
    print(file.read())
Вывод:
>>> "To be or not to be"
>>> 
! Вторая команда ничего не прочла, т.к. первая команда прочла полностью



----- SEEK

Возвращает на начало строки
"To be or not to be"
with open("users.txt", mode="r") as file:
    print(file.tell())    # 0
    print(file.read(5))   # To be
    print(file.tell())    # 5
    file.seek(0)          # 0 - сбросили курсор на 0
    print(file.tell())    # 0
    print(file.read(5))   # To be
    print(file.tell())    # 5




----- READLINE()

Readline - читает одну строку

with open("users.txt") as file:
    users = file.readline()
Вывод (на примере файла из видео):
Ivan
Ivan
Ivan
Max и т.д.





-----"b" - BINARY MODE

ПЕРЕВОД КАРТИНКИ В ТЕКСТ И ОБРАТНО В ИЗОБРАЖЕНИЕ
STEP 1:
with open("1.jpg", mode="rb) as file:
    image_bin = file.read()
    print(image_bin)
    print(type(image_bin))
# mode="rb", где r - режим чтение, b - бинарный режим

Вывод:
b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01...' - Выведет длинную последовательность байтов

STEP 2:
with open("1.jpg", mode="wb) as file:
    file.write("image_bin")
# mode="wb", где w - режим записи, b - бинарный режим




------ SHUTIL

Копирование файла - SHUTIL.COPY
shutil.copy("source/netflix.jpg", "source/data/") 
# откуда и куда

shutil.copy("source/netflix.jpg", "source/data/netflix_logo.jpg") 
# откуда, куда и переименовать


Перемещение файла - SHUTIL.MOVE
shutil.move("source/netflix.jpg", "source/data/netflix_logo.jpg")


Копирование содержимого в папке в новосозданное место - SHUTIL.COPYTREE
shutil.copytree("source/data", "source/icons")



-------- РАБОТА С АРХИВАМИ 
- SHUTIL.MAKE_ARCHIVE 

import shutil
print(shutil.get_archive_formats())
path = shutil.unpack_archive("source_archived.zip", "unpacked/backup/")
print(path)



