# Напишите программу, которая принимает две строки вида “a/b” -
# дробь с числителем и знаменателем. Программа должна возвращать
# сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
import  fractions


a = input('Введите числитель первой дроби: ')
b = input('Введите знаменатель первой дроби: ')
c = input('Введите числитель второй дроби: ')
d = input('Введите знаменатель второй дроби: ')

first_fraction_summ = a + '/' + b
second_fraction_summ = c + '/' + d
first_massiv = first_fraction_summ.split('/')
a1 = int(first_massiv[0])
b1 = int(first_massiv[1])
second_massiv = second_fraction_summ.split('/')
c1 = int(second_massiv[0])
d1 = int(second_massiv[1])
numerator_summ = int((a1 * d1) + (c1 * b1))
denominator_summ = int(b1 * d1)
for i in range(1, numerator_summ + 1):
    if (denominator_summ % i == 0) and (numerator_summ % i == 0):
        nod_summ = i
if nod_summ > 1:
    numerator_summ = int(numerator_summ / nod_summ)
    denominator_summ = int(denominator_summ / nod_summ)
fractions_summ = str(numerator_summ) + '/' + str(denominator_summ)


first_fraction_composition = a + '/' + b
second_fraction_composition = c + '/' + d
first_massiv = first_fraction_composition.split('/')
a1 = int(first_massiv[0])
b1 = int(first_massiv[1])
second_massiv = second_fraction_composition.split('/')
c1 = int(second_massiv[0])
d1 = int(second_massiv[1])
numerator_composition = int(a1 * c1)
denominator_composition = int(b1 * d1)
for i in range(1, numerator_composition + 1):
    if (denominator_composition % i == 0) and (numerator_composition % i == 0):
        nod_composition = i
if nod_composition > 1:
    numerator_composition = int(numerator_composition / nod_composition)
    denominator_composition = int(denominator_composition / nod_composition)
fractions_composition = str(numerator_composition) + '/' + str(denominator_composition)

f1 = fractions.Fraction(a1, b1)
f2 = fractions.Fraction(c1, d1)

print(f"Первая дробь: {first_fraction_summ} ")
print(f"Вторая дробь: {second_fraction_summ} ")
print(f"Сумма дробей: {first_fraction_summ} + {second_fraction_summ} = {fractions_summ}")
print(f"Для проверки суммы: {f1 + f2}")
print(f"Произведение дробей: {first_fraction_composition} * {second_fraction_composition} = {fractions_composition}")
print(f"Для проверки произведения: {f1 * f2}")
