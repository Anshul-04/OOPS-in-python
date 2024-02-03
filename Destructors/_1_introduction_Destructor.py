import time
'''
The destructor is the reverse of the constructor. The constructor is used to initialize objects,
while the destructor is used to delete or destroy the object that releases the resource occupied by
the object.

In Python, destructor is not called manually but completely automatic. destructor gets called in the 
following two cases
 1. When an object goes out of scope or
 2. The reference counter of the object reaches 0.

In Python, The special method __del__() is used to define a destructor. 

'''

class Student:

    # constructor
    def __init__(self, name):
        print('Inside Constructor')
        self.name = name
        print('Object initialized')

    def show(self):
        print('Hello, my name is', self.name)

    # destructor
    def __del__(self):
        print('Inside destructor')
        print('Object destroyed')

# create object
s1 = Student('Emma')
# create new reference
# both reference points to the same object
s2 = s1
s1.show()

# delete object reference s1
del s1

# add sleep and observe the output
time.sleep(5)
print('After sleep')
s2.show()

'''
Points to Remember about Destructor

  1. The __del__ method is called for any object when the reference count for that object becomes zero.

  2. The reference count for that object becomes zero when the application ends, or we delete all references 
    manually using the del keyword.
    
  3. The destructor will not invoke when we delete object reference. It will only invoke when all references 
    to the objects get deleted.
  
'''