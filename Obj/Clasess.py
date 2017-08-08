class Things:
    pass

class Inanimate(Things):
    pass

class Animate(Things):
    pass

class SideWalk(Inanimate):
    pass

class Animals(Animate):
    def breathe(self):
        print('Дышит')
    def move(self):
        print('Двигается')
    def eat_food(self):
        print('Питается')

class Mammals(Animals):
    def feed_milk(self):
        print('Кормит молоком')

class Girafes(Mammals):
    def eat_leavs(self):
        print('Ест листья')

reginald = Girafes()
harold = Girafes()

harold.breathe()
reginald.eat_leavs()
reginald.move()