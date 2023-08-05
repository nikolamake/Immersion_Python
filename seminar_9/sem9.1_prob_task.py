# 📌 Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными
# числами в каждой строке. 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения
# корней квадратного уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и
# работы функции в json файл.
# 📌 Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса

from random import randint
import csv
import numpy
from typing import Callable
import os
import json

def decor_csv(func: Callable):
    generat_csv()
    def wrapper():
        with open('coeff_equation.csv', 'r', encoding='UTF-8') as file:
            data = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
            for line in data:
                if line and line[0] != 0:
                    func(*line)
    return wrapper
def decor_json(func: Callable):
    if os.path.exists('save.json'):
        with open('save.json') as f_read:
            data = json.load(f_read)
    data = {}
    def wrapper(*args, **kwargs):

        with open('save.json', 'w') as f_write:
            data.update({'args: ' + str(args): 'roots: ' + func(*args, **kwargs)})
            json.dump(data, f_write, indent=2, ensure_ascii=False)
        # result = func(*args, **kwargs)
        # return result
    return wrapper
def generat_csv():
    with open('coeff_equation.csv', 'w', encoding='UTF-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for row in range(100, 1000):
            writer.writerow([randint(-20, 50), randint(-20, 70), randint(-20, 30)])
def print_decision(m, n , k, l, t):  # для печати ур-й и результатов
    print(f'{m}x2 + {n}x + {k}')
    print(f'x1 = {l}, x2 = {t}')


@decor_csv
@decor_json
def find_roots(a, b, c):
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = round((-b + discr ** 0.5) / (2 * a), 3)
        x2 = round((-b - discr ** 0.5) / (2 * a), 3)
        # print(f'{a}x2 + {b}x + {c}')
        # print(f'x1 = {x1}, x2 = {x2}')
        print_decision(a, b, c, x1, x2)
        return f'x1 = {x1}, x2 = {x2}'
    elif discr == 0:
        x1 = round(-b / (2 * a), 3)
        print_decision(a, b, c, x1, None)
        # print(f'{a}x2 + {b}x + {c}')
        # print(f'x1 = {x1}')
        return f'x1 = {x1}'
    else:
        x1 = numpy.around((-b + discr ** 0.5) / (2 * a), 3)
        x2 = numpy.around((-b - discr ** 0.5) / (2 * a), 3)
        print_decision(a, b, c, x1, x2)
        # print(f'{a}x2 + {b}x + {c}')
        # print(f'x1 = {x1}, x2 = {x2}')
        return f'x1 = {x1}, x2 = {x2}'
print(find_roots())
find_roots()