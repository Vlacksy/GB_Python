import os
from pathlib import Path
import json

proj_dir = os.path.abspath(os.curdir)
file_name = f'{os.path.split(proj_dir)[1]}_summary.json'
file_size_stat = {}
for root, dirs, files in os.walk(proj_dir):
    for file in files:  # check all files in dir
        file_size = os.stat(Path(f'{root}/{file}')).st_size  # get size of file by full path
        file_type = os.path.splitext(file)[1]
        check_size = 10
        while file_size > check_size:
            check_size *= 10
        if file_size_stat.get(check_size):
            file_size_stat[check_size][0] += 1
            if file_type not in file_size_stat[check_size][1]:
                file_size_stat[check_size][1].append(file_type)
        else:
            file_size_stat[check_size] = [1, [file_type]]

for k, v in file_size_stat.items():
    file_size_stat[k] = tuple(v)

with open(file_name, 'w', encoding='utf-8') as f:
    json.dump(file_size_stat, f, ensure_ascii=False, indent=4)
