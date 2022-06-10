from sys import exit
from os import path
import json

USERS_FILENAME = 'users.csv'
HOBBY_FILENAME = 'hobby.csv'
USERS_HOBBY_FILENAME = 'users_hobby.json'

if path.isfile(USERS_FILENAME) and path.isfile(HOBBY_FILENAME):
    with open(USERS_FILENAME, 'r', encoding='utf-8') as f:
        users = f.read().replace(',', ' ').split('\n')

    with open(HOBBY_FILENAME, 'r', encoding='utf-8') as f:
        hobby = f.read().split('\n')

    users_hobby = {}
    if len(hobby) > len(users):
        exit(1)
    else:
        users_hobby = {users[i]: None if i + 1 > len(hobby) else hobby[i] for i in range(len(users))}
        with open(USERS_HOBBY_FILENAME, 'w', encoding='utf-8') as f:
            json.dump(users_hobby, f, ensure_ascii=False, indent=4)

        with open(USERS_HOBBY_FILENAME, 'r', encoding='utf-8') as f:
            users_hobby_json = json.load(f)
    print(users_hobby_json)

elif not path.isfile(USERS_FILENAME) and path.isfile(HOBBY_FILENAME):
    print(f'Файл {USERS_FILENAME} не найден')

elif path.isfile(USERS_FILENAME) and not path.isfile(HOBBY_FILENAME):
    print(f'Файл {HOBBY_FILENAME} не найден')

else:
    print(f'Файлы {USERS_FILENAME}, {HOBBY_FILENAME} не найдены')
