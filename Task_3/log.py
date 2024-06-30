from colorama import Fore

def log_file(name):
    return f'{Fore.GREEN}{name}{Fore.RESET}'

def log_directory(name):
    return f'{Fore.CYAN}{name}{Fore.RESET}'

def log_arrow(name):
    return f'{Fore.MAGENTA}{name}{Fore.RESET}'