# Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит
# на экран сумму трёх чисел или произведение трёх чисел.

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

choice = input("Выберите операцию (сумма или произведение): ")

if choice == "сумма":
    result = num1 + num2 + num3
    print(f"Сумма трёх чисел: {result}")
elif choice == "произведение":
    result = num1 * num2 * num3
    print(f"Произведение трёх чисел: {result}")
else:
    print("Некорректный выбор операции. Пожалуйста, выберите 'сумма' или 'произведение'.")

# # Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит
# # на экран максимум из трёх, минимум из трёх или среднеарифметическое трёх чисел

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

choice = input("Выберите операцию (максимум, минимум или среднее): ")

if choice == "максимум":
    result = max(num1, num2, num3)
    print(f"Максимум из трёх чисел: {result}")
elif choice == "минимум":
    result = min(num1, num2, num3)
    print(f"Минимум из трёх чисел: {result}")
elif choice == "среднее":
    result = (num1 + num2 + num3) / 3
    print(f"Среднеарифметическое трёх чисел: {result}")
else:
    print("Некорректный выбор операции. Пожалуйста, выберите 'максимум', 'минимум' или 'среднее'.")

# Пользователь вводит с клавиатуры количество метров. В зависимости от выбора пользователя программа
# переводит метры в мили, дюймы или ярды.

meters = float(input("Введите количество метров: "))
choice = input("Выберите единицу измерения (мили, дюймы или ярды): ")

if choice == "мили":
    miles = meters * 0.000621371
    print(f"{meters} метров равно {miles} миль")
elif choice == "дюймы":
    inches = meters * 39.3701
    print(f"{meters} метров равно {inches} дюймов")
elif choice == "ярды":
    yards = meters * 1.09361
    print(f"{meters} метров равно {yards} ярдов")
else:
    print("Некорректный выбор единицы измерения. Пожалуйста, выберите 'мили', 'дюймы' или 'ярды'.")
