class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def calc_mass(self, asphalt_mass_kg_one_cm, asphalt_thickness_cm):
        mass = self._length * self._width * asphalt_mass_kg_one_cm * asphalt_thickness_cm / 1000
        print(f'Масса асфальта, необходимого для покрытия всей дороги = {mass} т.')


road_1 = Road(5000, 20)
road_1.calc_mass(25, 5)
