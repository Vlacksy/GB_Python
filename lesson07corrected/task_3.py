import os
from pathlib import Path
import shutil

proj_dir = os.path.abspath(os.curdir + '/my_project')
if os.path.exists(proj_dir):
    templates_dir = Path(f'{proj_dir}/templates')

    for root, dirs, files in os.walk(proj_dir):
        if root != templates_dir and dirs == ['templates']:
            shutil.copytree(f'{root}/templates', templates_dir, dirs_exist_ok=True)
else:
    print(f'Каталога {proj_dir} не существует')
