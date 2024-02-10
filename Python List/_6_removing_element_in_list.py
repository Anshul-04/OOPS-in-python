# Removing elements from a List

''' 
# Remove specific item

  Use the remove() method to remove the first occurrence of the item from the list.   

Note:  It Throws a keyerror if an item not present in the original list.
'''

my_list = list([2, 4, 6, 8, 10, 12])

# remove item 6
my_list.remove(6)
# remove item 8
my_list.remove(8)

print(my_list)
# Output [2, 4, 10, 12]

# Remove all occurrence of a specific item
# Use a loop to remove all occurrence of a specific item

my_list1 = list([6, 4, 6, 6, 8, 12])

for item in my_list1:
    my_list1.remove(6)

print(my_list1)
# Output [4, 8, 12]

"""
# Remove item present at given index
  Use the pop() method to remove the item at the given index. The pop() method removes and
  returns the item present at the given index.

Note: It will remove the last time from the list if the index number is not passed.
"""
my_list2 = list([2, 4, 6, 8, 10, 12])

# remove item present at index 2
my_list2.pop(2)
print(my_list2)
# Output [2, 4, 8, 10, 12]

# remove item without passing index number
my_list2.pop()
print(my_list2)
# Output [2, 4, 8, 10]

'''
#Remove the range of items
  Use del keyword along with list slicing to remove the range of items
'''

my_list3 = list([2, 4, 6, 8, 10, 12])

# remove range of items
# remove item from index 2 to 5
del my_list3[2:5]
print(my_list3)
# Output [2, 4, 12]

# remove all items starting from index 3

del my_list3[3:]
print(my_list3)
# Output [2, 4, 6]

'''
#Remove all items
  Use the list clear() method to remove all items from the list. The clear() method truncates the list.
'''

my_list4 = list([2, 4, 6, 8, 10, 12])

# clear list
my_list4.clear()
print(my_list4)
# Output []

# Delete entire list
del my_list4