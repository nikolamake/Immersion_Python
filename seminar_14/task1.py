class TriangleError(Exception):
    pass

class ValueTriangleError(TriangleError):
    """Исключение при вводе данных"""
    def __init__(self):
        super().__init__()
    def __str__(self):
        return ('Длина треугольника должна быть больше "0"!')

class MeaningTriangleError(TriangleError):
    """Исключение при вводе данных"""
    def __init__(self):
        super().__init__()
    def __str__(self):
        return ('Треугольник с такими сторонами не существует! Сумма длин двух сторон должна быть больше третьей стороны')


class CheckTriangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            raise ValueTriangleError
        if (self.a + self.b) < self.c or (self.a + self.c) < self.b or (self.c + self.b) < self.a:
            raise MeaningTriangleError
        else:
            self.chek_sides()

    def chek_sides(self):
        if self.a != self.b and self.a != self.c and self.c != self.b:
            print('Треугольник является разносторонним.')
        elif self.a == self.b and self.a == self.c and self.b == self.c:
            print('Треугольник является равносторонним.')
        else:
            print('Треугольник является равнобедренным.')

CheckTriangle(5,0,4)