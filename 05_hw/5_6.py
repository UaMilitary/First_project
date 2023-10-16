"""
Функція is_spam_words приймає рядок (параметр text), перевіряє його на вміст заборонених слів зі списку 
(параметр spam_words), і повертає результат перевірки: True, якщо є хоч одне слово присутнє зі списку, та False, 
якщо в тексті стоп-слів не виявлено.

Слова у параметрі text можуть бути у довільному регістрі, а значить функція is_spam_words, 
при пошуку заборонених слів, регістру незалежна і весь текст має зводитися до нижнього регістру.
Для спрощення, будемо вважати, що в рядку є тільки одне заборонене слово.

Передбачити третій параметр функції space_around, який за замовчуванням дорівнює False.
Він відповідатиме за те, що функція шукатиме окреме слово чи ні. Слово вважати, що стоїть окремо, 
якщо ліворуч від слова знаходиться символ пробілу або воно розташоване на початку тексту, 
а праворуч від слова знаходиться пробіл або символ крапки.

print(is_spam_words("Молох", ["лох"]))  # True
print(is_spam_words("Молох", ["лох"], True))  # False

Тобто у другому випадку слово не окреме і є частиною іншого.

У цьому прикладі функція поверне True в обох випадках.

print(is_spam_words("Ты лох.", ["лох"]))  # True
print(is_spam_words("Ты лох.", ["лох"], True))  # True
"""

def is_spam_words(text, spam_words, space_around=False):
    if space_around == False:
        if str(spam_words[0]).lower() in text:
            spam_id1 = True
        else:
            spam_id1 = False
        return spam_id1
    if space_around == True:
        word_div = text.split(" ", -1)
        for word in word_div:
            word_new = str(word).replace(',', '').replace('.', '').replace('!', '').replace('?', '')
            spam_words_new = str(spam_words[0])
            if word_new.lower() == spam_words_new.lower():
                spam_id = True
                break
            else:
                spam_id = False
        return spam_id


#print(is_spam_words("Текст є частиною нашого навчання, задачі потрібною вирішувати по мірі їх надходження", ["Потрібно"], False))
print(is_spam_words('Ты хорош, но выглядишь как лох.', ['хорош'], True))