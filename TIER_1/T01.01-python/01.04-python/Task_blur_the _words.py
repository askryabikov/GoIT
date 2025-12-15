import re

text = " to be or not to be an Idiot. BE a good coder!"

# Задача:
result = " to be or not to be an *****. BE a good coder!"

def replace_bad_words(text):
    pattern = r"idiot"
    return re.sub(pattern, "*****", text, flags=re.IGNORECASE)

replace = replace_bad_words(text)
print(result)

# Ignorecase = не обращать внимания на буквы в верхнем регистре




