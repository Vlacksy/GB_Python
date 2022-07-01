class Cell:
    def __init__(self, cells_num):
        self.cells_num = cells_num

    def __add__(self, other):
        res = self.cells_num + other.cells_num
        return Cell(res)

    def __sub__(self, other):
        if self.cells_num - other.cells_num <= 0:
            raise 'Difference in the number of cells is less than zero'
        else:
            res = self.cells_num - other.cells_num
            return Cell(res)

    def __mul__(self, other):
        res = self.cells_num * other.cells_num
        return Cell(res)

    def __floordiv__(self, other):
        res = self.cells_num // other.cells_num
        return Cell(res)

    def make_order(self, line_len):
        num = self.cells_num
        res = ''
        while num > line_len:
            res += '*' * line_len + '\n'
            num -= line_len
        if num > 0:
            res += '*' * num + '\n'
        return res


cell_1 = Cell(12)
cell_2 = Cell(10)
cell_3 = cell_1 + cell_2
cell_4 = cell_1 - cell_2
cell_5 = cell_1 * cell_2
cell_6 = cell_1 // cell_2
# cell_7 = cell_2 - cell_1  # check raise

print(cell_1.cells_num)
print(cell_2.cells_num)
print(cell_3.cells_num)
print(cell_4.cells_num)
print(cell_5.cells_num)
print(cell_6.cells_num)

print(cell_1.make_order(5))
print(cell_2.make_order(5))
print(cell_4.make_order(5))
