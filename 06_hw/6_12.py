"""
Функція get_credentials_users із попереднього завдання повертає нам список рядків username:password:

['andry:uyro18890D', 'steve:oppjM13LL9e']
Реалізуйте функцію encode_data_to_base64(data), яка приймає у параметрі data зазначений список, виконує кодування кожної пари username:password у формат Base64 та повертає список із закодованими парами username:password у вигляді:

['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU=']
"""

import base64

def encode_data_to_base64(data):
    coded_list = []
    for i in data:
        b_coded = i.encode("utf-8")
        b64_coded = base64.b64encode(b_coded)
        decode_b_b64 = b64_coded.decode()
        coded_list.append(decode_b_b64)
    return coded_list
    
data_list = ['andry:uyro18890D', 'steve:oppjM13LL9e', 'borys:uyro18890D', 'olga:oppjM13LL9e']
print(encode_data_to_base64(data_list))

