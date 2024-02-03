
'''
# What is Constructor in Python?
  In object-oriented programming, A constructor is a special method used to create and initialize an object of a class. 
  This method is defined in the class. 

  The constructor is executed automatically at the time of object creation.
  The primary use of a constructor is to declare and initialize data member/ instance variables of a class.
  The constructor contains a collection of statements (i.e., instructions) that executes at the time of object creation to
  initialize the attributes of an object.
  
'''
# In Python, Object creation is divided into two parts in Object Creation and Object initialization

# Internally, the __new__ is the method that creates the object
# And, using the __init__() method we can implement constructor to initialize the object.


class Student:
        
    def __init__(self):
        print('I am created inside Constructor')
      
student1 = Student()

'''
  Note:

  # For every object, the constructor will be executed only once. For example,
    if we create four objects, the constructor is called four times.

  # In Python, every class has a constructor, but it’s not required to define it explicitly.
   Defining constructors in class is optional.

  # Python will provide a default constructor if no constructor is defined.
'''