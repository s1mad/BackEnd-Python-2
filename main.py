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

def check_conditions(first_number, second_number):
    """Пример работы с условными операторами or, and, not, и вложенными if."""
    if first_number > 0 and second_number > 0:
        print("Оба числа положительные.")
        if first_number > 100 and second_number > 100:
            print("Оба числа больше 100.")
        else:
            if first_number > 100:
                print(f"Число {first_number} больше 100.")
            if second_number > 100:
                print(f"Число {second_number} больше 100.")
    elif first_number < 0 or second_number < 0:
        print("Хотя бы одно из чисел отрицательное.")
        if first_number < 0:
            if first_number < -100:
                print(f"Число {first_number} очень маленькое (меньше -100).")
            else:
                print(f"Число {first_number} отрицательное, но больше -100.")
        if second_number < 0:
            if second_number < -100:
                print(f"Число {second_number} очень маленькое (меньше -100).")
            else:
                print(f"Число {second_number} отрицательное, но больше -100.")
    if not is_even(first_number):
        print(f"Число {first_number} нечетное (используем not).")
    else:
        print(f"Число {first_number} четное (используем not).")

def calculate_with_choice(first_number, second_number, selected_operation: str):
    """Пример работы с конструкцией match-case."""
    match selected_operation:
        case "сложение":
            return f"Результат: {add(first_number, second_number)}"
        case "вычитание":
            return f"Результат: {subtract(first_number, second_number)}"
        case "умножение":
            return f"Результат: {multiply(first_number, second_number)}"
        case "деление":
            return f"Результат: {divide(first_number, second_number)}"
        case _:
            return "Неизвестная операция"


if __name__ == "__main__":
    while True:
        num_list = []
        for _ in range(2):
            num = input("Введите число: ")
            try:
                num = int(num)
                num_list.append(num)
            except ValueError:
                print("Пожалуйста, вводите только числа.")
                break

        number_1, num2 = num_list[0], num_list[1]

        # Запрос на выбор операции
        print("Выберите операцию: сложение, вычитание, умножение, деление")
        operation = input("Введите операцию: ").strip().lower()

        # Использование match-case
        result = calculate_with_choice(number_1, num2, operation)
        print(result)

        # Проверка условий
        check_conditions(number_1, num2)

        # Пример цикла в цикле: выводим таблицу умножения для каждого числа
        for i in range(1, 6):
            for num in num_list:
                print(f"{num} * {i} = {num * i}")
            print()  # Разделение строк для удобства

        # Спрашиваем, нужно ли повторить
        repeat = input("Хотите выполнить вычисления еще раз? (да/нет): ")
        if repeat.lower() != "да":
            break
