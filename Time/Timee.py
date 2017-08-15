import time

def many_number(max):

    t1 = time.time()
    for x in range(0, max):
        print(x)
    t2 = time.time()
    print('Время прошедшее с момента запуска этой хуйни %s' % (t2 - t1))
many_number(1000000)