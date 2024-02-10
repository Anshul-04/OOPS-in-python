# The list can be created using either the list constructor or using square brackets [].
'''
1.Using list() constructor: In general, the constructor of a class has its class name. 
  Similarly, Create a list by passing the comma-separated values inside the list().

2.Using square bracket ([]): In this method, we can create a list simply by enclosing 
the items inside the square brackets.

'''

# Using list constructor
list1 = list((1,2,3))
print("Creating List using list constructor : ",list1)
# Output [1, 2, 3]

# Using square bracket
list2 = [1,2,3]
print("Creating List using square bracket : ",list2)
# Output [1, 2, 3]

# with heterogeneous items
list3 = [1.0, 'Jessa', 3,False,(1,2,3),[1000,2000]]
print("Creating List with hetrogenous items : ",list3)
# Output [1.0, 'Jessa', 3]

for item in list3:
    print(f"Data type of our list item : ",type(item))

# Create empty list using Constructor 
list4 = list()
print('This is empty list created using constrcutor list():',list4)
# Output []

# Create empty list using square bracket 
list5 = []
print('This is empty list created using constrcutor []:',list5)
# Output []

# Length of a List
print('length of list2 is : ',len(list2))
#Output : 3