import sys
from os import path

users_filename = sys.argv[1]
hobby_filename = sys.argv[2]
users_hobby_filename = sys.argv[3]

if path.isfile(users_filename) and path.isfile(hobby_filename):
    with open(users_filename, 'r', encoding='utf-8') as f:
        users = [line.replace('\n', '') for line in f]

    with open(hobby_filename, 'r', encoding='utf-8') as f:
        hobby = [line.replace('\n', '') for line in f]

    users_hobby = []
    if len(hobby) > len(users):
        print('Process finished with exit code 1')
        sys.exit(1)
    else:
        users_hobby = [f'{users[i]}: {None}\n' if i + 1 > len(hobby) else f'{users[i]}: {hobby[i]}\n' for i in
                       range(len(users))]
        with open(users_hobby_filename, 'w', encoding='utf-8') as f:
            f.writelines(users_hobby)
        with open(users_hobby_filename, 'r', encoding='utf-8') as f:
            users_hobby = [line.replace('\n', '') for line in f]
    print(users_hobby)

elif not path.isfile(users_filename) and path.isfile(hobby_filename):
    print(f'Файл {users_filename} не найден')

elif path.isfile(users_filename) and not path.isfile(hobby_filename):
    print(f'Файл {hobby_filename} не найден')

else:
    print(f'Файлы {users_filename}, {hobby_filename} не найдены')
