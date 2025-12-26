import random

class UniversalHash:
    def __init__(self, m, max_key):
        self.m = m
        self.p = self._next_prime(max_key)
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)

    def _next_prime(self, n):
        while True:
            n += 1
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    break
            else:
                return n

    def hash(self, key):
        return ((self.a * key + self.b) % self.p) % self.m

# Приклад використання:
hasher = UniversalHash(100, 1000)
print(hasher.hash(123))
print(hasher.hash(456))


# Этот код создает универсальную хеш-функцию для хеширования ключей в таблицу размером 100, где максимальный ключ – 1000.

# В конструкторе __init__мы создаем следующие атрибуты:
# m - размер хэш-таблицы.
# max_key — максимально возможное значение ключа.
# p — простое число, которое больше max_key. Его используют для модульной арифметики в хэш-функции.
# a и b— случайные константы, определяющие хэш-функцию. 
# Эти константы выбираются при каждом создании нового экземпляра UniversalHash, что делает каждую хэш-функцию уникальной.


# Метод _next_prime находит следующее простое число после заданного числа n. Он полезен для нахождения p.
# Метод hash определяет хэш-функцию для заданного ключа key. Он использует модульную арифметику для генерации хэша.