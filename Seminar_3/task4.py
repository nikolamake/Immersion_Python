# Создайте словарь со списком вещей для похода в качестве ключа
# и их массой в качестве значения. Определите какие вещи влезут в
# рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть
# один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
import  random
max_capacity = int(input('Введите грузоподъемность рюкзака,кг : '))
list_things = dict(compass=0.5, lantern=0.7, thermos=2.2, med_cab=0.6, flask=0.75, \
                   meal=1.8, tent=3.5, shoes=0.8, bedroll=1.2, dishes=0.3)
things = []
mass_max = max_capacity
for element in list_things:
    if mass_max - list_things[element] >= 0:
        things.append(element)
        mass_max -= list_things[element]
print(f'Список вещей, которые поместятся в рюкзаке при его грузоподъемности {max_capacity},кг: ')
for i in things:
    print(i)