class MyError(Exception):
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __str__(self):
        return f'{self.num_1}/{self.num_2}: Zero Division'


def my_div(num_1, num_2):
    try:
        if num_2 == 0:
            raise MyError(num_1, num_2)
        else:
            res = num_1 / num_2
    except MyError as e:
        return e
    else:
        return res


a, b, c = 5, 0, 10

print(my_div(a, b))
print(my_div(a, c))
