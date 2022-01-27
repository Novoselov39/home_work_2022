class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        a=''
        for i in range(len(self.matrix)):
            a = a + '\t'.join(map(str,self.matrix[i])) + '\n'
        return str(a)

    def __add__(self, other):
        sum_matrix = []
        a = self.matrix
        for a, b in zip(a, other.matrix):
            s = []
            for i, j in zip(a,b):
                sum_el = i+j
                s.append(sum_el)
            sum_matrix.append(s)
        return Matrix(sum_matrix)


matrix1 = Matrix([[2, 3, 9], [3, 4, 6], [65,67,98]])
matrix2 = Matrix([[87, 34, 98], [30, 34, 86], [55,17,28]])
summ = matrix1 + matrix2

print(matrix1)
print(matrix2)
print('Сумма:')
print(summ)

