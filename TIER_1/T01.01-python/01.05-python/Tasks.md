- PATH
from pathlib import Path

Понять является ли объект папкой или файлом:

from pathlib import Path
def parse_folder(path):
    for el in path.iterdir():
        parse_folder(el)
    else:
        print(f"This is file: {el}")

parse_folder(Path("."))



Отсортировать все файлы из одной папки и посохранять каждый формат в отдельную папку:

from pathlib import Path
import shutil

source = Path("picture")
print(type(source))  
output = Path("sorted")

def copy_file(file: Path):
    ext = file.suffix # get file ext
    ext_folder = output / ext # create path in sorted
    ext_folder.mkdir(exist_ok=True, parents=True) # create actual folder for this path
    shutil.copyfile(file, ext_folder / file.name) # copy filefrom sorted to the source/.<ext>/<filename>

def parse_folder(path):
    for el in path.iterdir():
        if el.is_dir():
            parse_folder(el)
        else:
            copy_file(el)

parse_folder(source)





