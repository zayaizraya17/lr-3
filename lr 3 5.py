# Запрашиваем координаты у пользователя ввод данных с клавиатуры
x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))

# Определяем положение точки и выводим результат
if x == 0 and y == 0:
    print("Точка находится в начале координат.")
elif x == 0:
    print("Точка лежит на оси Y.")
elif y == 0:
    print("Точка лежит на оси X.")
elif x > 0 and y > 0:
    print("Точка находится в первой четверти.")
elif x < 0 and y > 0:
    print("Точка находится во второй четверти.")
elif x < 0 and y < 0:
    print("Точка находится в третьей четверти.")
elif x > 0 and y < 0:
    print("Точка находится в четвертой четверти.")