class Restaraunt():
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


my_restaurant = Restaraunt('Звездочка', 'Славянская Кухня!')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant_name()

class IceCreamStand(Restaraunt):
    '''Класс особая разновидность ресторана, киоск с мороженным'''
    def __init__(self, restaurant_name, cuisine_type ):
        '''инициалезация параметров родителя
        затем инициализация атрибутов характерных для киоска'''

        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['пломбир', 'сливочное', 'эскимо', 'сосай-кусай']

    def show_flavors(self):

        for x in range(len(self.flavors)):
            print('Сорт: %s' % (self.flavors[x]))

my_icecream_res = IceCreamStand('Белый Мишка', 'Мороженное')

my_icecream_res.describe_restaurant()
my_icecream_res.show_flavors()


