# ✔ Три друга взяли вещи в поход.
# Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.

friend_thing = dict(friend_1=('thing1', 'thing2', 'thing4', 'thing6', 'thing8'),
                    friend_2=('thing1', 'thing3', 'thing4', 'thing5', 'thing7'),
                    friend_3=('thing5', 'thing4', 'thing9', 'thing7', 'thing3'))


friends = []                                        #друзья которые идут в поход
for i in friend_thing:
    friends.append(i)

thing_friends_1 = set(friend_thing['friend_1'])  # вещи 1-го друга
thing_friends_2 = set(friend_thing['friend_2'])
thing_friends_3 = set(friend_thing['friend_3'])

general_things = thing_friends_1 | thing_friends_2 | thing_friends_3                    # все вещи
unique_thing_friends_1 = thing_friends_1.difference(thing_friends_2 | thing_friends_3)
unique_thing_friends_2 = thing_friends_2.difference(thing_friends_1 | thing_friends_3)
unique_thing_friends_3 = thing_friends_3.difference(thing_friends_1 | thing_friends_2)


print(f'Друзя, которые идут в поход: {friends}')
print(f'Все вещи друзей:\n {general_things}')
# print(f'Вещи первого друга: {thing_friends_1}')
# print(f'Вещи второго друга: {thing_friends_2}')
# print(f'Вещи третьего друга: {thing_friends_3}')
print(f'Вещи, которые есть только у первого друга:\n {unique_thing_friends_1}')
print(f'Вещи, которые есть только у второго друга:\n {unique_thing_friends_2}')
print(f'Вещи, которые есть только у третьего друга:\n {unique_thing_friends_3}')


