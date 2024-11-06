class Animal:
    def __init__(self, name, alive=True, fed=False):
        self.alive = alive
        self.fed = fed
        self.name = name


class Plant:
    def __init__(self, name, edible=False):
        self.name = name
        self.edible = edible


class Mammal(Animal):
    def __eat__(self, food):
        if self.food:
            print(self.name, ' съел ', food.name)
            self.fed = True
        else:
            print(self.name, ' не стал есть ', food.name)
            alive = False



class Predator(Animal):



class Flower(Plant):



class Fruit(Plant):