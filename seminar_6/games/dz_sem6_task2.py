# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей
# на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.


def matrix_print(data_matrix):  # вывод матрицы на печать
    for x in data_matrix:
        for r in x:
            print(r, end='\t')
        print()


def show_board(coord_shapes):  # для отрисовки расположения фигур на поле 8х8 по полученным координатам
    board = [[chr(9898)] * 8 for i in range(8)]
    for j in range(8):
        board[coord_queen[j][0] - 1][coord_queen[j][1] - 1] = chr(9813)
    return matrix_print(board)


def beat_nearby(coord_shapes):
    correct = True
    for i in range(8):
        for j in range(i + 1, 8):
            if coord_shapes[i][0] == coord_shapes[j][0] or coord_shapes[i][1] == coord_shapes[j][1] \
                    or abs(coord_shapes[i][0] - coord_shapes[j][0]) == \
                    abs(coord_shapes[i][1] - coord_shapes[j][1]):
                correct = False
    if correct:
        print('Фигуры не бьют попарно друг друга')
    else:
        print('Есть пара бьющих друг друга фигур')


coord_queen = [[1, 4], [2, 7], [3, 3], [4, 8], [5, 2], [6, 5], [7, 1], [8, 6]]  # координаты ферзей

show_board(coord_queen)
beat_nearby(coord_queen)
