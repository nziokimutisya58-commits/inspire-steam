# musa majjid
# 23/2/2026
# program to show inheritance in python

class Animal():
    def __init__(self,species,weight,food):
        self.species = species
        self.weight = weight
        self.food = food

    def grow(self,weight):
        weight = 1.1 * weight
        print(f"The animal weight {weight}")

    def eat(self,food):
        print(f"The animal eats {food}")

class Dog(Animal):
    def __init__(self,species,colour,weight,breed):
        super().__init__(species,weight,self.food)
        self.colour = colour
        self.weight = weight
        self.breed = breed

    def bark(self):
        weight = 1.1 * weight
        print(f"The animal weight {weight}")

    def eat(self,food):
        print(f"The animal eats {food}")

class Horse(Animal):
    def __init__(self, species, weight, food):
        def neigh(self,neigh):
            print(f"the animal neigh {neigh}")

        def eat(self,food):
            print("the animal eats {food}")
