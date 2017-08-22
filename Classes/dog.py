class Dog():
    '''Простая модель собаки'''

    def __init__(self, name, age):
        '''Инициализация атрибутов name и age.'''
        self.name = name
        self.age = age

    def sit(self):
        '''Собака садитсяф по команде.'''
        print(self.name + ' сел.')

    def baw_woow(self):
        '''Собака лает'''
        print(self.name + ' лает')


my_dog = Dog('Дружок', 5)
another_dog = Dog('Балонка', 4)

print('Мою собаку зовут ' + my_dog.name + '.')
print('Ей ' + str(my_dog.age) + ' лет.')
my_dog.baw_woow()
my_dog.sit()
print()

print('А эту собаку зовут ' + another_dog.name + '.')
print('Ей ' + str(another_dog.age) + ' лет.')
another_dog.baw_woow()
another_dog.sit()

