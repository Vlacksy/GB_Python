import os
from pathlib import Path
from pprint import pprint

proj_dir = os.path.abspath(os.curdir)
file_size_stat = {}
for root, dirs, files in os.walk(proj_dir):
    for file in files:  # check all files in dir
        file_size = os.stat(Path(f'{root}/{file}')).st_size  # get size of file by full path
        check_size = 10
        while file_size > check_size:
            check_size *= 10
        if file_size_stat.get(check_size):
            file_size_stat[check_size] += 1
        else:
            file_size_stat[check_size] = 1

pprint(file_size_stat)
