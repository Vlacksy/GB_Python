# Option 1
def odd_nums(m):
    """Return odd nums from 1 to n"""
    return [num for num in range(1, m+1, 2)]


n = int(input('Введите число n: '))
print(odd_nums(n))

# Option 2
odd_to_n = (num for num in range(1, n+1, 2))
print(*odd_to_n)

# Option 3
print([num for num in range(1, n+1, 2)])
