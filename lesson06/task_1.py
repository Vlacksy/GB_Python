from pprint import pprint
try:
    with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
        requests_info = [(line.split()[0], line.split()[5][1:], line.split()[6]) for line in f]
        pprint(requests_info)
        # requests_info does not fully fit to the PyCharm window
        # write requests_info to file to see full result in file
        with open('requests_info.txt', 'w', encoding='utf-8') as f2:
            for el in requests_info:
                print(el, file=f2)
except FileNotFoundError as e:
    print(f'{e}')
