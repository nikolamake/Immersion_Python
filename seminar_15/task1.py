import argparse
import logging

logging.basicConfig(level=logging.INFO, encoding="utf-8", filename="task1.log", filemode="a",
                    format='%(levelname)s, %(asctime)s, %(message)s')
class ValueTriangleError(Exception):
    """Исключение при вводе данных"""
    def __init__(self):
        super().__init__()
    def __str__(self):
        return ('Длина сторон треугольника должна быть больше "0"!')

class MeaningTriangleError(Exception):
    """Исключение при вводе данных"""
    def __init__(self):
        super().__init__()
    def __str__(self):
        return ('Треугольник с такими сторонами не существует! Сумма длин двух сторон должна быть больше третьей стороны')


class CheckTriangle:

    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            logging.error(f'Длина  <{a}> <{b}> <{c}> стороны треугольника должна быть больше "0"!')
            raise ValueTriangleError

        if (self.a + self.b) < self.c or (self.a + self.c) < self.b or (self.c + self.b) < self.a:
            logging.error(f'Треугольник со сторонами: <{a}> <{b}> <{c}> не существует! '
                          'Сумма длин двух сторон должна быть больше третьей стороны')
            raise MeaningTriangleError

        else:
            self.chek_sides

    def chek_sides(self):
        if self.a != self.b and self.a != self.c and self.c != self.b:
            logging.info(f'Треугольник со сторонами <{self.a}> <{self.b}> <{self.c}> является разносторонним.')
            return 'Треугольник является разносторонним.'
        elif self.a == self.b and self.a == self.c and self.b == self.c:
            logging.info(f'Треугольник со сторонами <{self.a}> <{self.b}> <{self.c}> является равносторонним.')
            return 'Треугольник является равносторонним.'
        else:
            logging.info(f'Треугольник со сторонами <{self.a}> <{self.b}> <{self.c}> является равнобедренным.')
            return 'Треугольник является равнобедренным.'


# print(CheckTriangle(5, 3, 5).chek_sides())
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-a', type=float)
    parser.add_argument('-b', type=float)
    parser.add_argument('-c', type=float)
    args = parser.parse_args()
    print(CheckTriangle(args.a, args.b, args.c).chek_sides())