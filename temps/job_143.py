import copy
import pickle
class Car:
    pass

car1 = Car()
car1.wheels = 4
car2 = car1
car2.wheels = 3
print(car1.wheels)

car3 = copy.copy(car1) #в этом случае объект копируется
car3.wheels = 6
print(car1.wheels) #шин в нем так и осталось 3

# сохранение в фал списка
my_favorite_list = ['смартфон', 'ссд', 'гном', 'кристалл']
save_my_list = open('c:\\myfavoritlist.dat', 'wb')
pickle.dump(my_favorite_list, save_my_list)
save_my_list.close()
# загрузка из файла
load_file = open('c:\\myfavoritlist.dat', 'rb')
loaded_file_data = pickle.load(load_file)
load_file.close()
print(loaded_file_data)