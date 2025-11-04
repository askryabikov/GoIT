from datetime import datetime, timedelta, timezone

# Текущая дата и время
print(datetime.now())

# Пример с временной зоной Польши (если доступен zoneinfo)
# datetime.now(tz=tz.gettz("Poland"))

# Создание объекта timezone с разницей -1 час
zone = timezone(timedelta(hours=-1))
print(zone)

# Проверка работы timezone с разницей в секундах
zone = timezone(timedelta(seconds=3600))
print(zone)

# Использование timezone в datetime
print(datetime.now(tz=zone))

Что делает этот код:

datetime.now() → возвращает текущее локальное время.
timezone(timedelta(hours=-1)) → создаёт часовой пояс, смещённый на -1 час от UTC.
datetime.now(tz=zone) → возвращает текущее время с учётом указанного часового пояса.
timedelta(seconds=3600) → это просто способ задать 1 час через секунды (1 час × 3600 секунд).