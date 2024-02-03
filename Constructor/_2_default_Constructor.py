'''
# Default Constructor

Python will provide a default constructor if no constructor is defined. 
Python adds a default constructor when we do not include the constructor in the class or forget to
declare it. It does not perform any task but initializes the objects. 
It is an empty constructor without a body.
'''

class Employee:

    def display(self):
        print('Inside Display')

emp = Employee()
emp.display()

'''
Note:

-> The default constructor is not present in the source py file. It is inserted into the code during compilation
   if not exists. See the below image.
-> If you implement your constructor, then the default constructor will not be added.
'''