import random
from faker import Faker   # Faker already installed in Virtual environment

fake = Faker()

def generate_cats_file(path="cats_file.txt", n=10):   # 10 - create 10 lines (cats)
    with open(path, "w", encoding="utf-8") as file:   # w - for writing
        for _ in range(n):   # start creation cycle
            cat_id = fake.uuid4()   # uuid4 - method for random IDs 
            cat_name = fake.first_name()   # cat name (random human name)
            cat_age = random.randint(1, 15)    # min and max 
            file.write(f"{cat_id},{cat_name},{cat_age}\n")   # line creation
    print(f"File '{path}' created with {n} fake cats.")   

if __name__ == "__main__":
    generate_cats_file("cats_file.txt", 10)