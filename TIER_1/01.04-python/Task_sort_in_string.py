import re

claim = "People love Python."

print(re.search(r"Python", claim)) # - найдет везде
print(re.match(r"Python", claim)) # - здесь НЕ найдет, т.к. будет искать только в начале предложения






