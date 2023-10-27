"""
Розробіть функцію sanitize_file(source, output), що переписує у текстовий файл output вміст текстового файлу source, очищений від цифр.

Вимоги:

прочитайте вміст файлу source, використовуючи менеджер контексту with та режим "r".
запишіть новий очищений від цифр вміст файлу output, використовуючи менеджер контексту with та режим "w"
запис нового вмісту файлу output має бути одноразовий і використовувати метод write
"""
from pathlib import Path
import re

def sanitize_file(source, output):
#    rfile_path = source / "source.txt"
    with open(source, "r") as read_file:
        text = ""
        while True:
            line = read_file.readline()
            translate_name = re.sub(r'\d', '', line)
            text += translate_name
            if line == "":
                break
        read_file.close()
    with open(output, "w") as write_file:
        write_file.write(text)
        write_file.close()
    return text

sanitize_file(Path("E:\\Py_Projects\\First_project\\txt_folder\\source.txt"), Path("E:\\Py_Projects\\First_project\\txt_folder\\output.txt"))    
      
        
            
    
    
        
            