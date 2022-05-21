"""Функция принимает список слов и некоторую букву, количество которых находится в списке"""

def count_letter():
    L = input("Введите список слов: ")
    L1 = str(L)
    L1.split()
    letter = input("Введите букву для подсчета: ")
    count = 0
    for i in L1:
        if i == letter:
            count += 1
    print(f"Буква {letter} встречается {count} раз в списке - ' {L} '")

count_letter()



