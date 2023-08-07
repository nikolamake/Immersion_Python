# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа
# и верните его из класса-фабрики.


class Animal:

    def __init__(self, name, age, voice='groal'):
        self.name = name
        self.age = age
        self.voice = voice


    def make_voice(self):
        print(self.voice)

    def call_name(self):
        print(self.name)

class Fish(Animal):
    def __init__(self, name, age, scales, voice):
        super().__init__(name, age, voice)
        self.scales = scales
    def swim(self):
        print("i'm swimming, oh, it's titan!")


class Dog(Animal):
    def __init__(self, name, age, breed, voice):
        super().__init__(name, age, voice)
        self.breed = breed
    def bark(self):
        print('Bark!')


class Raven(Animal):
    def __init__(self, name, age, color, voice):
        super().__init__(name, age)
        self.voice = voice
        self.color = name
    def fly_around_corpse(self):
        print('oooh, meat....')


class Factory:
    @staticmethod
    def create_animal(name_class):
        match name_class.__name__:
            case 'Fish':
                return Fish('Pepe', 1, 'green', 'ups')
            case 'Dog':
                return Dog('Kuza', 8, 'blac', 'av-tav')
            case 'Raven':
                return Raven('Vasa', 3, 'blue', 'ku-ka-re')

fish = Factory.create_animal(Fish)
dog = Factory.create_animal(Dog)
raven = Factory.create_animal(Raven)
animals = [fish, dog, raven]
print('Так зовут животных : ')
for i in animals:
    i.call_name()
print(f'Такие голоса у животных : ')
for i in animals:
    i.make_voice()