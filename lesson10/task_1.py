class Matrix:

    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        res = ''
        for i in range(len(self.matrix_list)):
            res += '| '
            for j in range(len(self.matrix_list[i])):
                res += f'{self.matrix_list[i][j]} '
            res += '|\n'
        return res

    def __add__(self, other):
        if len(self.matrix_list) == len(other.matrix_list):  # check number of lines in both matrices
            res = []
            for i in range(len(self.matrix_list)):
                # check number elements in line i in both matrices
                if len(self.matrix_list[i]) == len(other.matrix_list[i]):
                    res.append([])
                    for j in range(len(self.matrix_list[i])):
                        res[i].append(self.matrix_list[i][j] + other.matrix_list[i][j])
                else:
                    raise 'Len of the matrices lines must be the same'
            return Matrix(res)
        else:
            raise 'Len of the matrices must be the same'


my_matrix_1 = Matrix([[1, 4], [2, 2], [1, 3]])
my_matrix_2 = Matrix([[31, 22], [37, 43], [51, 86]])
my_matrix_3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
my_matrix_4 = Matrix([[1], [2], [1]])

matrix_sum = my_matrix_1 + my_matrix_2
print(my_matrix_1)
print(my_matrix_2)
print(my_matrix_3)
print(my_matrix_4)
print(matrix_sum)
