from pathlib import Path
#
def save_applicant_data(source, output):
    with open(output, "w") as f: 
        for applicant in source: 
            f.write( 
            f"{applicant.get('name')},{applicant.get('specialty')},{applicant.get('math')},{applicant.get('lang')},{applicant.get('eng')}\n" 
            )
    return None
#
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

print(save_applicant_data(list_origin, Path("E:\\Py_Projects\\First_project\\txt_folder\\output_6_8new.txt")))