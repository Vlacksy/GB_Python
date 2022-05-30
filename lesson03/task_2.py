def num_translate_adv(eng_num):
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
    if eng_num.istitle():
        return translate_dict.get(eng_num.lower()).capitalize()
    else:
        return translate_dict.get(eng_num)


print(num_translate_adv('One'))
print(num_translate_adv('two'))
print(num_translate_adv('eleven'))  # check None
