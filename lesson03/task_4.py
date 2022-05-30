def thesaurus(*people):
    """Get surnames and names for each letter"""
    names_dict = {}
    for man in sorted(people, key=lambda man: (man.split()[1][0], man[0])):
        name_letter, surname_letter = man[0], man.split()[1][0]
        if surname_letter not in names_dict:
            names_dict[surname_letter] = {name_letter: [man]}
        elif name_letter not in names_dict[surname_letter]:
            names_dict[surname_letter][name_letter] = [man]
        else:
            names_dict[surname_letter][name_letter].append(man)
    return names_dict


print(thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
