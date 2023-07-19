# Создайте функцию генератор чисел Фибоначчи


def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b


fib_gen = fib()
count = int(input('Введите количество чисел Фибоначчи: '))
for i in range(count):
    print(next(fib_gen))
