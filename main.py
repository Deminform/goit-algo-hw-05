from typing import Callable, Counter
import re


def caching_fibonacci():
    """
    Module 5 / Task 1
    """
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci


fib = caching_fibonacci()
# print(fib(10))


def generator_numbers(input_text: str):
    """
    # Module 5 / Task 2
    """
    for line in re.findall(r'\d+.?\d+', input_text):
        yield float(line)


def sum_profit(input_text: str, func: Callable):
    return sum(func(input_text))


text = ("Загальний дохід працівника складається "
        "з декількох частин: 1000.01 як основний дохід, "
        "доповнений додатковими надходженнями 27.45 і 324.00 доларів.")

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")




