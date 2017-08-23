class Restaraunt2():
    '''
    Представляет класс ресторана
    '''
    def __init__(self, restaurant_name2, cuisine_type2):
        '''инициализация атрибутов ресторана'''
        self.restauran_name2 = restaurant_name2
        self.cuisine_type2 = cuisine_type2

    def describe_restaurant2(self):
        print('Ресторан ' + str(self.restauran_name2) + ' ' + str(self.cuisine_type2))

    def open_restaurant_name2(self):
        print('Рестаран ' + str(self.restauran_name2) + ' ' + 'открыт!')

