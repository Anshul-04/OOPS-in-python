'''
To access the elements in the list from left to right, the index value starts from zero to
(length of the list-1) can be used. For example,
if we want to access the 3rd element we need to use 2 since the index value starts from 0.
'''

my_list = [10, 20, 'Jessa', 12.50, 'Emma']

# accessing 2nd element of the list
print(my_list[1])  # 20

# accessing 5th element of the list
print(my_list[4])  # 'Emma'

# Negative Indexing
'''
The elements in the list can be accessed from right to left by using negative indexing.
The negative value starts from -1 to -length of the list. It indicates that the list is indexed
from the reverse/backward.
'''

# accessing last element of the list
print(my_list[-1])
# output 'Emma'

# accessing second last element of the list
print(my_list[-2])
# output 12.5

# accessing 4th element from last
print(my_list[-4])
# output 20