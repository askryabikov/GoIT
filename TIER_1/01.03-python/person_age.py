''''
Код для счета возраста
''''

#2000-01-01

def calculate_person_age(date_of_birth_str: str) -> int:
    pass

print(calculate_person_age("2000-01-01"))  # 25
# 2024-02-09 - ввели дату рождения меньше года назад
print(calculate_person_age("2024-02-09"))  # 0


ТЕСТ:
assert calculate_person_age ("2000-01-01") == 30
ЭТО ТО ЖЕ САМОЕ ЧТО И:
if calculate_person_age ("2000-01-01") != 30
    raise AssertionError



def calculate_person_age(date_of_birth_str: str) -> int:
    date_of_birth = datetime.strptime(date_of_birth_str, %Y-%m-%d) 
    today = datetime.today()
    return today.year - date_of_birth.year
    
# strptime =  str parse time




# 2
def calculate_person_age(date_of_birth_str: str) -> int:
    date_of_birth = datetime.strptime(date_of_birth_str, %Y-%m-%d) 
    today = datetime.today()

    date_of_birth_this_year = date_of_birth.replace(year=today.year)
    print(date_of_birth_this_year)

    if (date_of_birth_this_year > today):
        age -= 1

    return age

assert calculate_person_age ("2000-01-01") == 25
assert calculate_person_age ("2025-10-31") == 0
assert calculate_person_age ("2025-10-20") == 1



# 3 Сравнение дат
def is_date_in_the_past(month_one: int, day_one: int, month_two: int, day_two: int) -> bool:
    return (month_one < month_two) or (month_one == month_two and day_one < day_two)
# Даты
# 02-09 02-08
# 02-07 02-08
# 01-01 02-08
# 01-01 01-01

assert is_date_in_the_past(2, 9, 2, 8) == False
assert is_date_in_the_past(2, 7, 2, 8) == True
assert is_date_in_the_past(1, 1, 2, 8) == True
assert is_date_in_the_past(1, 1, 1, 1) == False

assert is_date_in_the_past(2, 10, 3, 9) == False