def check_brackets(text):
    stack = []

    for ch in text:
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0

expr = input("Введіть вираз: ")

if check_brackets(expr):
    print("Дужки правильні")
else:
    print("Дужки неправильні")
