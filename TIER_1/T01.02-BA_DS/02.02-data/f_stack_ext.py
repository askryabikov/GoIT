# advanced oop usage
class stack(list):

    def pop(self):
        if len(self) == 0:
            print('Stack is empty')
            return None
        else:
            return super().pop()
    def push(self, item):
        super().append(item)
    def is_empty(self): 
        return len(self) == 0
    def peek(self):
        if len(self) == 0:
            return None
        else:
            return self[-1]
    

stk1=stack()
stk1.push('a') # push
stk1.push('b')
stk1.push(3)

print(stk1)
# stk2=stack(stk1)
# print(stk1.pop())  # pop
# print(stk1)
# print(stk1.peek())
# stk1.pop()
# stk1.pop()
# stk1.pop() #!
# print(stk1.peek())  # Output: None
# print(stk1.is_empty())  # Output: True

# print(stk2)