def get_cats_info(path):
    cats_list = []    # create an empty list to store dictionaries

    try:
        with open(path, "r", encoding="utf-8") as file:   # r for reading
            lines = file.readlines()  # read all lines

        for line in lines:   # start cycle
            line = line.strip()  # remove spaces and newlines
            cat_id, name, age = line.split(",")   # divide by comma id, name, age

            cat_dict = { # create dictionary for each cat
                "id": cat_id,
                "name": name,
                "age": age
            }

            cats_list.append(cat_dict)   # add dictionary into the list

        return cats_list   # return final version of the list

    except FileNotFoundError:   # in case file not found
        print("Помилка: файл не знайдено.")
        return []
    except Exception as e:   # in case of any other error
        print("Помилка при обробці файлу:", e)
        return []

if __name__ == "__main__":
    cats_info = get_cats_info("cats_file.txt")   # check generated file
    for cat in cats_info:   # show each cat on a new line
        print(cat)

