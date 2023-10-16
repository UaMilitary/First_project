"""
Реалізуйте функцію add_employee_to_file(record, path), яка у файл (параметр path - шлях до файлу) буде додавати 
співробітника (параметр record) у вигляді рядка "Drake Mikelsson,19".

Вимоги:
параметр record - співробітник у вигляді рядка виду "Drake Mikelsson,19"
кожен запис у файл має починатися з нового рядка.
необхідно щоб стара інформація у файлі теж зберігалася, тому при роботі з файлом відкрийте файл у режимі 'a',
 додайте співробітника record у файл і закрийте його
ми поки що не використовуємо менеджер контексту with
"""

from pathlib import Path
new_employee = "Drake Mikelsson,19"

def add_employee_to_file(record, path):
    virt_file = open(path, 'a')
    virt_file.write(f"{record}\n")
    virt_file.close()
    return list

print(add_employee_to_file(new_employee, Path(r"E:\Py_Projects\First_project\txt_folder\salery.txt")))   