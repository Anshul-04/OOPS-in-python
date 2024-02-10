# List Slicing
'''
Slicing a list implies, accessing a range of elements in a list. For example, if we want to get 
the elements in the position from 3 to 7, we can use the slicing method.

synatx : listname[start_index : end_index : step]

1.The start_index denotes the index position from where the slicing should begin and 
  the end_index parameter denotes the index positions till which the slicing should be done.

2.The step allows you to take each nth-element within a start_index:end_index range

'''

my_list = [10, 20, 'Jessa', 12.50, 'Emma', 25, 50]

# Extracting a portion of the list from 2nd till 5th element
print(my_list[2:5])
# Output ['Jessa', 12.5, 'Emma']

# slice first four items
print(my_list[:4])
# Output [10, 20, 'Jessa', 12.5]

# print every second element
# with a skip count 2
print(my_list[::2])
# Output [10, 'Jessa', 'Emma', 50]

# reversing the list
print(my_list[::-1])
# Output [50, 25, 'Emma', 12.5, 'Jessa', 20, 10]

# Without end_value
# Stating from 3nd item to last item
print(my_list[3:])
# Output [12.5, 'Emma', 25, 50]