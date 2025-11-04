
# formatted string

numbers = [1, 2, 12, 13, 12, 3, -1, 2, 41]
message = "Max number is {}, min is {}".format(max(numbers), min(numbers))
print(message)

ИЛИ:
numbers = [1, 2, 12, 13, 12, 3, -1, 2, 41]
message = f"Max number is {max(numbers)}, min is {min(numbers)}"
print(message)


debt = 0
while debt < 1000:
    debt += 10
    print(f"Current debt: {debt}")
Current debt: 10
Current debt: 20
Current debt: 30
...
Current debt: 1000


