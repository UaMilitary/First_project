"""
За допомогою функції zip, за аналогією прикладу теорії, створіть словник TRANS для транслітерації.
 Створюйте словник TRANS поза функцією translate

Напишіть функцію translate, яка проводить транслітерацію кириличного алфавіту на латинську.

Функція translate:

приймає на вхід рядок та повертає рядок;
проводить транслітерацію кириличних символів на латиницю;
Приклад виконання:

print(translate("Дмитро Короб"))  # Dmitro Korob
print(translate("Олекса Івасюк"))  # Oleksa Ivasyuk

Примітка: У задачі, при створенні словника TRANS, код TRANS[ord(c.upper())] = l.title() буде вважатися неправильним,
а TRANS[ord(c.upper())] = l.upper() — правильним. Це компроміс, тому що в першому випадку ми враховуємо великі літери,
а в другому — правильно, якщо ім'я буде все великими літерами. Щоб не ускладнювати завдання, прийнято як у 
документах — все ім'я друкується великими.
"""

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

letter_UP_list = []
letter_LOW_list = []
for letter in TRANSLATION:
    letter_UP = letter.upper()
    letter_UP_list.append(letter_UP)
    letter_LOW = letter.lower()
    letter_LOW_list.append(letter_LOW)
TRANSLATION_FIN = letter_LOW_list + letter_UP_list

letter_UP_list_CYR = []
letter_LOW_list_CYR = []
for letter in CYRILLIC_SYMBOLS:
    ord_letter_low = ord(letter)
    ord_letter_up = ord(letter.upper())
    letter_UP_list_CYR.append(ord_letter_low)
    letter_LOW_list_CYR.append(ord_letter_up)
list_letter_ord_cyr = letter_UP_list_CYR + letter_LOW_list_CYR

TRANS.update(zip(list_letter_ord_cyr, TRANSLATION_FIN))


def translate(name):
    text_convert = name.translate(TRANS)
    return text_convert


txt = "Привіт як у Вас справи?"
print(translate(txt))