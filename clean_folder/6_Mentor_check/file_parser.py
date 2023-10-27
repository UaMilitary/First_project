
import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
DOC_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
ZIP_ARCHIVES = []
GZ_ARCHIVES = []
TAR_ARCHIVES = []
MY_OTHER = []

REGISTER_EXTENSION = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    'AVI': AVI_VIDEO, 
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'DOC': DOC_DOCUMENTS,
    'DOCX': DOCX_DOCUMENTS,
    'DOC': DOC_DOCUMENTS,
    'TXT': TXT_DOCUMENTS,
    'PDF': PDF_DOCUMENTS,
    'XLSX': XLSX_DOCUMENTS,
    'PPTX': PPTX_DOCUMENTS,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'ZIP': ZIP_ARCHIVES,
    'GZ': GZ_ARCHIVES,
    'TAR': TAR_ARCHIVES,
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(name: str) -> str:
    return Path(name).suffix[1:].upper()  # suffix[1:] -> .jpg -> jpg

def scan(folder: Path):
    for item in folder.iterdir():
        # Робота з папкою
        if item.is_dir():  # перевіряємо чи обєкт папка
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                print(FOLDERS)
                scan(item)
            continue

        # Робота з файлом
        extension = get_extension(item.name)  # беремо розширення файлу
        full_name = folder / item.name  # беремо повний шлях до файлу
        if not extension:
            MY_OTHER.append(full_name)
        else:
            try:
                ext_reg = REGISTER_EXTENSION[extension]
                ext_reg.append(full_name)
                EXTENSIONS.add(extension)
            except KeyError:
                UNKNOWN.add(extension)  # .doc
                MY_OTHER.append(full_name)

if __name__ == "__main__":
    folder_process = sys.argv[1]
    scan(Path(folder_process))
    print(f'images jpeg: {JPEG_IMAGES}')
    print(f'images jpg: {JPG_IMAGES}')
    print(f'images png: {PNG_IMAGES}')
    print(f'images svg: {SVG_IMAGES}')
    print(f'audio mp3: {MP3_AUDIO}')
    print(f'audio ogg: {OGG_AUDIO}')
    print(f'audio wav: {WAV_AUDIO}')
    print(f'audio amr: {AMR_AUDIO}')
    print(f'documents doc: {DOC_DOCUMENTS}')      
    print(f'documents docx: {DOCX_DOCUMENTS}') 
    print(f'documents txt: {TXT_DOCUMENTS}')
    print(f'documents pdf: {PDF_DOCUMENTS}')
    print(f'documents xlsx: {XLSX_DOCUMENTS}')
    print(f'documents pptx: {PPTX_DOCUMENTS}')
    print(f'archives zip: {ZIP_ARCHIVES}')
    print(f'archives gz: {GZ_ARCHIVES}')
    print(f'archives tar: {TAR_ARCHIVES}')
    print(f'video avi: {AVI_VIDEO}')
    print(f'video mp4: {MP4_VIDEO}')
    print(f'video mov: {MOV_VIDEO}')    
    print(f'video mkv: {MKV_VIDEO}')
    print(f'EXTENSIONS: {EXTENSIONS}')
    print(f'UNKNOWN: {UNKNOWN}')



