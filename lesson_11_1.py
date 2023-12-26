import time
import random
from typing import Callable


def log_to_file(func: Callable):
    def wrapper(*args, **kwargs):
        filename = func.__name__
        log_entry = f"Method {filename} was called with args {args} at {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        result = func(*args, **kwargs)
        log_entry += f"Result: {result}\n"
        with open(f'data/{filename}.txt', 'a') as file:
            file.write(log_entry)

        return result

    return wrapper


@log_to_file
def add(x, y):
    return x + y


@log_to_file
def multiply(x, y):
    return x * y


random_x = random.randint(0, 9)
random_y = random.randint(0, 9)

result_add = add(random_x, random_y)
result_multiply = multiply(random_x, random_y)
