"""
Тепер ми потренуємося писати корисні регулярні вирази. Напишіть регулярний вираз для функції find_all_emails, 
яка буде в тексті (параметр text) знаходити всі email та повертати список отриманих з тексту збігів.

З метою спрощення приймемо, що:

ми використовуємо для email, — англійський алфавіт
префікс (все, що знаходиться до символу @) починається з латинської літери та може містити будь-яке число або букву,
 включаючи нижнє підкреслення та символ точки. Має складатися мінімум із двох символів
суфікс email (все, що знаходиться після символу @) складається лише з букв англійського алфавіту, та має дві частини,
 розділені точкою, також доменне ім'я верхнього рівня не може бути менш ніж два символи (все, що після точки)

Даний регулярний вираз жодною мірою не претендує на покриття всіх можливих варіантів email.

При виконанні цього завдання ми рекомендуємо використовувати наступний сервіс для перевірок регулярних виразів regex101.
"""
import re


def find_all_emails(text):
    text = "vbxc xoizihouzeupreu2089@yopmail.com gkj[jq greiquautrevouko3716@yopmail.com dfgsdfg , 12h3@i.ua]"
    result = re.findall(r"[a-zA-Z]{1}[\w\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}", text)
    return print(result)


find_all_emails("")