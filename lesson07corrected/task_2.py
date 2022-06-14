import os


def create_obj(obj_path):
    if '.' in obj_path:
        with open(obj_path, 'a', encoding='utf-8') as file:
            file.write('')
    else:
        os.makedirs(obj_path, exist_ok=True)


files_n_folders = {}
objects_path = []
with open('config.yaml', 'r', encoding='utf-8') as f:
    start_index = 0
    cur_dir = os.path.abspath(os.curdir)
    print(cur_dir)

    for line in f:
        obj_dir = cur_dir  # set dir to root folder
        cur_index = line.index('|--')  # get index of object level
        obj_name = line[cur_index + 3:].strip()  # get object name
        files_n_folders[cur_index] = obj_name  # add or replace object to files_n_folders
        for i in range(0, cur_index + 1, 2):  # get full path of object from 0 level (root) to object level
            obj_dir += '/' + files_n_folders[i]
        objects_path.append(obj_dir)


for path in objects_path:
    create_obj(path)
