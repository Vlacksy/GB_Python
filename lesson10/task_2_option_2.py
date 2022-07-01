from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def fabric_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, growth):
        self.growth = growth

    @property
    def fabric_consumption(self):
        return 2 * self.growth + 0.3


class ClothesBasket:
    def __init__(self):
        self.clothes = []
        self.fabric = 0

    def add(self, thing):
        self.clothes.append(thing)
        self.fabric += thing.fabric_consumption

    def remove(self, thing):
        self.clothes.remove(thing)
        self.fabric -= thing.fabric_consumption

    @property
    def sum_fabric_consumption(self):
        return self.fabric


coat_1 = Coat(2)
suit_1 = Suit(3)

print(coat_1.fabric_consumption)
print(suit_1.fabric_consumption)

print('-'*10 + 'Check basket' + '-'*10)
# initiate basket to calculate consumption for needed clothes
clothes_basket = ClothesBasket()
# add coat_1 and suit_1 to basket
clothes_basket.add(coat_1)
clothes_basket.add(suit_1)
# get sum consumption for all things in basket
print(clothes_basket.sum_fabric_consumption)

print('-'*10 + 'Check remove from basket' + '-'*10)
# check remove
clothes_basket.remove(coat_1)
print(clothes_basket.sum_fabric_consumption)
