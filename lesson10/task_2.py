from abc import ABC, abstractmethod


class Clothes(ABC):
    sum_fabric_consumption = 0

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Clothes.sum_fabric_consumption += self.fabric_consumption

    @property
    def fabric_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, growth):
        self.growth = growth
        Clothes.sum_fabric_consumption += self.fabric_consumption

    @property
    def fabric_consumption(self):
        return 2 * self.growth + 0.3


coat_1 = Coat(2)
suit_1 = Suit(3)

print(coat_1.fabric_consumption)
print(suit_1.fabric_consumption)
# sum
print(suit_1.sum_fabric_consumption)
