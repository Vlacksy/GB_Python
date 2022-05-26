employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
             'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for employee in employees:
    name = employee.split()[-1].lower().capitalize()
    print(f'Привет, {name}!')
