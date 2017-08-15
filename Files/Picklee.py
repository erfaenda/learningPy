import pickle
import time
game_data = {
    'позиция-игрока' : 'C23 B45',
    'карманы' : ['ключи', 'карманный нож', 'гладкий камень'],
    'рюкзак' : ['веревка', 'молоток', 'яблоко'],
    'деньги' : 158.50
}
save_file = open('/home/alex/save.dat', 'wb') #wb писать фал в бинарном формате
pickle.dump(game_data, save_file)
save_file.close()
print('Файл' + str(save_file) + 'успешно сохранен')
print('--------------следущая программа--------------')
time.sleep(1)
print('--------------идет загрузка файла-------------')
time.sleep(2)
load_file = open('/home/alex/save.dat', 'rb')#rb читать файл в бинарном формате
loaded_game_date = pickle.load(load_file)
load_file.close()
print(loaded_game_date)
