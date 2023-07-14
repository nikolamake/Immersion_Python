# Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

system_calculus = 16
number_decimal = int(input('Введите число: '))
resultat = ''
number = number_decimal
while number > 0:
    remains = number % system_calculus
    if system_calculus == 16:
        if remains == 10:
            remains = 'a'
        if remains == 11:
            remains = 'b'
        if remains == 12:
            remains = 'c'
        if remains == 13:
            remains = 'd'
        if remains == 14:
            remains = 'e'
        if remains == 15:
            remains = 'f'
    resultat = str(remains) + resultat
    number = number // system_calculus
print(f"Число {number_decimal} в десятичной системе равно {resultat} в шестнадцатеричной системе.")

print(f"Проверка фунцией hex: {hex(number_decimal)[2:]}")
