# Треугольник существует только тогда, когда сумма любых
# двух его сторон больше третьей.
# Дано a, b, c — стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.

# a = float(input('Введите длину стороны a: '))
# b = float(input('Введите длину стороны b: '))
# c = float(input('Введите длину стороны c: '))
# if (a + b) < c or (a + c) < b or (c + b) < a:
#     print('Треугольник с такими сторонами не существует!')
# elif a != b and a != c and c != b:
#     print('Треугольник является разносторонним.')
# elif a == b and a == c and b == c:
#     print('Треугольник является равносторонним.')
# else:
#     print('Треугольник является равнобедренным.')

# , a: float, b: float, c: float
class CheckTriangle:
    def __init__(self):
        self.a = float(input('Введите длину стороны <a> треугольника : '))
        self.b = float(input('Введите длину стороны <b> треугольника : '))
        self.c = float(input('Введите длину стороны <c> треугольника : '))
        if (self.a + self.b) < self.c or (self.a + self.c) < self.b or (self.c + self.b) < self.a:
            print('Треугольник с такими сторонами не существует!')
        else:
            self.chek_sides()

    def chek_sides(self):
        if self.a != self.b and self.a != self.c and self.c != self.b:
            print('Треугольник является разносторонним.')
        elif self.a == self.b and self.a == self.c and self.b == self.c:
            print('Треугольник является равносторонним.')
        else:
            print('Треугольник является равнобедренным.')

CheckTriangle()
