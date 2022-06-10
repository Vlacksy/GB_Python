import sys

SALES_FILE = 'bakery.csv'

try:
    with open(SALES_FILE, 'r', encoding='utf-8') as f:
        if len(sys.argv) == 1:
            print(f.read().strip())
        elif len(sys.argv) == 2:
            from_row = int(sys.argv[1]) - 1
            content = f.readlines()[from_row:]
            for line in content:
                print(line.strip())
        elif len(sys.argv) == 3:
            from_row = int(sys.argv[1]) - 1
            to_row = int(sys.argv[2])
            content = f.readlines()[from_row:to_row]
            for line in content:
                print(line.strip())

except FileNotFoundError as e:
    print(f'{e}')
