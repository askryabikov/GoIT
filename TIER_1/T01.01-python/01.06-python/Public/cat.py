import sys
'''
Написати аналог додатку cat, який буде читати файли
'''

# print("Hello, world!")
# print(sys.argv)

if len(sys.argv) < 2:
    print('Please provide filename')
    sys.exit()

file_name = sys.argv[1]
# print(file_name)

with open(file_name) as file:
    # for line in file.readlines():
    for line in file:
        print(line.rstrip())

