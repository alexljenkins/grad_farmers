"""
FARM with 2 chickens 4 pigs and 4 cows
count total number of legs of all the animals on the farm
"""
class Animal:
    def __init__(self, name:str, legs:int) -> None:
        self.name = name
        if legs < 0:
            self.number_of_legs = 0
        else:
            self.number_of_legs = legs
        
    def __repr__(self):
        return f"the animal is {self.name}, and it has {self.number_of_legs}"

class Farm:
    def __init__(self):
        self.animals = list() # {'animal': Animal, 'count':4}
    
    def add_animal(self, animal:Animal, number):
        animal_type = []
        # creates list of animal names
        animal_type = [a['animal'].name for a in self.animals]

        if animal.name in animal_type:
            self.animals[animal_type.index(animal.name)]['count'] += number
        else:
            self.animals.append({'animal': animal, 'count':number})
        print(self.animals)
    
    def get_total_legs(self):
        return sum([animal['count'] * animal['animal'].number_of_legs for animal in self.animals])


def main():
    pigs = Animal('pig', 4)
    chickens = Animal('chicken', 2)    

    farm = Farm()
    farm.add_animal(pigs, 2)
    farm.add_animal(chickens, 3)
    farm.add_animal(chickens, -2)
    print(farm.animals)
    print(farm.get_total_legs())  
if __name__ == '__main__':
    main()
