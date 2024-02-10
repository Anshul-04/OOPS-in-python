# Abstract classes are incomplete because they have methods that have nobody. 
# If Python allows creating an object for abstract classes then using that object if 
# anyone calls the abstract method, but there is no actual implementation to invoke.

'''
An abstract class can be considered a blueprint for other classes.
It allows you to create a set of methods that must be created within any child classes built from
the abstract class.

A class that contains one or more abstract methods is called an abstract class.
An abstract method is a method that has a declaration but does not have an implementation.
'''
from abc import ABC,abstractmethod

class Polygon(ABC):
    
    @abstractmethod
    def number_of_sides(self):
        pass
    
class Triangle(Polygon):
    def number_of_sides(self):
        print('I have 3 sides')

class Square(Polygon):
    def number_of_sides(self):
        print('I have 4 sides')

class Hexagon(Polygon):
    def number_of_sides(self):
        print('I have 6 sides')


triangle = Triangle()
triangle.number_of_sides()

square = Square()
square.number_of_sides()

hex = Hexagon()
hex.number_of_sides()