"""
Попрацюємо трохи зі специфікацією у форматуванні рядків. Напишіть функцію formatted_numbers, яка повертає 
список відформатованих рядків, щоб під час виведення наступного коду:

for el in formatted_numbers():
    print(el)

Виходила наступна таблиця:
| decimal  |   hex    |  binary  |
|0         |    0     |         0|
|1         |    1     |         1|
|2         |    2     |        10|
|3         |    3     |        11|
|4         |    4     |       100|
|5         |    5     |       101|
|6         |    6     |       110|
|7         |    7     |       111|
|8         |    8     |      1000|
|9         |    9     |      1001|
|10        |    a     |      1010|
|11        |    b     |      1011|
|12        |    c     |      1100|
|13        |    d     |      1101|
|14        |    e     |      1110|
|15        |    f     |      1111|

всі стовпці мають ширину 10 символів

у заголовків таблиці вирівнювання по центру
- перший стовпець десяткових чисел — вирівнювання по лівому краю
- другий стовпець шістнадцяткових чисел — вирівнювання по центру
- третій стовпець двійкових чисел — вирівнювання з правого краю
- вертикальний символ | не входить у ширину стовпця

Як ви вже зрозуміли, функція formatted_numbers виводить таблицю чисел від 0 до 15 у десятковому, 
шістнадцятковому та бінарному форматі.
"""
def formatted_numbers():
    list = []
    i = 0
    string = "|{:^10}|{:^10}|{:^10}|".format("decimal", "hex", "binary")
    print(string)
    list.append(string)
    while i <= 15:
        string = "|{:<10}|{:^10}|{:>10}|".format(i, '{:x}'.format(i), '{:b}'.format(i))
        print(string)
        list.append(string)
        i += 1
    return list

formatted_numbers()
