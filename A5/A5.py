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
	        self.__tusks = 2
	        
	def get_tusks(self):
		print(f"Tusks = {self.__tusks}")
	def set_tusks(self,tusks):
		self.__tusks = tusks
		
	def __del__(self):
		print("Please help! They want my tusks!")

class Fish(aquatic_animal):
	def __init__(self):
	        super().__init__()
	        self.legs = 0
	        self.tail = 0
	        self.ears = 0
	        self.nose = 0
	        self.nostrils = 2
	        self.__liver = 1
	        self.voice = "Grunt"
	        
	def get_liver(self):
		print(f"Liver = {self.__liver}")
	def set_liver(self,liver):
		self.__liver = liver	
	
	def __del__(self):
		print("Save Me!!!")
		
class Tiger(carnivores):
	def __init__(self):
	        super().__init__()
	        self.strips = "Black"
	        self.color = "Orange"
	        self.voice = "Roar"
	        self.__claws = 20
	        
	def get_claws(self):
		print(f"Claws = {self.__claws}")
	def set_claws(self,claw):
		self.__claws = claw
		
	def __del__(self):
		print("Save Tigers")       

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

init = 1
a1 = Giraffe()

print(a1.height)

emp = Elephant()
emp.set_tusks(0)
emp.get_tusks()

emp = Fish()
emp.get_liver()
