duration = int(input("Введите секунды")) # Функция int- возвращает целое число; функция input- ввод данных
if duration < 60: # Если меньше 60, то выводим на печать
    print(duration, "сек.")

elif 60 < duration < 3600:
    min = duration / 60
    sec = duration % 60
    print(int(min), "мин.", int(sec), "сек.")

elif 3600 < duration < 86400:
    hour = duration / 3600
    min = (duration % 3600) // 60
    sec = (duration % 3600) % 60
    print(int(hour), "ч.", int(min), "мин.", int(sec), "сек.")

elif 86400 < duration:
    year = duration / 31449600
    month = (duration % 31449600) // 2419200
    week = ((duration % 31449600) % 2419200) // 604800
    day = (((duration % 31449600) % 2419200) % 604800) // 86400
    hour = ((((duration % 31449600) % 2419200) % 604800) % 86400) // 3600
    min = (((((duration % 31449600) % 2419200) % 604800) % 86400) % 3600) // 60
    sec = (((((duration % 31449600) % 2419200) % 604800) % 86400) % 3600) % 60
    print(int(year), "год/года(лет)", int(month), "месяц(ев)", int(week), "нед.", int(day), "д.", int(hour), "ч.", int(min), "мин.", int(sec), "сек.")
