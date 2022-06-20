def slow_down_msg(name, speed, max_allowed_speed):
    msg = f'Current speed of {name} is equal to {speed}. ' \
          f'Maximum allowed speed is equal to {max_allowed_speed}.\n' \
          f'Please slow down.'
    return msg


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Car {self.name} is going')

    def stop(self):
        print(f'Car {self.name} is stopped')

    def turn(self, direction):
        print(f'Car {self.name} turns {direction}')

    def show_speed(self):
        print(f'Current speeed of {self.name} is equal to {self.speed}')


class TownCar(Car):
    max_allowed_speed = 60

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > self.max_allowed_speed:
            print(slow_down_msg(self.name, self.speed, self.max_allowed_speed))
        else:
            car.show_speed()


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    max_allowed_speed = 40

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > self.max_allowed_speed:
            print(slow_down_msg(self.name, self.speed, self.max_allowed_speed))
        else:
            car.show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


town_car_1 = TownCar(50, 'blue', 'Ford')
sport_car_1 = SportCar(120, 'red', 'Ferrari')
work_car_1 = WorkCar(30, 'brown', 'Volvo')
police_car_1 = PoliceCar(60, 'white', 'Chevrolet', True)

# get attributes of cars
for car in [town_car_1, sport_car_1, work_car_1, police_car_1]:
    for att in ['name', 'color', 'is_police', 'speed']:
        print(att, getattr(car, att))
    print('-' * 20)

police_car_1.show_speed()
town_car_1.stop()
sport_car_1.go()
police_car_1.turn('left')

print('-' * 20)
work_car_1.show_speed()
work_car_1.speed = 50
work_car_1.show_speed()

print('-' * 20)
town_car_1.show_speed()
town_car_1.speed = 70
town_car_1.show_speed()
