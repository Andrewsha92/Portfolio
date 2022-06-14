# # month = input ("Какой сейчас месяц?")
# first_name = input("Введите ваше имя: ")
# last_name = input("Введите вашу фамилию: ")
# age = input("Введите ваш возраст: ")
# city = input("Введите город проживания: ")
# # a = 1
# a = -13
# b = 7
# a = a - b
# # # b = a + b
# s1 = 'foo'
# s2 = 'bar'
# a = 5//2
# print(a)
# # # print(29//3)
# a = 2.2 ** 2
# # print(float(a))
# print(round(11*2.5/3,2))
# pi = 3.14159 * 3.14159
# print (round(pi/2))
# s = "Hello"
# # print(s.upper())
# numbers = input("Введите числа через пробел:")
#
# numbers_split = numbers.split()
# numbers_lines = "\n".join(numbers_split)
#
# # print(numbers_lines)
# age = 29
# my_age  = "I`m %i years old"% (age)
# print(my_age )
#
# a = 'saloma'
# print(a [-4])
# list = ['a', 'b', 'c', 'd', 'e' ]
# list.append('f')
# list.append('g')
# list.append('h')
#
# print(list[::2])
# L = ["а", "б", "в", 1, 2, 3, 4]
# print (L[ 1:-3 ])
#
# L = ["а", "б", "в", 1, 2, 3, 4]
# print (L[0::3])
#
# L = ["а", "б", "в", 1, 2, 3, 4]
# print(L [0:-3])
#
# L = ["а", "б", "в", 1, 2, 3, 4]
# print(L [-1:3:-1])
# #
# l = [3.3, 4.4, 5.5, 6.6]
# print(map(round,l))
# print(list(map(round, l)))
# #
# L = ['3.3', '4.4', '5.5', '6.6']
#
# print (list (map ( float , L)))
# #
# string = input("Введите числа через пробел:")
#
# list_of_strings = string.split() # список строковых представлений чисел
# list_of_numbers = list(map(int, list_of_strings)) # список чисел
#
# print(sum(list_of_numbers[::3])) # sum() вычисляет сумму элементов списка
# L = list(map(float, input().split()))
#
# # # обмениваем первое и последнее число
# # # с помощью множественного присваивания
# # L[0], L[-1] = L[-1], L[0]
# #
# # # находим сумму и добавляем её в конец списка
# # L.append(sum(L))
# #
# # print(L)
# d = {'day' : 22, 'month' : 6, 'year' : 2015}
#
# print("||".join(d.keys()))
# title = input("Введите название книги:")
# author = input("Введите фамилию автора:")
# year = int(input("Введите год издания:"))
#
# book = {'title': title,
#         'author': author,
#         'year': year}
#
# # print(book)
# s = input (str('введите текст: '))
# unique = list(set(s))
# # print(len(unique))
# s = input (str('введите текст: '))
# unique = list(set(s))
# # print(len(unique))
# a = input("Введите первую строку: ")
# # b = input("Введите вторую строку: ")
# #
# a_set, b_set = set(a), set(b) # используем множественное присваивание
#
# a_and_b = a_set.intersection(b_set)
#
# print(a_and_b)
#
# L = [1,5,3,6,2]
# sorted(L)
# # print(L)
# a = input("Введите первую строку: ").split()
#
# b = input("Введите вторую строку: ").split()
#
# a_set, b_set = set(a), set(b)
#
# a_and_b = a_set.symmetric_difference(b_set)
#
# a_and_b = a_and_b.sort()
#
# print(a_and_b)
# L = ['a', 'b', 'c']
# print(id(L))
#
# L.append('d')
# print(id(L))

# a = 1897053880688

# list_1 = ['a', 'b', 'c']
# list_2 = list_1
# list_3 = list(list_1)
# print(list_1)
# print(list_2)
# print(list_3)

#
# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
#
# shopping_center[-1].append("Uniqlo")
#
# print(shopping_center)

#
# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
# print(id(['H&M, Zara'])) # 2205089541312 - проведем сравнение
#
# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
#
# shopping_center[-1].append("Uniqlo")
#
# print (shopping_center)
#
# print(id(['H&M, Zara', 'Uniqlo'])) # результат - разные id
#
# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
# list_id_before = id(shopping_center[-1])
#
# shopping_center[-1].append("Uniqlo")
# # list_id_after = id(shopping_center[-1])
# #
# # print(list_id_before == list_id_after)
#
# a = input("Введите первую строку: ").split()
#
# b = input("Введите вторую строку: ").split()
#
# a_set, b_set = set(a), set(b)
#
# a_and_b = a_set.symmetric_difference(b_set)
#
# c = map(int, a_and_b)
#
# d = list(map(int, c))
#
# d.sort()
#
# print(d)
#
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0} #словарь

money = int(input('Введите сумму вклада '))

a = int((per_cent['ТКБ']) * (money/100))

b = int((per_cent['СКБ']) * (money/100))

c = int((per_cent['ВТБ']) * (money/100))

d = int((per_cent['СБЕР']) * (money/100))

deposit = str(max(a,b,c,d))

print('Максимальная сумма которую вы сможете заработать ' + deposit)














