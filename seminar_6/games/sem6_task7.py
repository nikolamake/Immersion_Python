# Создайте модуль и напишите в нём функцию, которая получает на вход
# дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь,
# если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует
# Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

month_dict = {31: [1, 2, 3, 5, 7, 8, 10, 12], 30: [4, 6, 9, 11]}


def chek_date(inp_year):
    day, month, year = map(int, inp_year.split('.'))

    if 0 < day < 32 and 0 < month < 13 and 0 < year < 10000:
        if month != 2:
            if day in month_dict:
                return month in month_dict[day]
            else:
                return True
        else:
            if check_year(year):
                return day < 29
            else:
                return day < 30

def check_year(year):
    if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
        print('Год невисокосный')
        return True
    else:
        print('Год високосный')
        return False


print(chek_date(input('Введите дату: ')))
