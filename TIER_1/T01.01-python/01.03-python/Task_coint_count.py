
# Possibility of flipping the coin on 1 side

# 1 / 2 -> 1 time in a row
# 1 / 4 -> 2 times in a row
# 1 / 8 -> 3 times in a row

import random

coin = {1: "Орел", 2: "Решка"}

count_O = 0 # - counts one side
count_P = 0 # - counts another side

sequence = []

while count_O < 4 and count_P <4:
    choice = random.randint
    if choice == 1:
        count_O += 1
        count_P = 0
    else:
        count_P += 1
        count_O = 0
    sequence.append(coin(choice))
print(sequence)
pring(len(sequence))