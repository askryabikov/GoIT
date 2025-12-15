# basic usage
stk0=[]

stk0.append('a') # push
stk0.append('b')
stk0.append(3)
print(stk0)  

print(stk0.pop())  # pop
print(stk0)  

def is_empty(stack):
    return len(stack) == 0
print(is_empty(stk0))  # Output: False

def peek(stack):
    if is_empty(stack):
        return None
    return stack[-1]
print(peek(stk0))  # Output: 'b'

# stk0.pop()
# stk0.pop()
# stk0.pop() #!
# print(peek(stk0))
# print(is_empty(stk0))  

