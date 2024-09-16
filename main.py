"""
Лабораторная №2.
Получение навыков работы с операторами преобразования и присваивания, 
условными операторами, операторами цикла, переменными и функциями.
"""

def add(a, b):
    """Функция для сложения двух чисел."""
    return a + b

def subtract(a, b):
    """Функция для вычитания двух чисел."""
    return a - b

def multiply(a, b):
    """Функция для умножения двух чисел."""
    return a * b

def divide(a, b):
    """Функция для деления двух чисел."""
    if b != 0:
        return a / b
    else:
        return "Деление на ноль невозможно"

def is_even(number):
    """Функция для проверки четности числа."""
    return number % 2 == 0


while True:
    num1 = input("Введите первое число: ")
    num2 = input("Введите второе число: ")

    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print("Пожалуйста, вводите только числа.")
        continue

    print(f"{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
    print(f"{num1} / {num2} = {divide(num1, num2)}")

    if is_even(num1):
        print(f"Число {num1} четное.")
    else:
        print(f"Число {num1} нечетное.")

    if is_even(num2):
        print(f"Число {num2} четное.")
    else:
        print(f"Число {num2} нечетное.")

    repeat = input("Хотите выполнить вычисления еще раз? (да/нет): ")
    if repeat.lower() != "да":
        break
