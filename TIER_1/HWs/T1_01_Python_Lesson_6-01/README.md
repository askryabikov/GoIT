# Salary Analyzer (Python Homework)

## Task Description
This program analyzes a text file containing monthly salaries of software developers in a company.  
Each line in the file has the following format:

```
Name,Salary
```

Example:
```
Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
```

The program calculates:
- the **total sum** of all salaries;  
- the **average salary**.

---

## Project Files
```
| File | Description |
|------|--------------|
| fake_salary_generator.py | Generates the salary_file.txt file with fake names and salaries using the **Faker** library |
| main.py | Reads the file and calculates the total and average salary |
| salary_file.txt | Text file containing developer names and their salaries |
| .venv/ | Python virtual environment |
| README.md | Project documentation |
```

---

## Requirements
- Python 3.10+  
- Library [`faker`](https://pypi.org/project/Faker/)

Install dependencies:
```
pip install faker
```

---

## 🚀 How to Run

1️⃣ Activate the virtual environment (if not already active):  
**Windows PowerShell:**
```
.\.venv\Scripts\Activate.ps1
```
**Mac/Linux:**
```
source .venv/bin/activate
```

2️⃣ Generate fake salary data:
```
python fake_salary_generator.py
```

3️⃣ Run the main analysis program:
```
python main.py
```

**Example Output:**
```
File 'salary_file.txt' created with 69 fake salary records.
Total salary: 229,829 usd, Average salary: 3,330.86 usd
```

---

## Program Logic
1. `fake_salary_generator.py` creates a text file with 69 randomly generated developer names and salaries (1000–6000 range).  
2. `main.py` opens and reads the file line by line.  
3. The program sums all salaries (**total**) and calculates the average (**average**).  
4. Results are printed in a clear format, rounded to two decimal places.

---

## Folder Structure
```
T1_01_Python_Lesson_6-01/
│
├── fake_salary_generator.py
├── main.py
├── salary_file.txt
├── README.md
└── .venv/
```

---

## Created by:
**Author:** Oleksandr Skriabikov  
Created as part of the **Neoversity Python course, Lesson 6, Home Task 1**
