duration = int(input('Введите временной интервал: '))

days_count = duration // 86400
hours_count = (duration - days_count * 86400) // 3600
min_count = (duration - days_count * 86400 - hours_count * 3600) // 60
sec_count = duration - days_count * 86400 - hours_count * 3600 - min_count * 60

# Option 1
time = [days_count, 'дн', hours_count, 'час', min_count, 'мин', sec_count, 'сек']

for i in range(0, len(time), 2):
    if time[i]:
        print(time[i], time[i + 1], end=' ')
print('\n')

# Option 2
time_dict = {
    'дн': days_count,
    'час': hours_count,
    'мин': min_count,
    'сек': sec_count
}

for key in time_dict:
    if time_dict[key]:
        print(time_dict[key], key, end=' ')
