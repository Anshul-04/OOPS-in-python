'''
# Constructor Overloading

  Constructor overloading is a concept of having more than one constructor with a 
  different parameters list in such a way so that each constructor can perform different tasks.

  #Python does not support constructor overloading.

    If we define multiple constructors then,the interpreter will considers only the last constructor 
    and throws an error if the sequence of the arguments doesn’t match as per the last constructor.
'''

# the below code will give  Error

class Student:
    # one argument constructor
    def __init__(self, name):
        print("One arguments constructor")
        self.name = name

    # two argument constructor
    def __init__(self, name, age):
        print("Two arguments constructor")
        self.name = name
        self.age = age

# creating first object
emma = Student('Emma')

# creating Second object
kelly = Student('Kelly', 13)


'''
-> As you can see in the above example, we defined multiple constructors with different arguments.

-> At the time of object creation, the interpreter executed the second constructor because Python 
   always considers the last constructor.

-> Internally, the object of the class will always call the last constructor, even if the class
    has multiple constructors.

-> In the example when we called a constructor only with one argument, we got a type error.


'''