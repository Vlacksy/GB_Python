from datetime import datetime


class Date:
    attr = 12

    def __init__(self, date):  # «день-месяц-год».
        self.date = date

    @classmethod
    def date_int(cls, date):
        day, month, year = date.split('-')
        return {'day': int(day), 'month': int(month), 'year': int(year)}

    @staticmethod
    def check_date(date):
        try:
            datetime.strptime(date, "%d-%m-%Y")  # use strptime date to check date
        except ValueError as e:
            return f'Incorrect date: {e}'
        else:
            return 'Date is correct'


date_1 = Date('07-04-2022')
print(date_1.date)
print(date_1.date_int(date_1.date))
print(Date.date_int(date_1.date))
print(date_1.date_int('07-04-2022'))
print(Date.date_int('07-04-2022'))

print(date_1.check_date(date_1.date))
print(Date.check_date(date_1.date))
print(date_1.check_date('07-04-2022'))
print(Date.check_date('07-04-2022'))

# check incorrect date
date_2 = Date('07-13-2022')
print(date_2.check_date(date_2.date))
print(Date.check_date(date_2.date))
print(date_2.check_date('31-06-2022'))
print(Date.check_date('07-13--98'))
