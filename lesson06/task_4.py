from sys import exit
from os import path

USERS_FILENAME = 'users.csv'
HOBBY_FILENAME = 'hobby.csv'
USERS_HOBBY_FILENAME = 'users_hobby.txt'

if path.isfile(USERS_FILENAME) and path.isfile(HOBBY_FILENAME):
    with open(USERS_FILENAME, 'r', encoding='utf-8') as f:
        users = [line.replace('\n', '') for line in f]

    with open(HOBBY_FILENAME, 'r', encoding='utf-8') as f:
        hobby = [line.replace('\n', '') for line in f]

    users_hobby = []
    if len(hobby) > len(users):
        exit(1)
    else:
        users_hobby = [f'{users[i]}: {None}\n' if i + 1 > len(hobby) else f'{users[i]}: {hobby[i]}\n' for i in
                       range(len(users))]
        with open(USERS_HOBBY_FILENAME, 'w', encoding='utf-8') as f:
            f.writelines(users_hobby)
        with open(USERS_HOBBY_FILENAME, 'r', encoding='utf-8') as f:
            users_hobby = [line.replace('\n', '') for line in f]

    print(users_hobby)

elif not path.isfile(USERS_FILENAME) and path.isfile(HOBBY_FILENAME):
    print(f'Файл {USERS_FILENAME} не найден')

elif path.isfile(USERS_FILENAME) and not path.isfile(HOBBY_FILENAME):
    print(f'Файл {HOBBY_FILENAME} не найден')

else:
    print(f'Файлы {USERS_FILENAME}, {HOBBY_FILENAME} не найдены')
