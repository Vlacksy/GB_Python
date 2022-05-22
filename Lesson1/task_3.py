for i in range(100):
    if (i + 1) % 10 == 1 and i + 1 != 11:
        word_declension = 'процент'
    elif (i + 1) % 10 in [2, 3, 4] and i + 1 not in [12, 13, 14]:
        word_declension = 'процента'
    else:
        word_declension = 'процентов'
    print(f'{i + 1} {word_declension}')
