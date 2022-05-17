HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
exit - выход из программы"""


today = []
tomorrow = []
other = []
tasks = []

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "add" or command == "фвв":
        task = input("Введите название задачи: ")
        date = input("Введите дату выполнения задачи: ")
        if date.lower() == "сегодня":
            today.append(task)
            print(f'Задача {task} \nДобавлена на {date.lower()}')

        elif date.lower() == "завтра":
            tomorrow.append(task)
            print(f'Задача {task} \nДобавлена на {date.lower()}')

        elif date.lower() != ("завтра", "сегодня"):
            other.append(task)
            print(f'Задача {task} добавлена')
    elif command == "show":
        print(f"Задачи на сегодня ",today)
        print(f"Задачи на завтра ",tomorrow)
        print(f"Остальные задачи ",other)
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
    else:
        print("Неизвестная команда")
        break







