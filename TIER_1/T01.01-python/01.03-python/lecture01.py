import random
names = ["Oleh", "Alina", "Stepan", "Olha"]
random.choice(names)
#'Oleh'

random.choices(names, k=2) # k - quantity of choices
# ['Oleh', 'Olha']
random.choices(names, k=10)
# ["Oleh", 'Stepan', 'Olha',.....]

random.sample(names, k=4)
# ["Oleh", 'Stepan', 'Olha', 'Alina']
random.sample(names, k=10) # Sample does not approve duplicates
# Error 


cards = ["Q", "J", "2", "K"]
random.shuffle(cards)
cards
# ["j", "Q", "K", "2"]



random.randint(0, 3) # - random digits FROM and TO
# 2
# 1



 
