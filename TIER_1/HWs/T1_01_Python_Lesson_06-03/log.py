from colorama import Fore, Style   # fore - colour of letters

def log_info(message: str):        # blue for info messages
    print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} {message}")

def log_warning(message: str):     # yellow for warning messages
    print(f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL} {message}")

def log_error(message: str):       # red for error messages
    print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} {message}")