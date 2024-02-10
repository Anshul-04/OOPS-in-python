class Employee:
    #Constructor
    def __init__(self,name:str,salary:int):
          # public data member
        self.name = name 
          # private data member
        self.__salary = salary

    # public instance methods
    def show(self):
        # private members are accessible from a class
        print("Name: ", self.name, 'Salary:', self.__salary)

robin = Employee("Robin",5000)
maya = Employee("Maya",4000)

print(robin.name)
print(robin._Employee__salary)
robin.show()
maya.show()