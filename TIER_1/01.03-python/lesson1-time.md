import datetime

import datetime
now = datetime .datetime .now ()
 print (now)

2023 - 12 - 14  12 : 39 : 29 . 992996

from datetime import datetime
from datetime import datetime

current_datetime = datetime .now ()

print (current_datetime.year) 
print (current_datetime.month) 
print (current_datetime.day) 
print (current_datetime.hour) 
print (current_datetime.minute) 
print (current_datetime.second) 
print (current_datetime.microsecond) 
print (current_datetime.tz)

from datetime import datetime

current_datetime = datetime .now ()
 print (current_datetime.date() )
 print (current_datetime.time() )
2023 - 12 - 14 
12 : 59 : 06 . 709007


datetime.datetime.combine(date _ object , time _ object )


import datetime
# Создание объектов date и time 
date_part = datetime.date( 2023 , 12 , 14 )
 time_part = datetime.time( 12 , 30 , 15 )
# Комбинирование даты и времени в один объект datetime 
combined_datetime = datetime.datetime.combine(date_part, time_part)
print (combined_datetime) # Выведет "2023-12-14 12:30:15"


import datetime
# Создание объекта datetime с конкретной датой 
specific_date = datetime.datetime( year =2020, month =1, day =7)
print (specific_date) # Выведет "2020-01-07 00:00:00"


import datetime

# Создание объекта datetime с конкретной датой и временем 
specific_datetime = datetime.datetime( year =2020, month =1, day =7, hour =14, minute =30, second =15)
print (specific_datetime) # Выведет "2020-01-07 14:30:15"


from datetime import datetime
# Создание объекта datetime
now = datetime.now()
# Получение номера дня недели
day_of_week = now.weekday()
# Возвратное число от 0 (понедельник) до 6 (воскресенье) 
print ( f"Сегодня: {day_of_week} " )  


from datetime import datetime

# Создание двух объектов datetime
datetime1 = datetime(2023, 3, 14, 12, 0)
datetime2 = datetime(2023, 3, 15, 12, 0)

# Сравнение дат 
print (datetime1 == datetime2) # False , потому что даты не одинаковые
 print (datetime1 != datetime2) # True , потому что датьы различные
 print (datetime1 < datetime2) # True , потому что datetime1 предшествует
 datetime2 print ( date datetime1 не наступает за datetime2
False 
True 
True 
False

Ключевые аспекты: методы работы с датами и временем

datetime.now(): Метод возвращает объект datetime, содержащий текущую дату и время.
datetime.date(): Этот метод возвращает объект date, представляющий только дату (без времени).
datetime.time(): Метод возвращает объект time, содержащий только время (без даты).
datetime.combine(date, time): Этот метод используется для объединения объектов dateи timeсоздания нового объекта datetime.
datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0): Конструктор класса datetimeпозволяет создать объект datetimeс конкретной датой и временем.
weekday(): Метод определяет номер дня недели для указанной даты, где понедельник имеет номер 0, а воскресенье – 6.




from datetime import timedelta
delta = timedelta(
    days =50,
     seconds =27,
     microseconds =10,
     milliseconds =29000,
     minutes =5,
     hours =8,
     weeks =2
)
print (delta)
64 days, 8 : 05 : 56.000010



from datetime import datetime
seventh_day_2019 = datetime( year =2019, month =1, day =7, hour =14)
seventh_day_2020 = datetime( year =2020, month =1, day =7, hour =14)

difference = seventh_day_2020 – seventh_day_2019
print (difference) # 365 days, 0:00:00
 print (difference.total_seconds()) # 31536000.0



from datetime import datetime, timedelta
now = datetime.now()
future_date = now + timedelta( days =10) # Добавляем 10 дней до текущей даты
 print (future_date)
2023 - 12 - 28  14 : 08 : 46 . 342976



от datetime import datetime, timedelta
seventh_day_2020 = datetime(year= 2020 , month= 1 , day= 7 , hour= 14 )
 four_weeks_interval = timedelta(weeks= 4 )
print (seventh_day_2020 + four_weeks_interval) # 2020 - 02 - 04  14 : 00 : 00 
print ( seventh_day_2020 - four_weeks_interval) # 2019 - 12 - 10  14 : 0
2020-02-04 14:00:00 2019-12-10 14:00:00​ ​​​​​
​​​​​ ​​​​​

from datetime import datetime
# Создание объекта datetime 
date = datetime( year =2023, month =12, day =18)
# Получение порядкового номера
ordinal_number = date.toordinal()
print (f "Порядковый номер даты {date} составляет {ordinal_number}" )
Порядковый номер даты 2023 -12 -18 00:00:00 составляет 738872



from datetime import datetime
# Установление даты сожжения Москвы Наполеоном (14 сентября 1812) 
napoleon_burns_moscow = datetime( year =1812, month =9, day =14)
# Текущая дата
current_date = datetime.now()
# Расчет количества дней
days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
print (days_since)
77161


from datetime import datetime
# Текущее время
now = datetime.now()
# Конвертация datetime в timestamp 
timestamp = datetime.timestamp(now)
print( timestamp ) # Выведет timestamp текущего времени
1702854066 . 56633


from datetime import datetime
# Предположим, есть timestamp 
timestamp = 1617183600
# Конвертация timestamp обратно в datetime
dt_object = datetime.fromtimestamp(timestamp)
print (dt_object)   # Выведет соответствующий datetime
2021-03-31 12:40:00​​​ ​​​​​


datetime_object.strf time ( format )
%Y- год с четырьмя цифрами (например, 2023).
%y- год с двумя цифрами (например, 23).
%m– месяц как номер (например, 03для марта).
%d- день месяца как номер (например, 14).
%H- час (24-часовой формат) (например, 15).
%I- час (12-часовой формат) (например, 03).
%M- минуты (например, 05).
%S- секунды (например, 09).
%A- полное название дня недели (например, Tuesday).
%a- сокращенное название дня недели (например, Tue).
%B- полное название месяца (например, March).
%bили %h– сокращенное название месяца (например, Mar).
%p– AM или PM для 12-часового формата.



from datetime import datetime
now = datetime.now()
# Форматирование даты и времени 
formatted_date = now.strftime( " %Y - %m - %d  %H : %M : %S " )
 print (formatted_date)

# Форматирование только даты 
formatted_date_only = now.strftime( " %A , %d  %B  %Y " )
 print (formatted_date_only)

# Форматирование только времени 
formatted_time_only = now.strftime( " %I : %M  %p " )
 print (formatted_time_only)  

# Форматирование только даты 
formatted_date_only = now.strftime( " %d . %m . %Y " )
 print (formatted_date_only)
2023 - 12 - 18  01 : 37 : 07 
Вторник , 18 Декабря 2023 
01 : 37 AM
18 . 12 . 2023


datetime_object = datetime.strptime( string , format )
где:
string- строка, содержащая дату и/или время.
format- строка формата, указывающая, как разобрать string.



from datetime import datetime
# Предположим, у нас есть дата в виде строки 
date_string = "2023.03.14"
# Преобразование строки в объект datetime 
datetime_object = datetime.strptime(date_string, " %Y . %m . %d " )
 print (datetime_object)   # Выведет объект datetime, соответствующий указанной дате и времени
2023 - 03 - 14  00 : 00 : 00



from datetime import datetime

# Текущая дата и время
now = datetime.now()
# Конвертация в формат ISO 8601
iso_format = now.isoformat()
print (iso_format)
2023 - 12 - 14 T15: 43 : 42 . 651309


from datetime import datetime
iso_date_string = "2023-03-14T12:39:29.992996"
# Конвертация из ISO формата
date_from_iso = datetime.fromisoformat(iso_date_string)
print (date_from_iso)
2023 - 03 - 14  12 : 39 : 29 . 992996


from datetime import datetime
# Создание объекта datetime
now = datetime.now()
# Использование isoweekday() для получения дня недели
day_of_week = now.isoweekday()
print ( f "Сегодня: {day_of_week} " )   # Вернет число от 1 до 7, что соответствует дню недели


from datetime import datetime
# Створення об'єкта datetime
now = datetime.now()
# Використання isoweekday() для отримання дня тижня
day_of_week = now.isoweekday()
print(f"Сьогодні: {day_of_week}")  # Поверне число від 1 до 7, що відповідає дню тижня
Сьогодні: 4



from datetime import datetime
# Створення об'єкта datetime
now = datetime.now()
# Отримання ISO календаря
iso_calendar = now.isocalendar()
print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")
ISO рік: 2023, ISO тиждень: 50, ISO день тижня: 4



from datetime import datetime, timezone
local_now = datetime.now()
utc_now = datetime.now(timezone.utc)
print(local_now)
print(utc_now)  # Виведе поточний час в UTC
2023-12-14 16:39:33.883454
2023-12-14 14:39:33.883454+00:00



from datetime import datetime, timezone, timedelta
utc_time = datetime.now(timezone.utc)
# Створення часової зони для Східного часового поясу (UTC-5)
eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# Перетворює час UTC в час Східного часового поясу
print(eastern_time)  
2023-12-14 09:43:06.778253-05:00



from datetime import datetime, timezone, timedelta

# Припустимо, місцевий час належить до часової зони UTC+2
local_timezone = timezone(timedelta(hours=2))
local_time = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)

# Конвертація локального часу в UTC
utc_time = local_time.astimezone(timezone.utc)
print(utc_time)  # Виведе час в UTC
2023-03-14 10:30:00+00:00



from datetime import datetime, timezone, timedelta

# Час у конкретній часовій зоні
timezone_offset = timezone(timedelta(hours=2))  # Наприклад, UTC+2
timezone_datetime = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset)

# Конвертація у формат ISO 8601
iso_format_with_timezone = timezone_datetime.isoformat()
print(iso_format_with_timezone)

2023-03-14T12:30:00+02:00



import time
current_time = time.time()
print(f"Поточний час: {current_time}")
Поточний час: 1702857932.326853



import time
print("Початок паузи")
time.sleep(5)
print("Кінець паузи")



import time
current_time = time.time()
print(f"Поточний час: {current_time}")
readable_time = time.ctime(current_time)
print(f"Читабельний час: {readable_time}")

Поточний час: 170285823.9412928
Читабельний час: Mon Dec 18 02:08:43 2023



import time

current_time = time.time()
print(f"Поточний час: {current_time}")

local_time = time.localtime(current_time)
print(f"Місцевий час: {local_time}")

Поточний час: 1702861070.8583968
Місцевий час: time.struct_time(tm_year=2023, tm_mon=12, tm_mday=18, tm_hour=2, tm_min=57, tm_sec=50, tm_wday=0, tm_yday=352, tm_isdst=0)


tm_year - рік
tm_mon - місяць від 1 до 12
tm_mday - день місяця від 1 до 31
tm_hour - години від 0 до 23
tm_min - хвилини від 0 до 59
tm_sec - секунди від 0 до 59
tm_wday - день тижня від 0 до 6
tm_yday - день року від 1 до 366
tm_isdst - прапорець літнього часу. 0 означає, що літній час не діє, -1 - інформація відсутня, 1 - літній час діє


import time

# Записуємо час на початку виконання
start_time = time.perf_counter()

# Виконуємо якусь операцію
for _ in range(1_000_000):
    pass  # Просто проходить цикл мільйон разів

# Записуємо час після виконання операції
end_time = time.perf_counter()

# Розраховуємо та виводимо час виконання
execution_time = end_time - start_time
print(f"Час виконання: {execution_time} секунд")

Час виконання: 0.04927480001060758 секунд


# Один мільйон
a = 1_000_000
print(a)  # Виведе 1000000

# Десять мільйонів
b = 10_000_000
print(b)  # Виведе 10000000

# Один мільярд
c = 1_000_000_000
print(c)  # Виведе 1000000000


time.time(): Повертає поточний час у секундах з 1 січня 1970 року (epoch time).
time.sleep(seconds): Зупиняє виконання програми на вказану кількість секунд.
time.ctime([seconds]): Перетворює часову мітку в текстове представлення, зрозуміле для людини.
time.localtime([seconds]): Перетворює часову мітку в структуру struct_time у місцевій часовій зоні.
time.gmtime([seconds]): Аналогічно localtime, але повертає struct_time у форматі UTC.
time.perf_counter(): Повертає лічильник з високою точністю для вимірювання коротких інтервалів часу.