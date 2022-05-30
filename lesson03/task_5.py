import random


def get_jokes(jokes_count, repeat_flag=False):
    """Create jokes using random words from nouns, adverbs and adjectives"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    try:
        if repeat_flag:
            for i in range(jokes_count):
                noun = nouns.pop(random.randrange(len(nouns)))
                adverb = adverbs.pop(random.randrange(len(adverbs)))
                adjective = adjectives.pop(random.randrange(len(adjectives)))
                joke = f'{noun} {adverb} {adjective}'
                jokes.append(joke)
        else:
            for i in range(jokes_count):
                joke = f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}'
                jokes.append(joke)
    except ValueError:
        print(f'Number of jokes should be <= 5')
    return jokes


print(get_jokes(3))
print(get_jokes(4, True))
print(get_jokes(6, True))  # check when number of jokes > 5
