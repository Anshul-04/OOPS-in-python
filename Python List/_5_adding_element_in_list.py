# Append item at the end of the list

# The append() method will accept only one parameter and add it at the end of the list.

list1 = [5,8,'Tom',True]

# Using append()
list1.append('Emma')
print(list1)
# Output[5, 8, 'Tom', True, 'Emma']

# append the nested list at the end
list1.append([25, 50, 75])
print(list1)
#Output [5, 8, 'Tom', True, 'Emma', [25, 50, 75]]

#--------------------------------------------------------------------------------------------------------#

# Add item at the specified position in the list
'''
Use the insert() method to add the object/item at the specified position in the list. 
The insert method accepts two parameters position and object.

synatx : insert(index, object)

'''
my_list = list([5, 8, 'Tom', 7.50])

# Using insert()
# insert 25 at position 2
my_list.insert(2, 25)
print(my_list)
# Output [5, 8, 25, 'Tom', 7.5]

# insert nested list at at position 3
my_list.insert(3, [25, 50, 75])
print(my_list)
# Output [5, 8, 25, [25, 50, 75], 'Tom', 7.5]

#--------------------------------------------------------------------------------------------------------#
'''
# Using extend()

The extend method will accept the list of elements and add them at the end of the list. 
We can even add another list by using this method.
'''

my_list1 = list([5, 8, 'Tom', 7.50])

# Using extend()
my_list1.extend([25, 75, 100])
print(my_list1)
# Output [5, 8, 'Tom', 7.5, 25, 75, 100]