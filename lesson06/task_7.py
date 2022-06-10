import sys

SALES_FILE = 'bakery.csv'

try:
    with open(SALES_FILE, 'r+', encoding='utf-8') as f:
        row = int(sys.argv[1]) - 1
        sales_sum = sys.argv[2]
        lines_count = sum(1 for line in f)
        if row + 1 > lines_count:
            print(
                f'Количество строк в файле = {lines_count}. Ввденный номер записи {row + 1} превышает количество строк')
        else:
            f.seek(0)  # move cursor to beginning of file after lines count
            if row + 1 == lines_count:  # last row
                content = [f'{sales_sum}' if index == row else line for index, line in enumerate(f)]
            else:
                content = [f'{sales_sum}\n' if index == row else line for index, line in enumerate(f)]
            f.seek(0)
            f.writelines(content)

except FileNotFoundError as e:
    print(f'{e}')
except IndexError:
    print('Пожалуйста, введите номер записи и сумму')
