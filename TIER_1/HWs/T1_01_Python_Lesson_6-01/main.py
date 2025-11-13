def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:   # r - for reading
            lines = file.readlines()   # read the whole file
        total = 0     # sum of all salaries
        count = 0     # number of employees

        for line in lines:   # cycle for counting each line
            line = line.strip()    # remove spaces and newlines
            name, salary = line.split(",")   # split line into name and salary
            total += int(salary)   # add salary to total
            count += 1   # count number of employees

        if count == 0:   # in case file is empty
            return (0, 0)

        average = total / count
        return (total, average)   # to return as tuple

    except FileNotFoundError:   # in case file not found
        print("Помилка: файл не знайдено.")
        return (0, 0)

    except Exception as e:   # in case of any other error
        print("Помилка при обробці файлу:", e)
        return (0, 0)

if __name__ == "__main__":
    total, average = total_salary("salary_file.txt")
    print(f"Загальна сума заробітної плати: {total} usd, Середня заробітна плата: {average:.2f} usd")
    # average:.2f} - 2 digits after comma