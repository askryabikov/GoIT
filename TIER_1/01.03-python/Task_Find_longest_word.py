# Given a string of space separated words, return the longest word.
# If there are multiple longest words, return the rightmost longest word.

# split
# len
# sort

text = "red white blue violet"
words = text.split()

# - Посчитать первое слово самым длиным, затем в цикле сравнивать с первым словом
res = words[0]
for word in words:
    if len(word) >= len(res):
        res = word

#ИЛИ через список:
text = "red white blue violet"
words.sort(key=len)
words
['red', 'blue', 'white', 'violet']
# теперь само длиное впереди:
words.sort(key=len, reverse=True)
['violet', 'white', 'blue', 'red']






# Найти последовательность с самым большим количеством согласных
# ЧТО НУЖНО:
# Get list of vowels (согласных)
# For loop - использовать цикл для переборки
text = "aevsaefsdsade asds d asd sa Oleeeeeeeeeh"

vowels - "aeiou" # - определили гласные буквы
for char in text: # - начали цикл
    if char.lower() not in vowels # - переведем все в нижний регистр
        text = text.replace(char, ".") # - все согласные заменили на точки

chains = text.splt(".")
chains.sort(key=len)
print(text)
print(chains)

ae..ae...a.e.a........a...a..O.eeeeeeee.
['ae', 'ae', '', 'a', 'e', '', '', '', 'a', 'e', 'a', 'a', '', '',
 '', 'a', 'e', '', 'a', '', 'O', '', 'eeeeeeee']
