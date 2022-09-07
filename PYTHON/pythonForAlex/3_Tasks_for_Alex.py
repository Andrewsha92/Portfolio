# Задача 1. Если введенное число больше 7 вывести привет

digit = int(input('Введите число больше 7: '))


def input_digit(digit):
    if digit > 7:
        print('Привет')
    else:
        print('Введите число больше 7, будьте внимательнее')


input_digit(digit)

# Задача 2. Если введенное имя совпадает с Вячеслав, вывести "Привет, Вячеслав", если нет вывести "Нет такого имени"

name = input('Введите имя Вячеслав: ')


def input_digit(name):
    if name == "Вячеслав":
        print('Привет, Вячеслав')
    while name != "Вячеслав":
        print("Нет такого имени")
        break


input_digit(name)


# Задача 3. На входе есть числовой массив, необходимо вывести элементы кратные 3


def input_digit():
    lower = int(input("Введите нижнюю границу диапазона:"))
    upper = int(input("Введите верхнюю границу диапазона:"))
    n = 3
    for i in range(lower, upper + 1):
        if (i % n == 0):
            print(i)


input_digit()
