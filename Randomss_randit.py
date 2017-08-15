import random

num = random.randint(1, 100)

a = 5
while a != 0:
    print('Введите число от 1 до 100, у вас %s попыток' % (a))
    guess = input()
    i = int(guess)
    if i == num:
        print('Ура ты угадал!!!')
        break
    elif i > num:
        a = a - 1
        print('Загаданное число меньше')
    elif i < num:
        a = a - 1
        print('Загаданное число больше')