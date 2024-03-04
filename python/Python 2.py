#!/usr/bin/env python3
# Created by Vera Lazareva 2024 

# Пользователь вводит с клавиатурыдва числа. Нужно
# посчитать отдельно сумму четных, нечетных и чисел,
# кратных 9 в указанном диапазоне, а также среднеарифметическое каждой группы

start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

sum_even = 0
count_even = 0

sum_odd = 0
count_odd = 0

sum_multiple_of_9 = 0
count_multiple_of_9 = 0

for i in range(start, end+1):
    if i % 2 == 0:
        sum_even += i
        count_even += 1
    else:
        sum_odd += i
        count_odd += 1
    
    if i % 9 == 0:
        sum_multiple_of_9 += i
        count_multiple_of_9 += 1

if count_even > 0:
    average_even = sum_even / count_even
else:
    average_even = 0

if count_odd > 0:
    average_odd = sum_odd / count_odd
else:
    average_odd = 0

if count_multiple_of_9 > 0:
    average_multiple_of_9 = sum_multiple_of_9 / count_multiple_of_9
else:
    average_multiple_of_9 = 0

print(f"Сумма четных чисел: {sum_even}, Среднее четных чисел: {average_even}")
print(f"Сумма нечетных чисел: {sum_odd}, Среднее нечетных чисел: {average_odd}")
print(f"Сумма чисел, кратных 9: {sum_multiple_of_9}, Среднее чисел, кратных 9: {average_multiple_of_9}")

# # Пользователь вводит с клавиатуры длину линии и
# # символ для заполнения линии. Нужно отобразить на
# # экране вертикальную линию из введенного символа,
# # указанной длины.
# # Например, если было введено 5 и символ %, тогда
# # вывод на экран будет такой:
# # %
# # %
# # %
# # %
# # %

length = int(input("Введите длину линии: "))
symbol = input("Введите символ для заполнения линии: ")

for _ in range(length):
    print(symbol)

  
# Пользователь вводит с клавиатуры числа. Программа должна подсчитывать сумму, максимум и минимум,
# введенных чисел. Когда пользователь вводит число 7
# программа прекращает свою работу и выводит на экран
# надпись «Good bye!»

numbers = []
while True:
    number = int(input("Введите число: "))
    numbers.append(number)

    if number == 7:
        print("Good bye!")
        break

sum_numbers = sum(numbers)
max_number = max(numbers)
min_number = min(numbers)

print(f"Сумма введенных чисел: {sum_numbers}")
print(f"Максимальное число: {max_number}")
print(f"Минимальное число: {min_number}")
