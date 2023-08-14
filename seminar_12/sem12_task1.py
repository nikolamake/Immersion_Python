# � Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву
# и наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра.
# Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки
# (от 2 до 5) и результаты тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам
import csv


class Validator:

    def __set_name__(self, owner, name):
        self._param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self._param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self._param_name, value)

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f'"Введенные данные не являются строкой"')

        if not value.isalpha():
            raise ValueError(f'Строка должна содержать только буквы')

        if not value.istitle():
            raise ValueError(f'Строка должна начинаться с заглавной буквы')


class Student:
    name = Validator()
    surname = Validator()
    patronymic = Validator()

    def __init__(self, name, surname, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.disciplines = []
        self.progress: dict[str: list[int, int]] = dict()
        self.upload_items()

    def upload_items(self):
        with open(f'Disciplines.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f, 'excel')
            for row in reader:
                self.disciplines.append(r := row[0])
                self.progress[r] = [None, None]

    def save_estimation(self, discipline: str, estimation: int):
        if not (2 <= estimation <= 5):
            raise ValueError(f'Значение не существует')
        else:
            self.progress[discipline][0] = estimation

    def save_test_res(self, discipline: str, res: int):
        if not (0 <= res <= 100):
            raise ValueError(f'Значение не существует')
        else:
            self.progress[discipline][1] = res

    def get_average(self) -> tuple[float, float]:
        average_mark, average_res = 0, 0
        mark_counter, res_counter = 0, 0
        for m_, r_ in self.progress.values():
            if m_ is not None:
                average_mark += m_
                mark_counter += 1
            if r_ is not None:
                average_res += r_
                res_counter += 1
        return average_mark / mark_counter, average_res / res_counter

s = Student('Максим', 'Максимович', 'Максимов')
print(s)
print(f' {s.disciplines}')
print(f' {s.progress}')
print(f' {s.save_estimation}')

