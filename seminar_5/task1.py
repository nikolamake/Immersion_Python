# ✔Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж
# из трёх элементов: путь, имя файла, расширение файла.


import os

def patch_line(line_adr):
    adr = os.path.abspath(line_adr)
    lst = adr.replace('.', '\\').split('\\')
    tuple_new = (adr, lst[-2], lst[-1])
    return tuple_new


str_adr = input('Введите имя файла: ')
print(patch_line(str_adr))