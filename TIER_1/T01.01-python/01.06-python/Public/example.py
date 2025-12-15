# my_string = "hello world"
# print(my_string, end='#####\n')
# print(my_string, end='#####\n')

my_list = [1, 2, 3, 'hello']
second_list = [4, 5, 6, 7]
# # a, b = my_list[1:]
# _, a, b = my_list
# # a = my_list[0]
# # b = my_list[1]

# print(a, b)

# print(list(enumerate(my_list)))

# for i, element in enumerate(my_list):
#     print(f'Number: {i}')
#     print(element)

# print(list(zip(my_list, second_list)))

for i, (first_element, second_element) in enumerate(zip(my_list, second_list)):
    print(f'Number: {i}')
    print(first_element, second_element)
