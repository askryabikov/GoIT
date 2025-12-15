import random
import pathlib

current_dir = pathlib.Path(__file__).parent

def get_random_joke():
    try:
        with open(current_dir / "jokes.txt", "r", encoding="utf-8") as file:
            jokes = file.readlines()
            return random.choice(jokes).strip()
    except FileNotFoundError:
        return "Не вдалося знайти файл з анекдотами."
    


# Этот код определяет функцию get_random_joke(), которая открывает файл jokes.txt, расположенный 
# в той же директории, что и скрипт, и выбирает из него случайный анекдот. Переменная 
# current_dir определяет директорию, где находится файл скрипта. Нам это необходимо, 
# чтобы путь к файлу current_dir / "jokes.txt" всегда был правильным, где бы мы 
# не выполнили нашу программу.

# В функции get_random_joke() файл jokes.txt открывается с помощью контекстного менеджера with, 
# что гарантирует правильное закрытие файла после завершения работы с ним. Анекдоты из файла 
# читаются в список jokes, из которого затем случайным образом выбирается один 
# с помощью random.choice(jokes). Если файл jokes.txt не найден, функция возвращает 
# строку "Не вдалося знайти файл з анекдотами." для информирования пользователя об ошибке.