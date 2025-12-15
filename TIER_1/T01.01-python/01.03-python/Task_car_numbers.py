
# Рандом для номеров машин

import random

# BC 6060 XA

set_of_letters = ["A", "B", "C", "E", "H", "K", "M", "P", "T", "X"]
set_of_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

l1 = random.choices(set_of_letters, k=2)
l2 = str(random.randint(0, 9999))
if len(l2) < 4:
    l2 = "0" * (4 - len(l2)) + l2 # - эти строки для добавления нолей для 1-, 2- и 3-значных чисел
# 0002



# ИЛИ:


import random

# BC 6060 XA

set_of_letters = ["A", "B", "C", "E", "H", "K", "M", "P", "T", "X"]
set_of_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

l1 = random.choices(set_of_letters, k=2)
l2 = f" {random.randint(0, 9999):04} "
l3 = random.choices(set_of_letters, k=2)

plate_number = "".join(l1) + l2 + "".join(l3)
# 1. l1 приведет список букв
# 2. сами цифры
# 3. l2 тоже добавит 2 буквы
print(plate_number)




