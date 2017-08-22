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

    def __init__(self, spots):
        self.giraffe_spots = spots

    def left_foot_foward(self):
        print('Левую ногу вперед')
    def left_foot_back(self):
        print('Левую ногу назад')
    def right_foot_foward(self):
        print('Правую ногу вперед')
    def right_foot_back(self):
        print('Правую ногу назад')
    def dance_foots(self):
        self.left_foot_foward()
        self.left_foot_back()
        self.right_foot_back()
        self.right_foot_foward()
        self.left_foot_back()
        self.right_foot_foward()

    def eat_leavs(self):
        print('Ест листья')
    def find_food(self):
        self.move()
        print('Я нашел еду')
        self.eat_food()
    def jig_dance(self):
        self.move()
        self.move()
        self.move()
        self.move()

#reginald = Girafes()
#harold = Girafes()
ozwald = Girafes(100)
gertruda = Girafes(500)

'''harold.breathe()
reginald.eat_leavs()
reginald.move()
reginald.feed_milk()
reginald.find_food()
reginald.jig_dance()
'''
ozwald.dance_foots()
print(ozwald.giraffe_spots)
print(gertruda.giraffe_spots)
