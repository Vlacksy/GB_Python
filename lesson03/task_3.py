def thesaurus(*names):
    """Get names for each letter"""
    letters = sorted(set([name[0] for name in names]))  # set used to remove duplicate values
    names_dict = {}
    for letter in letters:
        names_dict[letter] = list(filter(lambda name: name.startswith(letter), names))
    return names_dict


# Option 1
print(thesaurus("Иван", "Мария", "Петр", "Илья"))

# Option 2
name_list = ["Иван", "Мария", "Петр", "Илья"]
print(thesaurus(*name_list))
