import re


def email_parse(email_address):
    result = {}
    pattern = re.compile(r'(?P<username>\w+)@(?P<domain>\w+\.\w+)')
    try:
        for word in pattern.finditer(email_address):
            result = word.groupdict()
        if result:
            return result
        else:
            raise ValueError(f'wrong email: {email_address}')
    except ValueError as e:
        return f'{e}'


print(email_parse('123name321@gmail.com'))
print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))
