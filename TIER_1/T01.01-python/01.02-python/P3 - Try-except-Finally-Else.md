import random

attempts = 0
number = random.randint(0, 100)

# Try - если пользователь введет sdsdsadsa - программа не упадет
try: 
    guess = int(input("Guess my number between 1 and 1000: "))
    guess = guess / 0
except (ValueError, ZerpDivisionError): 
    guess = 0

ИЛИ (на каждую ошибку отдельно):
try: 
    guess = int(input("Guess my number between 1 and 1000: "))
    guess = guess / 0
except ValueError:
    guess = 0
except ZeroDivisionError:
    print("You can't divide in zero")

ИЛИ (на любую ошибку):
try: 
    guess = int(input("Guess my number between 1 and 1000: "))
    guess = guess / 0
except:
    guess = 0

# ! Лучше писать except на каждую ошибку отдельно


# FINALLY 
try:
    open("users.txt)
except:
    print("File does not exist")
finally:
    file.close()
# Т.Е. файл будет закрыт в любом случае, даже при ошибке



# ELSE
try:
    save_user_in_db()
except:
    rollback()
    print("File does not exist")
else: 
    save()
finally: 
# Т.Е. если что-то случится - мы откатимся назад, а если ошибок не было - все сохранится 
