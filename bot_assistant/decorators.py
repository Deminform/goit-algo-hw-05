from functools import wraps
from colorama import Fore, init, Style

init(autoreset=True)


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return e.args[0] if not e.args[0].startswith('not') else Fore.YELLOW + (
                "Enter the argument for the command."
            )
        except KeyError:
            return Fore.YELLOW + "KeyError."
        except IndexError as e:
            return e.args[0] if not e.args[0].startswith('list') else Fore.YELLOW + "Enter the argument for the command"

    return inner
