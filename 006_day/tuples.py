####################
# Creating a Tuple #
####################
# Empty tuple: Creating an empty tuple
# First attempt
empty_tuple = ()
output = empty_tuple # ()

# Second attempt
empty_tuple = tuple()
output = empty_tuple # ()

# Tuple with initial values
fruits = ('banana', 'orange', 'mango', 'lemon')
output = fruits # ('banana', 'orange', 'mango', 'lemon')


################
# Tuple length #
################
# We use the len() method to get the length of a tuple.
output = len(fruits) # 4


#########################
# Accessing Tuple Items #
#########################
# Similar to the list data type we use positive or negative indexing to access tuple items.
first = fruits[0] # banana
last = fruits[len(fruits) - 1] # lemon
last = fruits[-1] # lemon
reversed_fruits = fruits[::-1] # ('lemon', 'mango', 'orange', 'banana')
print(fruits.index('orange')) # 1
print(fruits.count('pear'))   # 0


##################
# Slicing tuples #
##################
# We can slice out a sub-tuple by specifying a range of indexes where to start and where to end 
# in the tuple, the return value will be a new tuple with the specified items.
# Range of Positive Indexes
fruits = ('banana', 'orange', 'mango', 'lemon')

all_fruits = fruits[0:4] 	# ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:] 	# ('banana', 'orange', 'mango', 'lemon')
orange_mango = fruits[1:3] 	# ('orange', 'mango')

# Range of Negative Indexes
fruits = ('banana', 'orange', 'mango', 'lemon')

all_fruits = fruits[-4:] 	# ('banana', 'orange', 'mango', 'lemon')
orange_mango = fruits[-3:-1] # ('orange', 'mango')


############################
# Changing Tuples to Lists #
############################
# We can change tuples to lists and lists to tuples. Tuple is immutable if we want to modify a tuple
# we should change it to a list.
# From a tuple to a list
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
output = fruits # ['banana', 'orange', 'mango', 'lemon']

# From a list to a tuple
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
output = fruits # ('banana', 'orange', 'mango', 'lemon')


###############################
# Checking an Item in a Tuple #
###############################
# We can check if an item exists or not in a tuple using in, it returns a boolean.
output = 'orange' in fruits # True
output = 'apple' in fruits  # False

# fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment


##################
# Joining Tuples #
##################
# We can join two or more tuples using + operator
fruits = ('banana', 'orange')
vegetables = ('Cabbage', 'Carrot')

fruits_and_vegetables = fruits + vegetables
output = fruits_and_vegetables # ('banana', 'orange', 'Cabbage', 'Carrot')


###################
# Deleting Tuples #
###################
# It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself 
# using del.
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
# output = fruits # error: NameError: name 'fruits' is not defined



print(output)
