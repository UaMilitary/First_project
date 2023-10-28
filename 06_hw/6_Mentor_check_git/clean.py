"""
Завдання
У багатьох на робочому столі є папка, яка називається якось ніби "Розібрати". Як правило, розібрати цю папку руки ніколи так і не доходять.

Ми з вами напишемо скрипт, який розбере цю папку. Зрештою ви зможете настроїти цю програму під себе і вона виконуватиме індивідуальний сценарій, що відповідає вашим потребам. Для цього наш додаток буде перевіряти розширення файлу (останні символи у імені файлу, як правило, після крапки) і, залежно від розширення, приймати рішення, до якої категорії віднести цей файл.

Скрипт приймає один аргумент при запуску — це ім'я папки, в якій він буде проводити сортування. Допустимо файл з програмою називається sort.py, тоді, щоб відсортувати папку /user/Desktop/Мотлох, треба запустити скрипт командою python sort.py /user/Desktop/Мотлох

Для того щоб успішно впорається з цим завданням, ви повинні винести логіку обробки папки в окрему функцію.
Щоб скрипт міг пройти на будь-яку глибину вкладеності, функція обробки папок повинна рекурсивно викликати сама себе, коли їй зустрічаються вкладенні папки.
Скрипт повинен проходити по вказаній під час виклику папці та сортирувати всі файли по групам:

зображення ('JPEG', 'PNG', 'JPG', 'SVG');
відео файли ('AVI', 'MP4', 'MOV', 'MKV');
документи ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
музика ('MP3', 'OGG', 'WAV', 'AMR');
архіви ('ZIP', 'GZ', 'TAR');
невідомі розширення.

Ви можете розширити та доповнити цей список, якщо хочете.

В результатах роботи повинні бути:
1. Список файлів в кожній категорії (музика, відео, фото и ін.)
2. Перелік усіх відомих скрипту розширень, які зустрічаються в цільовій папці.
3. Перелік всіх розширень, які скрипту невідомі.
4. Після необхідно додати функції, які будуть відповідати за обробку кожного типу файлів.
5. Всі файли та папки треба перейменувати, видалив із назви всі символи, що призводять до проблем. Для цього треба застосувати до імен файлів функцію normalize. Слід розуміти, що перейменувати файли треба так, щоб не змінити розширень файлів.

Функція normalize:
1) Проводить транслітерацію кирилічного алфавіту на латинський.
2) Замінює всі символи крім латинських літер, цифр на '_'.

Вимоги до функції normalize:
- приймає на вхід рядок та повертає рядок;
- проводить транслітерацію кирилічних символів на латиницю;
- замінює всі символи, крім літер латинського алфавіту та цифр, на символ '_';
- транслітерація може не відповідати стандарту, але бути читабельною;
- великі літери залишаються великими, а маленькі — маленькими після транслітерації.

Умови для обробки:
- зображення переносимо до папки images
- документи переносимо до папки documents
- аудіо файли переносимо до audio
- відео файли до video
- архіви розпаковуються та їх вміст переноситься до папки archives

Критерії прийому завдання
1. - всі файли та папки перейменовуються за допомогою функції normalize.
2. - розширення файлів не змінюється після перейменування.
3. - порожні папки видаляються
4. - скрипт ігнорує папки archives, video, audio, documents, images;
5. - розпакований вміст архіву переноситься до папки archives у підпапку, названу так само, як і архів, але без розширення у кінці;
6. - файли, розширення яких невідомі, залишаються без зміни.
"""

from pathlib import Path
import shutil
import sys
import file_parser
from normalize import normalize
#
#
# створення папки в яку будуть переміщуватись наші файли із зміненими ім'ями
def handle_media(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    file_name.replace(target_folder / normalize(file_name.name))

#
def handle_video(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True) 
    file_name.replace(target_folder / normalize(file_name.name))
    
#
def handle_audio(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True) 
    file_name.replace(target_folder / normalize(file_name.name))
    
#
def handle_documents(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True) 
    file_name.replace(target_folder / normalize(file_name.name))

#
def handle_outher(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True) 
    file_name.replace(target_folder / file_name.name)

#
def handle_archive(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / file_name.name.replace(file_name.suffix, '')
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(file_name), str(folder_for_file))
    except shutil.ReadError:
        folder_for_file.rmdir()
        return
    file_name.unlink()
#
# функція яка проходить/передивляється по усіх файлах і пакує їх по вказаних нами папках
def main(folder: Path):
    file_parser.scan(folder)
# images
    for file in file_parser.JPEG_IMAGES:
        handle_media(file, folder / 'images' / 'JPEG')
    for file in file_parser.JPG_IMAGES:
        handle_media(file, folder / 'images' / 'JPG')
    for file in file_parser.PNG_IMAGES:
        handle_media(file, folder / 'images' / 'PNG')
    for file in file_parser.SVG_IMAGES:
        handle_media(file, folder / 'images' / 'SVG')
# audio
    for file in file_parser.MP3_AUDIO:
        handle_audio(file, folder / 'audio' / 'MP3')
    for file in file_parser.OGG_AUDIO:
        handle_audio(file, folder / 'audio' / 'OGG') 
    for file in file_parser.WAV_AUDIO:
        handle_audio(file, folder / 'audio' / 'WAV')  
    for file in file_parser.AMR_AUDIO:
        handle_audio(file, folder / 'audio' / 'AMR')
# video
    for file in file_parser.AVI_VIDEO:
        handle_video(file, folder / 'video' / 'AVI')
    for file in file_parser.MP4_VIDEO:
        handle_video(file, folder / 'video' / 'MP4')
    for file in file_parser.MOV_VIDEO:
        handle_video(file, folder / 'video' / 'MOV')
    for file in file_parser.MKV_VIDEO:
        handle_video(file, folder / 'video' / 'MKV')
# documents
    for file in file_parser.DOC_DOCUMENTS:
        handle_documents(file, folder / 'documents' / 'DOC')
    for file in file_parser.DOCX_DOCUMENTS:
        handle_documents(file, folder / 'documents' / 'DOCX')
    for file in file_parser.TXT_DOCUMENTS:
        handle_documents(file, folder / 'documents' / 'TXT')
    for file in file_parser.PDF_DOCUMENTS:
        handle_documents(file, folder / 'documents' / 'PDF')
    for file in file_parser.XLSX_DOCUMENTS:
        handle_documents(file, folder / 'documents' / 'XLSX')
    for file in file_parser.PPTX_DOCUMENTS:
        handle_documents(file, folder / 'documents' / 'PPTX')
# archives
    for file in file_parser.ZIP_ARCHIVES:
        handle_archive(file, folder / 'archives' )
    for file in file_parser.TAR_ARCHIVES:
        handle_archive(file, folder / 'archives' )
    for file in file_parser.GZ_ARCHIVES:
        handle_archive(file, folder / 'archives' )
# other
    for file in file_parser.MY_OTHER:
        handle_outher(file, folder / 'MY_OTHER')
#
# видалення пустих папок
    for folder in file_parser.FOLDERS[::-1]:
        # Видаляємо пусті папки після сортування
        try:
            folder.rmdir()
        except OSError:
            print(f'Error during remove folder {folder}')
#
#
if __name__ == "__main__":
    folder_process = Path(sys.argv[1])
    main(folder_process.resolve())
