import sys
from os import stat

SALES_FILE = 'bakery.csv'

try:
    sales_sum = sys.argv[1]
    with open(SALES_FILE, 'a', encoding='utf-8') as f:
        if not stat(SALES_FILE).st_size:  # first row
            f.write(sales_sum)
        else:
            f.write('\n')
            f.write(sales_sum)
except IndexError:
    print('Пожалуйста, введите сумму')
