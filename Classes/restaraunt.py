class Restaraunt2():
    '''
    Представляет класс ресторана
    '''
    def __init__(self, restaurant_name, cuisine_type):
        '''инициализация атрибутов ресторана'''
        self.restauran_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Ресторан ' + str(self.restauran_name) + ' ' + str(self.cuisine_type))

    def open_restaurant_name(self):
        print('Рестаран ' + str(self.restauran_name) + ' ' + 'открыт!')


my_restaurant = Restaraunt2('Звездочка', 'Славянская Кухня!')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant_name()
