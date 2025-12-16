import argparse
import shutil
from pathlib import Path


def copy_tree(path: Path, dest: Path, indent: str = "") -> None:
    try:  
        if path.is_dir():                   # for FOLDERS
            for child in path.iterdir():    # check inside
                copy_tree(child, dest, indent + "    ")         # recursion

        elif path.is_file():                # for FILES
            ext = path.suffix.lower().replace(".", "")          # get extension without dot

            if ext == "":                   # if no extension
                ext = "no_extension"        # folder name for such files

            target_folder = dest / ext      # create destination subfolder by extension
            target_folder.mkdir(parents=True, exist_ok=True)    # create folder if needed

            target_file = target_folder / path.name             # destination file path
            shutil.copy2(path, target_file)                     # copy file

    except PermissionError:                 # exceptions
        print("Permission denied:", path)
    except OSError as e:
        print("OS error:", path, e)


def main() -> None:
    parser = argparse.ArgumentParser()      # create parser
    parser.add_argument("source")           # source folder path
    parser.add_argument("destination", nargs="?", default="dist")  # destination folder (default dist)
    args = parser.parse_args()              # parse arguments

    source = Path(args.source)              # make Path for source
    dest = Path(args.destination)           # make Path for destination

    if not source.exists():                 # check source exists
        print("Source directory does not exist")
        return

    if not source.is_dir():                 # check if source is a folder
        print("Source path is not a directory")
        return

    dest.mkdir(parents=True, exist_ok=True) # create destination folder

    copy_tree(source, dest)                 # start recursion
    print("Task completed")


if __name__ == "__main__":
    main() 