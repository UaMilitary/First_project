"""
Дані про користувачів краще зберігати у форматі бінарних файлів. Тому вам необхідно створити функцію, яка буде записувати логін та пароль користувача у файл.

Реалізуйте функцію save_credentials_users(path, users_info), яка зберігає інформацію про користувачів з паролями в бінарний файл.

Де:

path – шлях до файлу.
users_info - словник типу {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}, де ключ — логін (username) користувача, а значення — його пароль (password).
Вимоги:

Кожен рядок файлу повинен мати такий вигляд username:password. Такий формат запису використовують при Базовій аутентифікації.
Відкрийте файл для запису та збережіть ключ та значення зі словника users_info у вигляді окремого рядка username:password для кожного елемента словника users_info
"""
from pathlib import Path

def save_credentials_users(path, users_info):
    with open(path, 'w') as write_file:
        for keys, value in users_info.items():
            write_file.write(f"{keys}:{value}\n")
    return None



users_dict = {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}
print(save_credentials_users(Path("E:\\Py_Projects\\First_project\\txt_folder\\output_6_10.bin"), users_dict))