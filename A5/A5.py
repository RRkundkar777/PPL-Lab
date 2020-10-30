class animal():
    def __init__(self):
        self.eyes = 2
        self.nose = 1
        self.ears = 2
        self.teeth = True
        self.mouth = 1

        self.legs = 4
        self.tail = 1
        

class wild_animal(animal):
    def __init__(self):
        super().__init__()
        self.place = "Jungle"

class carnivores(wild_animal):
    def __init__(self):
        super().__init__()
        self.food = "Non-Veg"

class herbivores(wild_animal):
    def __init__(self):
        super().__init__()
        self.food = "Veg"

class domestic_animal(animal):
    def __init__(self):
        super().__init__()
        self.place = "Jungle"
        self.food = "Humans Mercy"

class aquatic_animal(animal):
    def __init__(self):
        super().__init__()
        self.place = "UnderWater"
        self.food = "Planktons"       


class Elephant(herbivores):
    def __init__(self):
        super().__init__()
        self.trunk = 1
        self.nose = 0
        self.legsize = "huge"
        self.earsize = "Large"

class Fish(aquatic_animal):
    def __init__(self):
        super().__init__()
        self.legs = 0
        self.tail = 0
        self.ears = 0
        self.nose = 0
        self.nostrils = 2
        self.voice = "Grunt"

class Tiger(carnivores):
    def __init__(self):
        super().__init__()
        self.strips = "Black"
        self.color = "Orange"
        self.voice = "Roar"
        self.fingers = "Claws"

class Dog(domestic_animal):
    def __init__(self):
        super().__init__()
        self.color = "Black"
        self.voice = "Bark"
        self.fingers = "Claws"

class Cat(domestic_animal):
    def __init__(self):
        super().__init__()
        self.earposition = "Top"
        self.color = "Strips and Dots"
        self.voice = "Meow"

class Buffalo(domestic_animal):
    def __init__(self):
        super().__init__()
        self.horns = 2
        self.color = "Black"
        self.voice = "Mooo"

class Camel(herbivores):
    def __init__(self):
        super().__init__()
        self.hump = 1
        self.voice = "Bellow"
        self.neck = "Long"
        self.color = "Ochre"

class Pig(domestic_animal):
    def __init__(self):
        super().__init__()
        self.voice = "Wheek"
        self.earposition = "Top"
        self.mouthshape = "Nuzzle"
        self.color = "Pink"

class Giraffe(herbivores):
    def __init__(self):
        super().__init__()
        self.height = "Tall"
        self.voice = "Snore"
        self.neck = "Long"
        self.color = "Yellow"
        self.dots = "Present"

class Albatross(wild_animal):
    def __init__(self):
        super().__init__()
        self.beak = "Long beak"
        self.wing = "Large"
        self.color = "Black White Grey"
        self.tail = 0
        self.legs = 2
        self.nose = 0
        self.ears = 0

    def __del__(self):
        print("Even you Brutus!!!\n")

a1 = Albatross()