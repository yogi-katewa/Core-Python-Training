from math import pi

class Circle(object):
    #initialize the variables
    def __init__(self, radius):
        self.radius = radius

    #get Area of Circle
    def getArea(self):
        return (pi*self.radius*self.radius)

    #get Perimeter of Circle
    def getPerimeter(self):
        return (2*pi*self.radius)

#takes input from User
radius = int(input("Enter Radius of Circle : "))
obj = Circle(radius)
print ("Area of Circle : " , obj.getArea())
print ("Perimeter of Circle : " , obj.getPerimeter())
