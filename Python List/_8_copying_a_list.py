'''
#Using assignment operator (=)
  This is a straightforward way of creating a copy. In this method, the new list will be a deep copy. 
  The changes that we make in the original list will be reflected in the new list.

This is called deep copying.
'''

my_list1 = [1, 2, 3]

# Using = operator
new_list = my_list1
# printing the new list
print(new_list)
# Output [1, 2, 3]

# making changes in the original list
my_list1.append(4)

# print both copies
print(my_list1)
# result [1, 2, 3, 4]
print(new_list)
# result [1, 2, 3, 4]

'''
Note: 
  When you set list1 = list2, you are making them refer to the same list object, 
  so when you modify one of them, all references associated with that object reflect the 
  current state of the object. So don’t use the assignment operator to copy the dictionary 
  instead use the copy() method
'''

"""
#Using the copy() method
  The copy method can be used to create a copy of a list. This will create a new list and 
  any changes made in the original list will not reflect in the new list. This is shallow copying.
"""

my_list2 = [1, 2, 3]

# Using copy() method
new_list = my_list2.copy()
# printing the new list
print(new_list)
# Output [1, 2, 3]

# making changes in the original list
my_list2.append(4)

# print both copies
print(my_list2)
# result [1, 2, 3, 4]
print(new_list)
# result [1, 2, 3]