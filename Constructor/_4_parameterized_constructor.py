'''
# Parameterized Constructor

  A constructor with defined parameters or arguments is called a parameterized constructor.
  We can pass different values to each object at the time of creation using a parameterized constructor.

  The first parameter to constructor is self that is a reference to the being constructed,
  and the rest of the arguments are provided by the programmer. A parameterized constructor can have
  any number of arguments.

'''

class Employee:
    # parameterized constructor
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    # display object
    def show(self):
        print(self.name, self.age, self.salary)

# creating object of the Employee class
emma = Employee('Emma', 23, 7500)
emma.show()

kelly = Employee('Kelly', 25, 8500)
kelly.show()