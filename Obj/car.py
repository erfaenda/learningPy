class Car():
    '''Простая модель автомобиля'''
    def __init__(self, make, model, year):
        '''Инициализирует атрибуты описания автомобиля'''
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 100

    def get_descriptive_name(self):
        '''Возвращает аккуратно отформатированное описание'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometr(self):
        '''Выводит пробег машины в милях'''
        print('Пробег этой машины ' + self.model + ' ' + self.make + ' ' + str(self.odometr_reading) + ' километров')

    def update_odometr(self, kmrage):
        '''Метод обновления одометра
        при попытки с крутки отклоняет изменения'''
        if kmrage >= self.odometr_reading:
            self.odometr_reading = kmrage
        else:
            print('Вы не должны скручивать пробег!')

    def incriment_odometr(self, kmrage):
        '''Метод плюсующий пробег к уже текущему пробегу'''
        self.odometr_reading += kmrage

my_new_car = Car('Hyndai', 'Accent', 2009)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometr()
my_new_car.incriment_odometr(198)
my_new_car.read_odometr()