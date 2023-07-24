# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной
# расстановки ферзей в задаче выше. Проверяйте
# различный случайные  варианты и выведите 4 успешных расстановки.
from random import randint


def matrix_print(data_matrix):  # вывод матрицы на печать
    for x in data_matrix:
        for r in x:
            print(r, end='\t')
        print()


def show_board(coord_shapes):  # для отрисовки расположения фигур на поле 8х8 по полученным координатам
    board = [[chr(9898)] * 8 for i in range(8)]
    for j in range(8):
        board[rnd(1, 8, 2, 8)[j][0] - 1][rnd(1, 8, 2, 8)[j][1] - 1] = chr(9813)
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
        print(f'Фигуры не бьют попарно друг друга')
    else:
        print(f'Есть пара бьющих друг друга фигур')
    return correct


def rnd(*args):
    random_queen = [[randint(1, 8) for j in range(2)] for i in range(8)]
    return random_queen


while beat_nearby(rnd(1, 8, 2, 8)) != True:
    beat_nearby(rnd(1, 8, 2, 8))
print(rnd(1, 8, 2, 8))
show_board(rnd(1, 8, 2, 8))
beat_nearby(rnd(1, 8, 2, 8))

