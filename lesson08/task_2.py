import re

FILENAME = 'nginx_logs.txt'
pattern = re.compile(r'^(.+)\s-\s-\s\[(.+)]\s"(\w+)\s(/\w+/\w+).+"\s(\d+)\s(\d+)')
cont = []

try:
    with open(FILENAME, 'r', encoding='utf-8') as f:
        for line in f:
            parsed_raw = pattern.findall(line)
            print(parsed_raw)
            cont.append(parsed_raw)

    # requests_info does not fully fit to the PyCharm window
    # write requests_info to file to see full result in file
    with open('requests_info.txt', 'w', encoding='utf-8') as f:
        for el in cont:
            f.write(f'{el}\n')

except FileNotFoundError as e:
    print(f'{e}')
