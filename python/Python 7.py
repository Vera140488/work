#!/usr/bin/env python3
# Created by Vera Lazareva 2024 

# Пользователь вводит с клавиатуры число в диапазоне от 1 до 100. Если число кратно 3 (делится на 3 без
# остатка) нужно вывести слово Fizz. Если число кратно 5
# нужно вывести слово Buzz. Если число кратно 3 и 5 нужно
# вывести Fizz Buzz. Если число не кратно не 3 и 5 нужно
# вывести само число.
# Если пользователь ввел значение не в диапазоне от 1
# до 100 требуется вывести сообщение об ошибке.

number = int(input("Введите число от 1 до 100: "))

if number < 1 or number > 100:
    print("Ошибка: число должно быть в диапазоне от 1 до 100")
elif number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)

# Написать программу, которая по выбору пользователя возводит введенное им число в степень от нулевой
# до седьмой включительно.

number = int(input("Введите число: "))
power = int(input("Введите степень (от 0 до 7): "))

if power < 0 or power > 7:
    print("Ошибка: степень должна быть от 0 до 7")
else:
    result = number ** power
    print(f"{number} в степени {power} равно {result}")

# Написать программу подсчета стоимости разговора
# для разных мобильных операторов. Пользователь вводит
# стоимость разговора и выбирает с какого на какой оператор он звонит. Вывести стоимость на экран

# Создаем словарь с тарифами для разных операторов
tariffs = {
    "МТС": {
        "МегаФон": 2,
        "Билайн": 3,
        "Теле2": 4
    },
    "МегаФон": {
        "МТС": 2,
        "Билайн": 2.5,
        "Теле2": 3.5
    },
    "Билайн": {
        "МТС": 3,
        "МегаФон": 2.5,
        "Теле2": 3
    },
    "Теле2": {
        "МТС": 4,
        "МегаФон": 3.5,
        "Билайн": 3
    }
}

cost = float(input("Введите стоимость разговора: "))
operator_from = input("Введите ваш мобильный оператор: ")
operator_to = input("Введите оператор, на который звоните: ")

if operator_from in tariffs and operator_to in tariffs[operator_from]:
    rate = tariffs[operator_from][operator_to]
    total_cost = cost * rate
    print(f"Стоимость разговора с {operator_from} на {operator_to} составит {total_cost}")
else:
    print("Ошибка: такие операторы не поддерживаются")

# # Зарплата менеджера составляет 200$ + процент от продаж, продажи до 500$ — 3%, от 500 до 1000 — 5%, свыше
# # 1000 — 8%. Пользователь вводит с клавиатуры уровень
# # продаж для трех менеджеров. Определить их зарплату,
# # определить лучшего менеджера, начислить ему премию
# # 200$, вывести итоги на экран.

# # Функция для вычисления зарплаты менеджера
def calculate_salary(sales):
    base_salary = 200
    if sales <= 500:
        commission_rate = 0.03
    elif sales <= 1000:
        commission_rate = 0.05
    else:
        commission_rate = 0.08
    total_salary = base_salary + sales * commission_rate
    return total_salary

# Ввод уровня продаж для трех менеджеров
sales_manager1 = float(input("Введите уровень продаж для первого менеджера: "))
sales_manager2 = float(input("Введите уровень продаж для второго менеджера: "))
sales_manager3 = float(input("Введите уровень продаж для третьего менеджера: "))

# Вычисление зарплаты для каждого менеджера
salary_manager1 = calculate_salary(sales_manager1)
salary_manager2 = calculate_salary(sales_manager2)
salary_manager3 = calculate_salary(sales_manager3)

# Определение лучшего менеджера и начисление ему премии
best_manager = max(salary_manager1, salary_manager2, salary_manager3)
if best_manager == salary_manager1:
    salary_manager1 += 200
elif best_manager == salary_manager2:
    salary_manager2 += 200
else:
    salary_manager3 += 200

# Вывод результатов на экран
print(f"Зарплата первого менеджера: {salary_manager1}$")
print(f"Зарплата второго менеджера: {salary_manager2}$")
print(f"Зарплата третьего менеджера: {salary_manager3}$")
