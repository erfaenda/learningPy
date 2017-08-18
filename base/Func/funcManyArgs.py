def make_pizza(size, *manyargz):
    print('Вы заказали пиццу размера ' + str(size))
    for manyarg in manyargz:
        print('- ' + manyarg)
make_pizza('peperoni')

make_pizza(12, 'Пеперони', 'грибы', 'томаты', 'тертый сыр', 'оливки')