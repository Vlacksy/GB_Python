def num_translate(eng_num):
    """Translate numbers from En to Ru"""
    translate_dict = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }
    return translate_dict.get(eng_num)


print(num_translate('one'))
print(num_translate('eight'))
print(num_translate('eleven'))  # check None
