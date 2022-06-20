from time import sleep


class TrafficLight:
    __color = {
        'red': [7, 31],
        'yellow': [2, 33],
        'green': [5, 32]
    }

    def running(self):
        for k, v in self.__color.items():
            print(f'\033[{v[1]}m {k}')
            sleep(v[0])


traffic_light_1 = TrafficLight()

while True:
    traffic_light_1.running()
