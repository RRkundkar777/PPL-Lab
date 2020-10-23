import turtle

class shape:
    def info(self):
        print( "In Mathematics, a shape may be defined as Outline of something.\n")

class polygon(shape):
    def __init__(self, sides, length) :
        self.sides = sides
        self.length = length
    
    def show(self):
        pen = turtle.Turtle()
        angle = 360/self.sides
        for i in range(self.sides):
            pen.forward(self.length)
            pen.right(angle)

class triangle(polygon):
    def __init__(self,length):
        super().__init__(3,length)

class square(polygon):
    def __init__(self,length):
        super().__init__(4,length)

        
class pentagon(polygon):
    def __init__(self,length):
        super().__init__(5,length)    

class hexagon(polygon):
    def __init__(self,length):
        super().__init__(6,length)

class septagon(polygon):
    def __init__(self,length):
        super().__init__(7,length)

class octagon(polygon):
    def __init__(self,length):
        super().__init__(8,length)

class nonagon(polygon):
    def __init__(self,length):
        super().__init__(9,length)

class decagon(polygon):
    def __init__(self,length):
        super().__init__(10,length)

class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    
    def show(self):
        len = 2*(3.14)*(self.radius)*120/144
        pen = turtle.Turtle()
        for i in range(72):
            pen.right(5)
            pen.forward(len)


c1 = circle(3)
c1.show()
poly1 = polygon(11,100)
plot1 = triangle(250)
poly1.show()
plot1.show()







