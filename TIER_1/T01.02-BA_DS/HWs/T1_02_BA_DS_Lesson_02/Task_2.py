from collections import deque

def is_palindrome(text):
    d = deque(text)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

word = input("Введіть слово: ")

if is_palindrome(word):
    print("Паліндром")
else:
    print("Не паліндром")
