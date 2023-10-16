"""
Нагадаємо, що у 4 модулі ми для кулінарного блогу писали функцію format_ingredients, яка приймала на вхід 
список з інгредієнтами рецепта.

Ми продовжимо працювати в цьому напрямку та створимо функцію, яка шукатиме рецепт у файлі та повертатиме 
знайдений рецепт у вигляді словника певної форми.

У вас є файл, який містить рецепти у вигляді:
60b90c1c13067a15887e1ae1,Herbed Baked Salmon,4 lemons,1 large red onion,2 tablespoons chopped fresh basil
60b90c2413067a15887e1ae2,Lemon Pancakes,2 tablespoons baking powder,1 cup vanilla-flavored almond milk,1 lemon
60b90c2e13067a15887e1ae3,Chicken and Cold Noodles,6 ounces dry Chinese noodles,1 tablespoon sesame oil,3 tablespoons soy
sauce
60b90c3b13067a15887e1ae4,Watermelon Cucumber Salad,1 large seedless watermelon,12 leaves fresh mint,1 cup crumbled
 feta cheese
60b90c4613067a15887e1ae5,State Fair Lemonade,6 lemons,1 cups white sugar,5 cups cold water

Кожен рецепт записаний з нового рядка (не забуваємо під час вирішення завдання про кінець рядка). 
Кожен запис починається з первинного ключа бази даних MongoDB. Далі через кому, йде назва рецепта, а потім 
через кому, йде перелік інгредієнтів рецепта.

Вам необхідно реалізувати функцію, котра буде отримувати інформацію про рецепт у вигляді словника для кожної 
страви що шукається. Створіть функцію get_recipe(path, search_id), яка повертатиме словник для рецепта із 
зазначеним ідентифікатором MongoDB.

Де параметри функції:

path — шлях до файлу.
search_id — первинний ключ MongoDB для пошуку рецепта
Вимоги:

Використовуйте менеджер контексту with для читання з файлу
Якщо рецепта із зазначеним search_id у файлі немає, функція повинна повернути None
Приклад: для файлу, вказаного вище, виклик функції у вигляді

get_recipe("./data/ingredients.csv", "60b90c3b13067a15887e1ae4")
Повинен знайти у файлі рядок 60b90c3b13067a15887e1ae4,Watermelon Cucumber Salad,1 large seedless watermelon,
12 leaves fresh mint,1 cup crumbled feta cheese і повернути результат у вигляді словника такої структури:

{
    "id": "60b90c3b13067a15887e1ae4",
    "name": "Watermelon Cucumber Salad",
    "ingredients": [
        "1 large seedless watermelon",
        "12 leaves fresh mint",
        "1 cup crumbled feta cheese",
    ],
}
"""
from pathlib import Path

def get_recipe(path, search_id):
# -------- визначення пустих списків для заповнення і використання їх вподальшому ----------
    fin_list = [] 
    key_list = ["id", "name", "ingredients"]  
    var_list = []  
    result = None 
# -------- відкриття і зчитування даних з файлу ----------
    with open(path, "r") as virt_file:
        while True:
            dict_el = {}  
            line = virt_file.readline()
            line_strip = line.rstrip()
            var_list = line_strip.split(',')
            if line == "":
                break
# -------- створення словника по 2-м існуючим спискам key_list, var_list для 2-х перших ключів словника
            for i in range(0, len(key_list)):
                dict_el[key_list[i]] = var_list[i]
# -------- створення словника по 2-м існуючим спискам key_list, var_list із списком з інгредієнтами
                if i == (len(key_list)-1):  # тут умова коли ми пройшли перші два елемента ID та назву рецепта і дійшли до 3-го
                    dict_el[key_list[i]] = var_list[i:] #в цій умові вказується, що ключу "ingredients" присвоюється зріз починаючи з першого інгредієнта
# --------  запис створених словників у фінальний список
            fin_list.append(dict_el)
# -------- перевірка на входження search_id і вивід результату якщо він є то вивід відповідного словника, якщо немає то буде раніше визначений None
        for dic in fin_list:
            for key, var in dic.items():
                if var == search_id:
                    result = dic
    return result


print(get_recipe(Path(r"E:\Py_Projects\First_project\txt_folder\dish_recepy.txt"), "60b90c3b13067a15887e1ae41"))  