import copy

class Animal:
    def __init__(self,species, number_of_leg, color):
        self.species = species
        self.number_of_leg = number_of_leg
        self.color = color

Harry = Animal('гипапотам', 4, 'розовый')
Barry = Animal('Воробушек', 5, 'коричневенький')
Rukka = Animal('Волк', 2, 'серый')
Sally = Animal('сфинкс', 4, 'песочный')

animal_list = [Harry, Barry, Rukka]
more_animals = copy.deepcopy(animal_list)

print(len(more_animals))
animal_list.append(Sally)
print(len(animal_list))

'''more_animals = copy.copy(animal_list)
animal_list.append(Sally)
print(len(animal_list))
print(len(more_animals))

animal_list[1].color = 'говнистый'
print(more_animals[0].color)
print(more_animals[1].color)
'''