import os

folders = [
    'my_project',
    'my_project/settings',
    'my_project/mainapp',
    'my_project/adminapp',
    'my_project/authapp'
]

cur_dir = os.path.abspath(os.curdir) + '/'

for folder in folders:
    folder = cur_dir + folder
    os.makedirs(folder, exist_ok=True)
