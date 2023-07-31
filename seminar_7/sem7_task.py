# Напишите функцию группового переименования файлов. Она должна:
# 1)принимать параметр- желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# 2)принимать параметр - количество цифр в порядковом номере.
# 3)принимать параметр - расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# 4)принимать параметр - расширение конечного файла.
# принимать - диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6
# из исходного имени файла. К ним прибавляется желаемое конечное имя,
# если оно передано. Далее счётчик файлов и расширение.
import os


def rename_files(number_digits: int, initial_extension: str, final_extension: str, \
                 start_range: int, end_range: int):
    """

    :param number_igits: количество цифр в порядковом номере
    :param initial_extension: расширение исходного файла
    :param final_extension: расширение конечного файла
    :param start_range: начало среза для имени файла
    :param end_range: конец среза для имени файла
    :return:
    """

    count = 1
    ordinal_number = str(count).rjust(number_digits, '0')  # порядковый номер переим-го файла
    for file in os.listdir():
        new_name = file.split('.')[0]
        if initial_extension == file.split('.')[-1]:
            os.rename(file, new_name[start_range:end_range] + str(ordinal_number) + '.' + final_extension)
            count += 1


rename_files(3, 'txt', 'bmp', 2, 4)
