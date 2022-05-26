from decimal import getcontext, Decimal

getcontext().prec = 2


def prices(price_list):
    all_prices = ''
    for price in price_list:
        rub = int(price)  # get rub
        kopeck = f'{int((Decimal(price) - rub) * 100):02d}'  # get kop, decimal is used for correct value of kop
        all_prices += f'{rub} руб {kopeck} коп, '
    return all_prices[:-2]


my_price_list = [57.8, 46.51, 97, 123.22, 22, 4.78, 98.34, 88, 12.06, 46.46, 57.7, 88.07, 100]

# A
print(prices(my_price_list))
# B
print(sorted(my_price_list))
print(my_price_list)  # check that my list is not changed after sorting
# C
new_price_list = sorted(my_price_list, reverse=True)  # create new list from my list sorted desc
print(new_price_list)
# D
print(new_price_list[:5])  # 5 most expensive prices
