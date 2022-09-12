# 1.1
# 1) установить Python и PyCharm
# 2) напишите и запустите программу, которая выводит строку "Hello world!"
print("Hello world!")


# 3) напишите программу, которая на входе получает имя пользователя, сохраняет его в переменную user_name
# и выводит строку "Hello {user_name}!"

def user_name_func():
    user_name = input("Введите имя пользователя: ")
    print(f"Hello {user_name}!")


user_name_func()

# 1.2
# 1) Напишите программу, чтобы вывести
#     *********
#     *       *
#     *       *
#     *********
v1 = "*********"
v2 = "*       *"

print(v1)
print(v2)
print(v2)
print(v1)
