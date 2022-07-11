class ComplexNumOperations:
    def __init__(self, num):
        self.num = complex(num)

    def __str__(self):
        return f'{self.num}'

    def __add__(self, other):
        res = self.num + other.num
        return res

    def __mul__(self, other):
        res = self.num * other.num
        return res


num_1 = ComplexNumOperations('1e3+2e-3j')
num_2 = ComplexNumOperations('.1+2j')

print(num_1)
print(num_2)
print(num_1 + num_2)
print(num_2 * num_2)
