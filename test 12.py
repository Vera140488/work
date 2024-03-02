# Вывести на экран фигуры, заполненные звездочками.
# Диалог с пользователем реализовать при помощи меню

def print_rectangle():
    width = int(input("Введите ширину прямоугольника: "))
    height = int(input("Введите высоту прямоугольника: "))
    for i in range(height):
        print("*" * width)

def print_triangle():
    size = int(input("Введите высоту треугольника: "))
    for i in range(1, size+1):
        print("*" * i)

while True:
    print("Меню:")
    print("1. Вывести прямоугольник")
    print("2. Вывести треугольник")
    print("3. Выход")
    
    choice = input("Выберите действие (1, 2 или 3): ")
    
    if choice == "1":
        print_rectangle()
    elif choice == "2":
        print_triangle()
    elif choice == "3":
        break
    else:
        print("Пожалуйста, выберите корректное действие.")