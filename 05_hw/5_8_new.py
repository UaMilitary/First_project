"""
У минулому модулі ми працювали із системою оцінок ECTS. Напишіть функцію formatted_grades, яка приймає на вхід словник
 оцінювання студентів за предмет наступного вигляду:

students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
І повертає список відформатованих рядків, щоб під час виведення наступного коду:

for el in formatted_grades(students):
    print(el)

Виходила наступна таблиця:

   1|Nick      |  A  |  5
   2|Olga      |  B  |  5
   3|Mike      | FX  |  2
   4|Anna      |  C  |  4
перший стовпець — ширина 4 символи, вирівнювання по правому краю
другий стовпець — ширина 10 символів, вирівнювання по лівому краю
третій та четвертий стовпець — ширина 5 символів, вирівнювання по центру
вертикальний символ | не входить у ширину стовпця
"""

grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

def formatted_grades(students):
    count = 1
    list = []
    for key, value in students.items():
        string = "{:>4}|{:<10}|{:^5}|{:^5}".format(count, key, value, grades[value])
        print(string)
        list.append(string)
        count += 1
    return list


formatted_grades({"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"})