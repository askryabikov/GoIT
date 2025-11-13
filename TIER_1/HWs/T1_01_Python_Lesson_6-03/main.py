# Usage:
#   python main.py <path-to-directory>   -> show directory tree (main task)
#   python main.py test                  -> show color log examples

import sys
from pathlib import Path   # built-in module to work with file system
from colorama import init, Fore, Style   # colorama loaded in virtual environment
from log import log_info, log_warning, log_error  # additional colored logs

init(autoreset=True)   # for colorama on Windows / resets color at the end of line

def handle_file(file: Path, prefix: str, is_last: bool):
    branch = "┗ " if is_last else "┣ "   # visualize middle and last branches
    print(prefix + branch + Fore.GREEN + file.name + Style.RESET_ALL)


def parse_folder(path: Path, prefix: str = ""):
    items = sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
    # get all items inside folder

    total = len(items)   # Counter to find last branch
    for idx, el in enumerate(items):
        is_last = (idx == total - 1)
        branch = "┗ " if is_last else "┣ "   # visualize last and middle branches

        if el.is_dir():   # cyan for directories
            print(prefix + branch + Fore.CYAN + el.name + Style.RESET_ALL)
            child_prefix = prefix + ("  " if is_last else "┃ ")
            parse_folder(el, child_prefix)    # recursion for subfolder
        else:
            handle_file(el, prefix, is_last)   # for file


def run_test_demo():   # Prints colorama test message
    print("\n--- DEMO: color log messages ---")
    log_info("This is an info message example.")
    log_warning("This is a warning example.")
    log_error("This is an error example.")
    print("\n--- END OF DEMO ---\n")

    print(Fore.CYAN + "Available commands:" + Style.RESET_ALL)   # Prints again available commands
    print(Fore.YELLOW + "  python main.py <path-to-directory>" + Style.RESET_ALL + "  - show directory tree")
    print(Fore.YELLOW + "  python main.py test" + Style.RESET_ALL + "                 - show color log examples")
    print()


def main():   # to run test if activated
    if len(sys.argv) == 2 and sys.argv[1].lower() == "test":
        run_test_demo()
        return

    if len(sys.argv) < 2:  # path must be typed in to run the program acc/to Home task
        log_warning("Usage: python main.py <path-to-directory> or python main.py test")
        sys.exit(1)

    source = Path(sys.argv[1])    # read path from command line

    if not source.exists():   # Error in case path does not exist
        log_error(f"Path does not exist: {source}")
        sys.exit(1)

    if not source.is_dir():   # Error in case path is not a folder
        log_error(f"{source} is not a directory.")
        sys.exit(1)

    log_info(f"Starting scan of '{source}'")   # main work: print directory tree
    print(Fore.MAGENTA + f"📦 {source.name}" + Style.RESET_ALL)
    parse_folder(source)
    log_info("Done.")

if __name__ == "__main__":
    main()