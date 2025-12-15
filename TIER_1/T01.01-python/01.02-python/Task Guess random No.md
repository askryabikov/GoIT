
Game Guess random number

import random

attempts = 0
number = random.randint(0, 100)

while attempts < 10:
    guess = int(input("Guess my number btw 1 and 100 >>> "))
    attempts += 1

    if guess > number:
        print(f"{guess} is too high")
    elif guess < number:
        print(f"{guess} is too low")
    else:
        print(f"Congrats, you won in {attempts} attempts!")
        break
else:
    print(f"Sorry, you've used all attempts. The number was {number}.")

print("You won!")
