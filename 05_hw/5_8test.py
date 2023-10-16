grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

def formatted_grades(students):
    row_number = 0
    table = []
    for student, grade in students.items():
        score = grades.get(grade, 'not found')
        row_number += 1
        final_str = ("{num:>4}|{name:<10}|{ects:^5}|{grade_num:^5}".format(num=row_number, name=student, ects=grade, grade_num=score))
        table.append(final_str)
    return table

formatted_grades({"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"})