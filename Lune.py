import sys

def moon_weight():
    i = 0
    print('Введите свой вес')
    mass = int(sys.stdin.readline())
    print('Сколько лет вы планируете прибывать на луне?')
    years = int(sys.stdin.readline())
    print('На какой коэфицент будем толстеть?')
    gravitymass = float(sys.stdin.readline())
    for i in range(years):
        mass = mass + gravitymass
        print(mass)

moon_weight()
