from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        res = func(*args)
        types_in = tuple(f'{arg} - тип {type(arg)}' for arg in args)
        type_out = f'Тип значения функции - {type(res)}'
        print(f'{func.__name__}: {types_in}'.replace('"', ''))
        print(type_out)
        return res

    return wrapper


@type_logger
def calc_cube(x, y):
    """Return sum of parameters to the third power"""
    return (x + y) ** 3


if __name__ == '__main__':
    res_1 = calc_cube(1, 2.5)
    print(res_1)
    help(calc_cube)  # check wraps
