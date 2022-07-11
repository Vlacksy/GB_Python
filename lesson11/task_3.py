class MyError(Exception):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return f'{self.val} is not a digit'


my_list = []
while True:
    num = input('Please enter a number. To stop program please enter Stop ')
    if num == 'Stop':
        break
    try:
        if len(num.split('.')) > 2:  # check for float also
            raise MyError(num)
        for el in num.split('.'):  # check each element after split
            if not el.isdigit():
                raise MyError(num)
    except MyError as e:
        print(e)
    else:
        my_list.append(num)

print(my_list)
