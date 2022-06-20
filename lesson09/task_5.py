class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super().draw()
        print(f'запись ручкой: \033[3m{self.title}\033[0m')


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super().draw()
        print(f'запись карандашом: {self.title}')


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super().draw()
        print(f'запись маркером: \033[1m{self.title}\033[0m')


pen_title_1 = Pen('ручка')
pencil_title_1 = Pencil('карандаш')
handle_title_1 = Handle('маркер')

pen_title_1.draw()
pencil_title_1.draw()
handle_title_1.draw()
