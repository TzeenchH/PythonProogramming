import timeit
from random import random
from string import punctuation
from time import sleep


def calc_duration(func):
    def decorated(*args, **kwargs):
        start = timeit.default_timer()
        result = func(*args, **kwargs)
        finish = timeit.default_timer() - start
        print(f'elapsed {finish} seconds')
        return result


def suppress_errors(error_list):
    def decorator(func):
        def decorated(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except error_list as error:
                return (f'{error} was suppressed')

        return decorated

    return decorator


def validate_range(min_l: int, max_l: int):
    def decorator(func):
        def decorated(*args, **kwargs):
            result = func(*args, **kwargs)
            if min_l <= result <= max_l:
                return result
            raise ValueError

        return decorated

    return decorator


def validate_length(length: int):
    def decorator(func):
        def decorated(*args, **kwargs):
            result = func(*args, **kwargs)
            if len(result) < length:
                return result
            raise ValueError

        return decorated

    return decorator


def universal_validator(max, min = None):
    def decorator(func):
        def decorated(*args, **kwargs):
            result = func(*args, **kwargs)
            if min is None:
                if len(result) < max:
                    return result
                raise ValueError
            else:
                if min <= result <= max:
                    return result
                raise ValueError
        return decorated
    return decorator


def replace_commas(func):
    def decorated(string: str):
        for ch in punctuation:
            string = string.replace(ch, ' ')
        return func(string)

    return decorated


def upper(string):
    string, res = string.title(), ""
    for word in string.split():
        res += "".join((word[:-1], word[-1].upper(), ' '))
    return res[:-1]


def replace_to_upper(func):
    def decorated(string: str):
        return func(upper(string))

    return decorated


def cache_decorator(func):
    cache = {}

    def decorated(*args, **kwargs):
        key = ''.join(args.__str__(), kwargs.__str__())
        if key not in cache:
            result = func(*args, **kwargs)
            cache[key] = result
            return result
        return cache[key]


# Decorated functions
@calc_duration
def long_executing_task():  # func(*args, **kwargs) ==== long_executing_task
    for index in range(3):
        print(f'Iteration {index}')
        sleep(random())


@suppress_errors((ValueError, KeyError))
def potentially_unsafe_func(key: str):
    print(f'Get data by the key {key}')
    data = {'name': 'test', 'age': 30}
    return data[key]


@validate_range(0, 5)
def sum_of_two(numbers):
    return sum(numbers)


@validate_length(30)
def some_msg(msg: str):
    return f'Message was: {msg}'


@universal_validator(10, 0)
def universal_sum(numbers):
    return sum(numbers)


@universal_validator(30)
def universal_msg(msg: str):
    return f'universal message was: {msg}'


@replace_commas
@replace_to_upper
def process_text(text: str):
    return text.replace(':', ',')


@replace_to_upper
@replace_commas
def another_process(text: str):
    return text.replace(':', ",")


@cache_decorator
def some_func(last_name, first_name, age):
    return f'Hi {last_name} {first_name}, you are {age} years old'
