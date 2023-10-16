"""
Щоб замінити всі підрядки, що відповідають регулярному виразу, можна скористатися функцією sub. Замінимо кольори blue, red, white на слово colour:

p = re.sub(r'(blue|white|red)', 'color', 'blue socks and red shoes')
print(p)  # color socks and color shoes


Напишіть функцію replace_spam_words, яка приймає рядок (параметр text), перевіряє його на вміст 
заборонених слів зі списку (параметр spam_words), та повертає результат рядок, але замість заборонених слів, 
підставлений шаблон з *, причому довжина шаблону дорівнює довжині забороненого слова. Визначити нечутливість 
до регістру стоп-слів.
"""
import re


def replace_spam_words(text, spam_words):
        for i in spam_words:
            nstars = "*"*len(i)
            text = re.sub(i, nstars, text, flags=re.IGNORECASE)
        return text

print(replace_spam_words('PYTHOnist', 'Python'))
    
    
        
    

