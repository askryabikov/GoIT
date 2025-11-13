import random
from faker import Faker # Module Faker already installed on virtual environment

fake = Faker()

def get_mocked_salary():
    fake = Faker()
    mock = {
        "developer_name": fake.name(),                # generate name in English
        "monthly_salary": random.randint(1000, 6000)  # random salary close to hometask
    }
    return mock

def generate_salary_file(path="salary_file.txt", n=69): # n - number of employees
    with open(path, "w", encoding="utf-8") as file:  # w - open file for writing
        for _ in range(n): # start cycle to create data
            record = get_mocked_salary()  # write line as: Name, Salary
            file.write(f"{record['developer_name']},{record['monthly_salary']}\n")
    print(f"Файл '{path}' створено з {n} записами фейкових зарплат.")

if __name__ == "__main__": # run directly
    generate_salary_file("salary_file.txt", 69) 