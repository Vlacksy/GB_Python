from os import stat
FILENAME = 'nginx_logs.txt'
try:
    if stat(FILENAME).st_size:  # check that file is not empty
        requests_count = {}
        with open(FILENAME, 'r', encoding='utf-8') as f:
            for line in f:  # read file by line because size of file can be bigger that size of available RAM
                if line.split()[0] not in requests_count:
                    requests_count[line.split()[0]] = 1
                else:
                    requests_count[line.split()[0]] = requests_count[line.split()[0]] + 1

        sorted_requests = sorted(requests_count, key=requests_count.get)  # sort list to get max count of requests
        print(f'IP адрес спамера: {sorted_requests[-1]}, '
              f'количество отправленных им запросов = {requests_count[sorted_requests[-1]]}')
    else:
        print(f'File {FILENAME} is empty')

except FileNotFoundError as e:
    print(f'{e}')
