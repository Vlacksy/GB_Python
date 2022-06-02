from requests import get, utils
from datetime import datetime


def get_param_value(content_str, value):
    """get parameter value from content string"""
    return content_str.split(value)[1][:content_str.split(value)[1].index('<')]


def currency_rates(currency_code):
    """Get currency value in rub"""
    currency_code = currency_code.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    date_val = datetime.strptime(content.split('Date="')[1][:10], '%d.%m.%Y').date()
    prices = {}

    for el in content.split('<Valute ID=')[1:]:
        # get values for all parameters of currency
        currency_num_code = get_param_value(el, '<NumCode>')
        currency_char_code = get_param_value(el, '<CharCode>')
        currency_nominal = get_param_value(el, '<Nominal>')
        currency_name = get_param_value(el, '<Name>')
        currency_value = round(float(get_param_value(el, '<Value>').replace(",", ".")), 2)

        # add currency with values to dict
        prices[currency_char_code] = {
            'NumCode': currency_num_code,
            'Nominal': currency_nominal,
            'Name': currency_name,
            'Value': currency_value
        }

    if currency_code in prices.keys():
        return f'На {date_val} {prices[currency_code]["Nominal"]} {prices[currency_code]["Name"]} ' \
               f'({currency_code}, код {prices[currency_code]["NumCode"]}) = {prices[currency_code]["Value"]} р. '


if __name__ == '__main__':
    print(currency_rates('NOK'))
    print(currency_rates('CNY'))
    print(currency_rates('RUB'))  # check for None
    print(currency_rates('amd'))  # check register
    print(currency_rates('Uzs'))  # check register
