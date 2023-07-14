"""Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: «Число является простым,
если делится нацело только на единицу и на себя».
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч."""


num = int(input('Введите положительное число меньше 100 тысяч: '))
if num > 0 and num < 100000:
    divider = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            divider +=1
    if divider <= 0:
        print('Число является простым')
    else:
        print('Число является составным')
else:
    print('Введите корректное число')

