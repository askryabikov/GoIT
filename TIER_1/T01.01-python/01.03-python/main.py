from datetime import date, datetime

today = date(year=2025, month=10, day=12)
>>> type(today)
class 'datetime.date'
>>> today.day
7
>>> today.year
2025
>>> date.today()
datetime.date(2025, 10, 31)

today = "2025-10-7"


# %Y: 4-digit year
# %y: 2-digit year
# %m: 2-digit month (01–12)
# %d: 2-digit day of the month (01–31)
# %H: 2-digit hour (00–23)
# %M: 2-digit minute (00–59)
# %S: 2-digit second (00–59)


from datetime import date, datetime

user_input = "2025-10-7" 

# string parse time # str -> datetime
d = datetime.strptime(user_input, "%Y-%m-%d")
print(d)




from datetime import datetime
birthday = "14-06-2000"
# --- str -> datetime
birthday_date = datetime.strptime(birthday, "%d-%m-%Y")
print(birthday_date)

# --- datetime -> str
# %A - узнать день недели (словарь python на datetime)
# %B - месяц года
res = birthday_date.strftime("%A %B")
print(res)
wednesday June

# Т.Е. strftime - противоположная от strptime



# TIMEDELTA - умеет считать только количество дней
start_date = date(year=2022, day=22, month=2)
end_date = date(year=2025, day=7, month=10)
end_date - start_date
datetime.timedelta(days=1323) 



# TEXT
text = "To be or not to be"
text = text.lower()
# str - тип immutable - его нельзя переделвть, поэтому все изменения - изменения копии
text.capitalize() # - все с большой
text.isalpha # - проверка является ли это буквой
text.isalnum; text.isdigit # - проверка является ли цифрой

"12".isdigit()
True

text = "   andrus@gmail.com"
text.strip() # - снимает пробелы и слева и справа
text.lstrip # - убирает пробелы слева
text.rstrip # - убирает пробелы справа
text.split() # --> ['To', 'be', 'or', not,...]

text = "name, last_name, email"
text.split(",") # --> ['name', 'last_name', 'email']

>>> text.split(",")
text = "name, last_name, email"
>>> columns = text.split(",")
>>> columns
"name, last_name, email"

>>> "|".join(columns) # - можно использовать любой разделитель
"name | last_name | email"



text = "To be or not to be"
text.replace("be", "быть") # - в скобках указывать что ищешь и что хочешь заменить
'To быть or not to быть' # - это копия
text = text.replace("be", "быть") 
'To быть or not to быть' # - это поменяли оригинал



# Узнать позици. ряда, слова, буквы
>>> text
'To быть or not to быть'
>>> text.find("or")
8
>>> text[8:] # - возвращает индекс 
'To быть or not to быть'
>>> text.index("or") # - находит первое вхождение 
8





