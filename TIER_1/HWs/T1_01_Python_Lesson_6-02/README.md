# Task: Get Cats Info (Lesson 6 - Python Basics)

## Description
This project contains a simple program that reads information about cats from a text file and returns it as a list of dictionaries.  
Each cat has three parameters: unique ID, name, and age.  

---

## Project Structure
```
T1_01_Python_Lesson_6-02/
│
├── main.py              # Reads cats info from a file and prints it
├── cats_generator.py    # Generates fake cats data using Faker
├── cats_file.txt        # Text file with fake cats data
└── .venv/               # Virtual environment
```

---

## How It Works

### 1. Generate fake data
Run the generator script to create a text file with fake cat data:
```
python cats_generator.py
```

This will create a file cats_file.txt with lines like:
```
60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
```

### 2. Read cats info
Run the main script:
```
python main.py
```

Output example:
```
{'id': '60b90c1c13067a15887e1ae1', 'name': 'Tayson', 'age': '3'}
{'id': '60b90c2413067a15887e1ae2', 'name': 'Vika', 'age': '1'}
{'id': '60b90c2e13067a15887e1ae3', 'name': 'Barsik', 'age': '2'}
```

---

## Function Description
### `get_cats_info(path)`

Purpose:  
Reads the file line by line, splits each line into ID, name, and age, and returns a list of dictionaries.

Returns:
```
[{'id': str, 'name': str, 'age': str}, ...]
```

Handles Errors:
1. File not found  
2. General exceptions while reading the file

---

## Requirements
Before running the code, install required libraries (inside virtual environment):
```
pip install faker
```
Python version: **3.8+**

---

**Example Output**
```
File 'cats_file.txt' created with 10 fake cats.
{'id': '9e99b856-b6ec-4d96-9995-4d98ad9ff113', 'name': 'John', 'age': '6'}
{'id': 'c2df93c2-67cf-4194-9c6a-864799f88e7f', 'name': 'Chelsey', 'age': '5'}
{'id': '6acbfbe9-f261-446b-a59f-61f726702da0', 'name': 'Matthew', 'age': '9'}
...
```

## Created by:
**Author:** Oleksandr Skriabikov  
Created as part of the **Neoversity Python course, Lesson 6, Home Task 2**
