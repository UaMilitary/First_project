"""
Реалізуйте функцію get_credentials_users(path), яка повертає список рядків із бінарного файлу, створеного в попередньому завданню, де:

path – шлях до файлу.
Формат файлу:
andry:uyro18890D
steve:oppjM13LL9e

Відкрийте файл для читання, використовуючи with та режим rb. Сформуйте список рядків із файлу та поверніть його з функції get_credentials_users у наступному форматі:

['andry:uyro18890D', 'steve:oppjM13LL9e']
Вимоги:

Використовуйте менеджер контексту для читання з файлу
"""
from pathlib import Path

def get_credentials_users(path):
    inf_list = []
    with open(path, "rb") as read_file:
        r_text = read_file.readlines()
        for i in r_text:
            elem_decode = i.decode()  # декодування отриманого елемента 
            dell_line_break = elem_decode.replace('\n', '')  # видалення знаку перенесення рядка
            inf_list.append(dell_line_break)  # доповнення пустого списку відформатованими елементами
    return inf_list

print(get_credentials_users(Path("E:\\Py_Projects\\First_project\\txt_folder\\output_6_10.bin")))