from utils import currency_rates
import sys

currency_code = sys.argv[1]
print(currency_rates(currency_code))
