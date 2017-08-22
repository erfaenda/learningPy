class User():
    '''класс характеризующий обычного пользователя домена'''
    def __init__(self, fist_name, last_name, departments, location):
        '''инициализируем атрибуты описания пользователя'''
        self.fist_name = fist_name
        self.last_name = last_name
        self.departments = departments
        self.location = location
        self.svodka = [fist_name, last_name, departments, location]

    def describe_user(self):
        '''метод выводящий  всю сводную информацию'''
        print('Сводная информация' + str(self.svodka))

    def greet_users(self):
        print('Доброго времени суток ' + self.fist_name + ' ' + self.last_name)

simple_user = User('Витек', 'Ракетов', 'очкодёр', 'кабинет белых камней')

simple_user.describe_user()
simple_user.greet_users()