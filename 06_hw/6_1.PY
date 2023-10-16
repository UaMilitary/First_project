"""
Нехай ми маємо текстовий файл, який містить дані з місячною заробітною платою по кожному розробнику компанії.

Приклад файлу:

Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
Як бачимо, структура файлу – це прізвище розробника та значення його заробітної плати, розділеної комою.

Розробіть функцію total_salary(path) (параметр path - шлях до файлу), яка буде розбирати текстовий файл і 
повертати загальну суму заробітної плати всіх розробників компанії.

Вимоги до завдання:

функція total_salary повертає значення типу float
для читання файлу функція total_salary використовує лише метод readline
ми поки що не використовуємо менеджер контексту with
"""
from pathlib import Path
import re

def total_salary(path):
    file_name = path / "salery.txt"
    text_file = open(file_name, 'r')
    line = text_file.readline()
    a = line
    while line != "":
        line = text_file.readline()
        a += line
    text_file.close()
    nums = re.findall(r'\d+', a)
    sum = 0
    for i in nums:
        sum += float(i) 
    return sum

print(total_salary(Path(r"E:\Py_Projects\First_project\txt_folder")))
    
        