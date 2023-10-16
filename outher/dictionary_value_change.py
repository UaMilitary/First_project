"""
Ваша компанія веде блог. Треба реалізувати функцію find_articles для пошуку за статтями цього блогу. 
Є список articles_dict, в якому міститься опис статей блогу. Кожен елемент цього списку є словником 
з наступними ключами: прізвища авторів - ключ 'author', назва статті - ключ 'title', рік видання - ключ 'year'.

Реалізуйте функцію find_articles,

Параметр key функції визначає поєднання букв для пошуку. Наприклад, при key="Python" функція шукає, 
чи є у списку articles_dict статті, у назві чи іменах авторів яких зустрічається це поєднання літер. 
Якщо такі елементи списку були знайдені, треба повернути новий список зі словників, що містять прізвища авторів,
 назву та рік видання всіх таких статей.

Другий ключовий параметр функції letter_case визначає, чи треба враховувати під час пошуку регістр літер. 
За умовчанням він дорівнює False і регістр немає значення тобто пошук в тексті "Python" і "python" це те ж саме.
Інакше потрібно шукати повний збіг.
"""
articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2019,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key):
    b = []
    for dict in articles_dict:
        for key1, value in dict.items():
            if key in str(value):
                ak = dict.keys()
                list_ak = list(ak)
                list_ak.sort()
                B = {}
                for k in list_ak:
                    B[k] = dict[k]
                b.append(B)
                break
    for dict2 in b:
        for i in dict:
            if i == "author":
                name = dict2["author"]
                g = f"{name}"
                k = g[2]
                dict2["author"] = "test"
                
            else:
                dict2["author"] = dict2["author"]

           
    return dict2
   
    

print(find_articles("ocean"))