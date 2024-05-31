########################
# How to Create a List #
########################
# Create empty list
# First attempt
output = list() # []

# Second attempt
output = [] # []

# Assign values
fruits = list()
fruits[:] = ['banana', 'orange', 'mango', 'lemon']

vegetables = list(['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'])

print('Fruits:', fruits)
print('Number of fruits {}'.format(len(fruits)))

print('Vegetables', vegetables)
print('Number of vegetables {}'.format(len(vegetables)))

# Lists can have items of different data types
zouhair = ['Zouhair', 11, True, {'country': 'Morocco', 'city': 'Sale'}]
print(zouhair)

# Accessing list items
fruits = ['banana', 'orange', 'mango', 'lemon']
output = fruits[0] # 'banana'
output = fruits[len(fruits) - 1] # 'lemon'
output = fruits[-1] # 'lemon'

# Or I can reverse it first, then take the first which is the last one
output = fruits[::-1][0]

# returns an iterator, specifically a list_reverseiterator object, rather than a list. 
# This iterator can be used to iterate over the elements of the list in reverse order, 
# but it is not directly a list itself.
# So to solve this, convert the reversed iterator into a list using the list() constructor.
output = list(reversed(fruits))[0] # lemon

# In case you want just the first(which the last) item, not the entire reversed list
output = next(reversed(fruits)) # lemon


########################
# Unpacking List Items #
########################
# First example
first_item, second_item, *rest = ['item1','item2','item3', 'item4', 'item5']
output = first_item # item1
output = second_item # item2
output = rest # ['item3', 'item4', 'item5']


# Second example
first, second, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output = first  # 1
output = second # 2
output = rest  	# [3, 4, 5, 6, 7, 8, 9]
output = tenth 	# 10

# Third example
first, _, third, *rest, ninth, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output = first # 1
output = third # 3
output = rest  # [4, 5, 6, 7, 8]
output = ninth # 9
output = tenth # 10


#############################
# Slicing Items from a List #
#############################
# Positive Indexing: We can specify a range of positive indexes by specifying:
# the start, end and step, the return value will be a new list. 
# (default values for start = 0, end = len(lst) - 1 (last item), step = 1)
fruits = ['banana', 'orange', 'mango', 'lemon']
output = fruits[0:] # ['banana', 'orange', 'mango', 'lemon']
output = fruits[0:len(fruits) - 1] # ['banana', 'orange', 'mango', 'lemon']
output = fruits[::1] # ['banana', 'orange', 'mango', 'lemon']

# here we used a 3rd argument, step. It will take every 2cnd item
output = fruits[::2] # ['banana', 'mango']

# Negative Indexing: We can specify a range of negative indexes by specifying:
# the start, end and step, the return value will be a new list.
output = fruits[-1:] # ['lemon']
output = fruits[-4:] # ['banana', 'orange', 'mango', 'lemon']
output = fruits[-3:-1] # ['orange', 'mango']

# a negative step will take the list in reverse order
output = fruits[::-1] # ['lemon', 'mango', 'orange', 'banana']
output = fruits[::-2] # ['lemon', 'orange']


###################
# Modifying Lists #
###################
# List is a mutable or modifiable ordered collection of items. Lets modify the fruit list.
fruits = ['banana', 'orange', 'mango', 'lemon']

fruits[0] = 'avocado'
output = fruits # ['avocado', 'orange', 'mango', 'lemon']

fruits[len(fruits) - 1] = 'lime'
output = fruits # ['avocado', 'orange', 'mango', 'lime']

fruits[-1] = 'strawberry'
output = fruits # ['avocado', 'orange', 'mango', 'strawberry']


############################
# Checking Items in a List #
############################
fruits = ['banana', 'orange', 'mango', 'lemon']

output = 'banana' in fruits # True
output = 'pear' in fruits # False


##########################
# Adding Items to a List #
##########################
fruits = ['banana', 'orange', 'mango', 'lemon']

fruits.append('apple')
output = fruits # ['banana', 'orange', 'mango', 'lemon', 'apple']


###############################
# Inserting Items into a List #
###############################
# We can use insert() method to insert a single item at a specified index in a list. 
# Note that other items are shifted to the right. 
# The insert() methods takes two arguments:index and an item to insert.
fruits = ['banana', 'orange', 'mango', 'lemon']

# insert apple between orange and mango
fruits.insert(2, 'apple')
output = fruits # ['banana', 'orange', 'apple', 'mango', 'lemon']

# insert lime between apple and mango
fruits.insert(3, 'lime') # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']


##############################
# Removing Items from a List #
##############################
# The remove method removes a specified item from a list
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']

fruits.remove('banana') # returns None
output = fruits # ['orange', 'mango', 'lemon', 'banana']


############################
# Removing Items Using Pop #
############################
# The pop() method removes the specified index, (or the last item if index is not specified):
fruits = ['banana', 'orange', 'mango', 'lemon']

fruits.pop() # returns element was popped off: lemon
output = fruits # ['banana', 'orange', 'mango']

output = fruits.pop(0) # 'banana'
output = fruits # ['orange', 'mango']


############################
# Removing Items Using Del #
############################
# The del keyword removes the specified index and it can also be used to delete items within index range. 
# It can also delete the list completely
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']

del fruits[0]
output = fruits # ['orange', 'mango', 'lemon', 'kiwi', 'lime']

del fruits[0:3]
output = fruits # ['kiwi', 'lime']

del fruits
# output = fruits # error: NameError: name 'fruits' is not defined


#######################
# Clearing List Items #
#######################
# The clear() method empties the list:
fruits = ['banana', 'orange', 'mango', 'lemon']

output = fruits.clear() # returns None
output = fruits # []


##################
# Copying a List #
##################
# It is possible to copy a list by reassigning it to a new variable in the following way: list2 = list1. 
# Now, list2 is a reference of list1, any changes we make in list2 will also modify the original, list1. 
# But there are lots of case in which we do not like to modify the original instead 
# we like to have a different copy. One of way of avoiding the problem above is using copy().
fruits = ['banana', 'orange', 'mango', 'lemon']

fruits_copy = fruits.copy()
output = fruits_copy # ['banana', 'orange', 'mango', 'lemon']


#################
# Joining Lists #
#################
# There are several ways to join, or concatenate, two or more lists in Python.
# Plus Operator (+)
positive_numbers = [1, 2, 3]
null = [0]
negative_numbers = [-1, -2, -3]

output = negative_numbers + null + positive_numbers # [-1, -2, -3, 0, 1, 2, 3]

# Joining using extend() method The extend() method allows to append list in a list. See the example below.
num1 = [1, 2, 3]
num2 = [4, 5, 6]

output = num1.extend(num2) # returns None
output = num1 # [1, 2, 3, 4, 5, 6]


############################
# Counting Items in a List #
############################
# The count() method returns the number of times an item appears in a list:
ages = [22, 19, 24, 25, 26, 24, 25, 24]
output = 'Hello'.count('l') # 2

output = ages.count(24) # 3
output = ages.count('24') # 0


############################
# Finding Index of an Item #
############################
# The index() method returns the index of an item in the list:
ages = [22, 19, 24, 25, 26, 24, 25, 24]

output = ages.index(24) # 2, the first occurrence 


####################
# Reversing a List #
####################
# The reverse() method reverses the order of a list.
fruits = ['banana', 'orange', 'mango', 'lemon']

# Will mutate the original list
fruits.reverse()
output = fruits # ['lemon', 'mango', 'orange', 'banana']

# Will NOT mutate the original list
# But we have to convert it back from list_reverseiterator to list: list
output = list(reversed(fruits)) # ['banana', 'orange', 'mango', 'lemon']
output = fruits # ['lemon', 'mango', 'orange', 'banana']

######################
# Sorting List Items #
######################
# To sort lists we can use sort() method or sorted() built-in functions. 
# The sort() method reorders the list items in ascending order and modifies the original list. 
# If an argument of sort() method reverse is equal to true, it will arrange the list in descending order.

# sort(): this method modifies the original list
fruits = ['banana', 'orange', 'mango', 'lemon']

# Ascending
fruits.sort() # returns None
output = fruits # ['banana', 'lemon', 'mango', 'orange']

numbers = [1, 2, 3, 4, 5]

# Descending
numbers.sort(reverse=True)
output = numbers # [5, 4, 3, 2, 1]


# sorted(): returns the ordered list without modifying the original list Example:
fruits = ['banana', 'orange', 'mango', 'lemon']

# Ascending
output = sorted(fruits) # ['banana', 'lemon', 'mango', 'orange']

# Remain unchanged
output = fruits # ['banana', 'orange', 'mango', 'lemon']


# Descending
output = sorted(fruits, reverse=True) # ['orange', 'mango', 'lemon', 'banana']
output = fruits # ['banana', 'orange', 'mango', 'lemon']



print(output)
