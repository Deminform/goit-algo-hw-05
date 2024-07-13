from functools import wraps
from colorama import Fore, Style


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            raise ValueError(Fore.RED + str(e) + Style.RESET_ALL)
        except FileNotFoundError as e:
            raise FileNotFoundError(Fore.RED + f'File not found {e.filename}' + Style.RESET_ALL)
        except PermissionError as e:
            raise PermissionError(Fore.RED + f'No access to the file {e.filename}' + Style.RESET_ALL)

    return inner
