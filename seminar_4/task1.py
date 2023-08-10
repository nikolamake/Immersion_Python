# Напишите функцию для транспонирования матрицы


from random import randint


def matrix_print(data_matrix): #вывод матрицы на печать
    for x in original_matrix:
        for r in x:
            print(r, end='\t')
        print()


def matrix_transp(matrix):  #транспонирование матрицы
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


line = int(input('Введите число строк матрицы: '))
column = int(input('Введите число столбцов матрицы: '))
if line <= column:
    original_matrix = [[randint(1, 10) for j in range(column)] for i in range(line)]
    print('Исходная матрица: ')
    matrix_print(original_matrix)
    print('транспонированная матрица: ')
    matrix_print(matrix_transp(original_matrix))
else:
    print('Число столбцов должно быть не меньше числа строк')

