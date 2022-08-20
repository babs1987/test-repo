import math
from random import randint

"""
1.Преобразвует вывод функции к строке
"""


def to_string(func) -> str:
    def decorator(*args, **kwargs):
        return str(func(*args, **kwargs))
    return decorator


"""
2.Замалчивает все ошибки
"""


def shut_up_exceptions(func):
    def decorator(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            return "молчим"

    return decorator


"""
3.рандомим вывод None
"""


def random_none(probability: float):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not 0.0 <= probability <= 1.0:
                raise ValueError
            s = randint(0, 101)
            if s <= 100-(100 * probability):
                return func(*args, **kwargs)
            else:
                return None

        return wrapper

    return decorator


@shut_up_exceptions
@random_none(0)
@to_string
def fun(i: int):
    return i * i


"""
баловство - таблица брадиса с декоратором который выводит исходные данные(головку и боковик)
"""


def make_grad_min_decor(func):
    def decorator(*args, **kwargs):
        return "   " + "".join([str(f"{i:7d}\'") for i in range(0, 66, 6)]) + "\n" + func(1)

    return decorator


for i in range(25):
    print(fun(5))


@make_grad_min_decor
def bradis(tab=None):
    return "\n".join(list(map(lambda i, j: str(f"{j} ") + "  ".join(
        list(map(lambda a: f"{(math.sin(math.radians(i + a / 60))):.4f}", [a for a in range(0, 66, 6)]))),
                              [i for i in range(0, 86, 5)],
                              [(lambda j: f"{j:2d}\N{DEGREE SIGN}" if tab is not None else " ")(j) for j in
                               range(0, 91, 5)])))

print(bradis())
def func(a):
    return a*2