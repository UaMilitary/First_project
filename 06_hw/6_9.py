"""
Завдання 9/14
Є два рядки у різних кодуваннях - "utf-8" та "utf-16". Нам необхідно зрозуміти, чи дорівнюються рядки між собою.

Реалізуйте функцію is_equal_string(utf8_string, utf16_string), яка повертає True, якщо рядки дорівнюють собі, і False — якщо ні.
"""

def is_equal_string(utf8_string, utf16_string):
    utf8_decode = utf8_string.decode('utf-8')
    utf16_decode = utf16_string.decode('utf-16')
    if utf8_decode == utf16_decode:
        result = True
    else:
        result = False
    return result

string = "Hello"

print(is_equal_string("HE".encode('utf-8'), "HEL".encode('utf-16')))

