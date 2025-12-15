

import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000: # 1st rule for appropriate input numbers
        print("Numbers must be between 1 and 1000")
        return []
    if quantity > (max - min + 1) or quantity <= 0: # 2nd rule: cannot get more unique numbers than quantity
        print("Incorrect quantity of numbers")
        return []

    numbers = []
    while len(numbers) < quantity: # continue cycle until quantity number is met
        num = random.randint(min, max) # random numbers between 1st and 2nd input
        if num not in numbers: # check for unique numbers / skip repetitive number
            numbers.append(num) # add one more unique number into return

    numbers.sort() # sort numbers in ascending order
    return numbers

print(get_numbers_ticket(1, 49, 6)) # [7, 8, 22, 27, 43, 49]
print(get_numbers_ticket(1, 10, 3)) # [4, 8, 10]
print(get_numbers_ticket(1, 5, 10)) # False test
