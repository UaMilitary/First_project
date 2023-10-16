"""
У попередній задачі ми записали співробітників у файл у такому вигляді:

Robert Stivenson,28
Alex Denver,30
Drake Mikelsson,19
Виконаємо тепер зворотнє завдання і створимо функцію read_employees_from_file(path), яка читатиме дані з
 файлу та повертатиме список співробітників у вигляді:

['Robert Stivenson,28', 'Alex Denver,30', 'Drake Mikelsson,19']
Пам'ятайте про наявність символу кінця рядка \n під час читання даних із файлу. Його необхідно прибирати при
 додаванні прочитаного рядка до списку.

Вимоги:
прочитайте вміст файлу за допомогою режиму "r".
ми поки що не використовуємо менеджер контексту with
поверніть із функції список співробітників із файлу
"""
from pathlib import Path
def read_employees_from_file(path):
    virt_file = open(path, 'r')
    list = []
    for line in virt_file:
        list.append(line.rstrip())
    virt_file.close()
    return list

print(read_employees_from_file(Path(r"E:\Py_Projects\First_project\txt_folder\salery.txt")))  

""" ---- ver-2 ------
def read_employees_from_file(path):
    virt_file = open(path, 'r')
    lines = virt_file.readlines()
    list = []
    for line in lines:
        list.append(line.rstrip())
    virt_file.close()
    return list (edited) 
"""