import sys
from itertools import zip_longest
from colorama import Fore, Style
'''
Написати додаток, який працює як diff
'''

if len(sys.argv) < 3:
    print('Please provide two filenames to compare')
    sys.exit()

# file_name_one = sys.argv[1]
# file_name_two = sys.argv[2]

_, file_one, file_two = sys.argv

# Скажемо що файли не великі і їх можна читати повністю

# print(file_name)
with open(file_one) as file:
    # for line in file.readlines():
    file_one_lines = file.readlines()

with open(file_two) as file:
    # for line in file.readlines():
    file_two_lines = file.readlines()

# Поки що приймемо що файли однакової довжини
# ['123\n', 'abc\n', '456\n']
# ['456\n', 'def\n', '123\n']

# for i in range(len(file_two_lines)):
#     file_one_line = file_one_lines[i]
#     file_two_line = file_two_lines[i]

#     if file_one_line != file_two_line:
#         print(i)
#         print(f'< {file_one_line.rstrip()}')
#         print(f'> {file_two_line.rstrip()}')

for i, (file_one_line, file_two_line) in enumerate(zip_longest(file_one_lines, file_two_lines, fillvalue='')):
    if file_one_line != file_two_line:
        print(i + 1)
        print(f'{Fore.RED}< {file_one_line.rstrip()}{Style.RESET_ALL}')
        print(f'{Fore.GREEN}> {file_two_line.rstrip()}{Style.RESET_ALL}')
