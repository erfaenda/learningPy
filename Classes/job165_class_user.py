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
just_user = User('Морис', 'Пескарев', 'клееерк', 'кабинет под лесницей')

simple_user.describe_user()
simple_user.greet_users()
just_user.describe_user()
just_user.greet_users()

class Privelegis():
    '''отдельный самодостаточный класс содержит в себе различные привелегии'''
    def __init__(self, privelegis=['разрешено добавлять пользователя',
                      'разрешено удалять пользователя',
                      'разрешено банить пользователей']):
        '''инициализирует привелегии'''
        self.privelegis = privelegis

    def show_privilegis(self):
        print('Имеющиеся привелегии: '+ str(self.privelegis))



class Admin(User):
    '''класс характеризующий особенности администратора'''
    def __init__(self, fist_name, last_name, departments, location):
        '''инициализация специфических данных класса админ'''
        super().__init__(fist_name, last_name, departments, location)
        self.privelegis = Privelegis()


print('-------------------------------')
dcadmin = Admin('ДЭнчик', 'Кабельканалов', 'СМЫВ', 'Ырлова')
dcadmin.greet_users()
dcadmin.privelegis.show_privilegis()
