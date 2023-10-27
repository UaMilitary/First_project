from pathlib import Path

def save_applicant_data(source, output):
    text = ''
    with open(output, 'w') as write_file:
        for dict in source:
            text_line = ''
            for keys_dict, value in dict.items():
                text_line += f'{value},'
            text += f'{text_line} \n'   #створення рядка з необхідним текстом та + 1н переніс рядка після нього
        text = text.replace('\n','replace_point').replace(', replace_point','\n')  #видалення коми в кінці рядків
        write_file.writelines(text)
        write_file.close()
    return None

list_origin = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

print(save_applicant_data(list_origin, Path("E:\\Py_Projects\\First_project\\txt_folder\\output_6_8.txt")))