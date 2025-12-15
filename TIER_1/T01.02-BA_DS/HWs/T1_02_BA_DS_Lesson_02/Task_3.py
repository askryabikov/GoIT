def check_brackets(text):
    stack = []                   # create an empty stack
    pairs = {")": "(", "]": "[", "}": "{"}  # list possible options
    open = {"(", "[", "{"}       # set of opening brackets
    close = {")", "]", "}"}      # set of closing brackets

    for ch in text:              # check all characters
        if ch in open:           # for an opening bracket
            stack.append(ch)     # push to stack
        elif ch in close:        # for a closing bracket
            if not stack:        # if stack is empty - nothing to match
                return False     # if not symmetric
            top = stack.pop()    # take last opened bracket
            if top != pairs[ch]: # if types do not match
                return False     # not symmetric

    return len(stack) == 0       # symmetric ONLY if no unclosed brackets left


expr = input("Enter expression: ")     # user input

if check_brackets(expr):
    print("Симетрично")         
else:
    print("Несиметрично")
