import random

attempts = 0
number = random.randint(0, 100)

guess = int(input("Guess my number between 1 and 1000: "))

while attempts < 10:
    attempts += 1
    if guess > number:
        print(f"{guess} is too high")
    elif guess < number:
        print(f"{guess} is too low")
    else:
        print(f"Congrats, you won in {attempts} attempts")
        break

    guess = int(input("Guess again pls >>> "))

print(12)
