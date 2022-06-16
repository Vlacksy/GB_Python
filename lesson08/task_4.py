from functools import wraps


def val_checker(val_check):
    def _val_checker(func):
        @wraps(func)
        def wrapper(arg):
            if val_check(arg):
                res = func(arg)
                return res
            else:
                raise ValueError(f'wrong value {arg}')
        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    """Return x^3"""
    return x ** 3


if __name__ == '__main__':
    res_1 = calc_cube(3)
    print(res_1)
    help(calc_cube)  # check wraps
    res_2 = calc_cube(-3)  # check raise
