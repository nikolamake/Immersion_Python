# Напишите функцию принимающую на вход только ключевые параметры
# и возвращающую словарь, где ключ — значение переданного аргумента,
# а значение — имя аргумента. Если ключ не хешируем, используйте
# его строковое представление.

def revers_dict(**kwargs):
    result_dict = [type(5), type("5"), type(True), type((1, 2, 3)), type(5.2)]
    for value in kwargs.values():
        if type(value) not in result_dict:
            kwargs = {k: str(v) for k, v in kwargs.items()}
    convert_dict = {value: key for key, value in kwargs.items()}
    return convert_dict


inp_dict = {'35': 'abc', '200': 100, 'bc': 30, '25': 250, '45': ['sdf', 'jhg'], 'hf': {'12': 35, 'll': 35}}
print(inp_dict)
print(revers_dict(**inp_dict))

