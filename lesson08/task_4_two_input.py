from functools import wraps


def val_checker(val_check):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args):
            if val_check(*args):
                res = func(*args)
                return res
            else:
                raise ValueError(f'wrong values: {args}')

        return wrapper

    return _val_checker


@val_checker(lambda x, y: x > 0 and y > 0)
def calc_cube(x, y):
    """Return x*y"""
    return x * y


if __name__ == '__main__':
    res_1 = calc_cube(3, 4)
    print(res_1)
    help(calc_cube)  # check wraps
    res_2 = calc_cube(3, -4)  # check raise
