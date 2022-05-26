initial_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

init_count = int(len(initial_list))  # get len of init list
i = 0

while i < init_count:
    if initial_list[i].isdigit():  # check if element is digit
        initial_list[i] = f'{int(initial_list[i]):02d}'  # format digit
        initial_list.insert(i + 1, '"')  # add " after
        initial_list.insert(i, '"')  # add " before
        init_count += 2  # increase len of init list
        i += 3
    elif any(map(str.isdigit, initial_list[i])):  # check if element contains digit
        for j in range(len(initial_list[i])):  # check symbols of elements
            if initial_list[i][j].isdigit():  # check if symbols is digit
                initial_list[i] = initial_list[i][:j] + f'{int(initial_list[i][j:]):02d}'  # format digit in element
                initial_list.insert(i + 1, '"')  # add " after
                initial_list.insert(i, '"')  # add " before
                init_count += 2  # increase len of init list
                i += 3
                break
    else:
        i += 1

init_count = int(len(initial_list))  # get len of list after adding of "
i = 0
finish_list = []  # create new list

while i < init_count:
    if initial_list[i] == '"':
        finish_list.append(''.join(initial_list[i:i + 3]))
        i += 3
    else:
        finish_list.append(initial_list[i])
        i += 1

print(initial_list)
print(' '.join(finish_list))
