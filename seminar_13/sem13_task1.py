from random import randint

class MatrixError(Exception):
    pass

class MatrixAddEqError(MatrixError):
    """Исключение при сложении или сравнении 2-х матриц"""
    def __init__(self):
        super().__init__()
    def __str__(self):
        return (f'Операция сложения/сравнения матриц невозможна! Число строк - "{matrix_1.line}"'
                f'/столбцов - "{matrix_1.column}" первой '
                f'матрицы неравно соответственно числу столбцов - "{matrix_2.column}"/строк - "{matrix_2.line}" второй матрицы!')

class MatrixMulError(MatrixError):
    """Исключение при умножении 2-х матриц"""
    def __init__(self):
        super().__init__()
    def __str__(self):
        return (f'Операция умножения матриц невозможна! Число столбцов - "{matrix_1.column}" первой '
                                 f'матрицы неравно числу строк - "{matrix_2.line}" второй матрицы!')


class Matrix:

    def __init__(self, line: int, column: int, numbre_top: int, numbre_botton: int):
        """ line - количество строк матрицы
            column - количество столбцов матрицы
            numbre_top - минимальное целое значение в матрице
            numbre_botton - максимальное целое значение в матрице"""
        self.line = line
        self.column = column
        self.numbre_top = numbre_top
        self.numbre_botton = numbre_botton
        self.matrix = [[randint(self.numbre_top, self.numbre_botton)
                        for j in range(self.column)] for i in range(self.line)]

    def __str__(self):
        """Вывод на печать в виде матрицы"""
        res = ''
        for i in range(self.line):
            sub_res = ''
            for j in range(self.column):
                sub_res += str(f'{self.matrix[i][j]:>3}') + ' '
            res += sub_res + '\n'
        return res

    def __add__(self, other):
        """Сложение двух матриц"""
        if self.line != other.line or self.column != other.column:
            raise MatrixAddEqError
        res = []
        for i in range(self.line):
            sub_res = []
            for j in range(self.column):
                sub_res.append(self.matrix[i][j] + other.matrix[i][j])
            res.append(sub_res)
        return res

    def __eq__(self, other):
        """Сравнение двух матриц"""
        if self.line != other.line or self.column != other.column:
            raise MatrixAddEqError
        for i in range(self.line):
            for j in range(self.column):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True

    def __mul__(self, other):
        """Умножение двух матриц"""
        if self.column != other.line:
            raise MatrixMulError
        res = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*other.matrix)] for row_a in self.matrix]
        return res


matrix_1 = Matrix(3, 3, 2, 20)
print('matrix_1' '\n' f'{matrix_1}')

matrix_2 = Matrix(3, 3, 4, 8)
print('matrix_2' '\n' f'{matrix_2}')

matrix_3 = matrix_1 + matrix_2
print('Результат сложения matrix_1 и matrix_2')
for x in matrix_3:
    for r in x:
        print(f'{r:>3}', end='\t')
    print()

matrix_4 = matrix_1 * matrix_2
print('Результат умножения matrix_1 на matrix_2')
for x in matrix_4:
    for r in x:
        print(f'{r:>3}', end='\t')
    print()


print(f'Результат сравнения matrix_1 и matrix_2 \n{matrix_1 == matrix_2}')
