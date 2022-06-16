from functools import wraps


def type_logger_named(func):
    """logger for named parameters"""

    @wraps(func)
    def wrapper(x, y):
        res = func(x, y)
        types_in = f'(x = {x} - тип {type(x)}, y = {y} - тип {type(y)})'
        type_out = f'Тип значения функции - {type(res)}'
        print(f'{func.__name__}: {types_in}')
        print(type_out)
        return res

    return wrapper


@type_logger_named
def calc_cube(x, y):
    """Return sum of parameters to the third power"""
    return (x + y) ** 3


if __name__ == '__main__':
    res_1 = calc_cube(y=1, x=2.5)
    print(res_1)
    help(calc_cube)  # check wraps
