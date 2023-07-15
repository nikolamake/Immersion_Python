# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

from random import randint

source_list = []
for i in range(10):
    source_list.append(randint(1, 20))
print(f'Исходный список: \n{source_list}')

unique_list = []
for element in source_list:
    if element not in unique_list:
        unique_list.append(element)
print(f'Список значений без дубликатов: \n{unique_list}')

doubl_list = []
for meaning in source_list:
    if source_list.count(meaning) > 1:
        doubl_list.append(meaning)
print(f'Список повторяющихся значений: \n{doubl_list}')
