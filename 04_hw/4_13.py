from pathlib import Path

def parse_folder(path):
    files = []
    folders = []
    for p in path.iterdir():
        if p.is_dir():
            folders.append(p.name)
        elif p.is_file():
            files.append(p.name)
    return files, folders

a = 'E:\Py_Projects'
print(parse_folder(Path(a)))