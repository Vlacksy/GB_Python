class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        total_income = float(self._income['wage']) + float(self._income['bonus'])
        print(f'Доход с учетом премии: {total_income} $')


worker_1 = Position('Johnny ', 'Cage', 'Actor', '70000', '30000')
worker_1.get_full_name()
worker_1.get_total_income()
print(worker_1.name)
print(worker_1.position)
