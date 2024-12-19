# Запрашиваем у пользователя ввод дня, месяца и года
day = int(input("Введите день (число): "))
month = int(input("Введите месяц (число): "))

# Проверка на отрицательный день или месяц
if day < 1 or month < 1 or month > 12:
    print("Некорректный ввод даты.")
else:
    # Определяем количество дней в месяце
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Проверка на корректность дня
if day > days_in_month[month - 1]:
        print("Некорректный ввод даты.")
else:
        # Проверяем, к какому времени года относится введенная дата
        if (month == 3 and day >= 1) or (month in [4, 5]) or (month == 6 and day < 1):
            season = "Весна"
        elif (month == 6 and day >= 1) or (month in [7, 8]) or (month == 9 and day < 1):
            season = "Лето"
        elif (month == 9 and day >= 1) or (month in [10, 11]) or (month == 12 and day < 1):
            season = "Осень"
        else:
            season = "Зима"

     
print(f"Дата {day}.{month}. относится к сезону: {season}")