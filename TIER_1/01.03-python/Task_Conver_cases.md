

snake_case
PascalCase
camelCase


Задача: camelCase -> snake_case
userIsLoggedIn -> user_is_logged_in

# userIsLoggedIn 
1. малые буквы пропустить
2. Перед большими поставть _
3. перевести большие буквы в малые


def convert_camel_to_snake(text): 
    result = ""
    for letter in text:
        if letter.isupper():
            result += "_" + letter.lower()
        else:
            result += letter
    print(result)

convert_camel_to_snake("bankAccountInfo")


Разделы функции:
1. def + name of func + () -> называется function signature
2. от начала def до конца print(result) - declaration
3. все, что внутри функции (под строчкой def) - function body
4. function call: convert_camel_to_snake("bankAccountInfo")
5. function parameters - то, что внутри скобок в начале "def convert_camel_to_snake(text):"
6. arguments: convert_camel_to_snake("bankAccountInfo")