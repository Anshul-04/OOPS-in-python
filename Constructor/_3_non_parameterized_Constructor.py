'''
# Non-Parametrized Constructor

A constructor without any arguments is called a non-parameterized constructor. 
This type of constructor is used to initialize each object with default values.

This constructor doesn’t accept the arguments during object creation. Instead,
 it initializes every object with the same set of values.


'''

class Company:

    # no-argument constructor
    def __init__(self):
        self.name = "PYnative"
        self.address = "ABC Street"

    # a method for printing data members
    def show(self):
        print('Name:', self.name, 'Address:', self.address)

# creating object of the class
cmp = Company()

# calling the instance method using the object
cmp.show()

'''
Note:

-> The default constructor is not present in the source py file. It is inserted into the code during compilation
   if not exists. See the below image.
-> If you implement your constructor, then the default constructor will not be added.
'''