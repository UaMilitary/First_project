"""
У модулі роботи з функціями ми писали функцію get_fullname для складання повного імені користувача. 
Виконаємо невелике продовження для цього завдання та напишемо функцію is_check_name, яка приймає два 
параметри (fullname, first_name) і повертає логічне значення True або False. Це результат перевірки, 
чи є рядок first_name префіксом рядка fullname. Функція is_check_name чутлива до регістру літер, тобто 
"Sam" і "sam" для неї різні імена.
"""

def is_check_name(fullname, first_name):
    print(fullname)
    suf_name = fullname.removeprefix(first_name)
    if fullname == suf_name:
        bool_val = False
    else:
        bool_val = True 
        
    return bool_val



print(is_check_name("Alexandr", "alex"))

