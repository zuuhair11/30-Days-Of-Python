##################
# Creating a Set #
##################
# Creating an empty set
st = set()
print(st) # set()

# Creating a set with initial items
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits) # {'banana', 'orange', 'mango', 'lemon'}


########################
# Getting Set's Length #
########################
# We use len() method to find the length of a set
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits)) # 4


############################
# Accessing Items in a Set #
############################
# We use loops to access items. We will see this in loop section
for item in fruits:
	print(item)


####################
# Checking an Item #
####################
# To check if an item exist in a list we use in membership operator.
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('Does set fruits contains orange:', 'orange' in fruits) # Does set fruits contains orange: True


#########################
# Adding Items to a Set #
#########################
# Once a set is created we cannot change any items and we can also add additional items.
fruits = {'banana', 'orange', 'mango', 'lemon'}

# Add one item using add()
fruits.add('lime')
print(fruits) # {'lemon', 'lime', 'mango', 'banana', 'orange'}

# Add multiple items using update() The update() allows to add multiple items to a set. 
# The update() takes a list argument
fruits.update(['10', '20'])
print(fruits) # {'20', 'banana', 'lemon', 'orange', '10', 'mango', 'lime'}

fruits.update(('30', '40'))
print(fruits) # {'20', 'orange', 'mango', 'lemon', '40', 'banana', '30', '10', 'lime'}

fruits.update('abc')
print(fruits) # {'lime', 'c', '20', '40', 'a', '10', '30', 'mango', 'banana', 'b', 'orange', 'lemon'}


#############################
# Removing Items from a Set #
#############################
# We can remove an item from a set using remove() method. If the item is not found remove() method 
# will raise errors, so it is good to check if the item exist in the given set. 
# However, discard() method doesn't raise any errors.
fruits = {'banana', 'orange', 'mango', 'lemon'}

fruits.remove('orange')
print(fruits) # {'banana', 'mango', 'lemon'}

# fruits.discard('orange') # Ok
# fruits.remove('orange')  # Error


# The pop() methods remove a random item from a list and it returns the removed item.
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()
print(fruits) # {'mango', 'orange', 'lemon'}

# If we are interested in the removed item.
removed_item = fruits.pop()
print(removed_item) # orange


###########################
# Clearing Items in a Set #
###########################
# If we want to clear or empty the set we use clear method.
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()


##################
# Deleting a Set #
##################
# If we want to delete the set itself we use del operator.
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
# print(fruits) # error: NameError: name 'fruits' is not defined


##########################
# Converting List to Set #
##########################
# We can convert list to set and set to list. Converting list to set removes duplicates 
# and only unique items will be reserved.
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
print(fruits) # ['banana', 'orange', 'mango', 'lemon', 'orange', 'banana']

# from a list to set
fruits = set(fruits)
print(fruits) # {'orange', 'banana', 'mango', 'lemon'}

# from a set to list
fruits = list(fruits)
print(fruits) # ['orange', 'banana', 'mango', 'lemon']


################
# Joining Sets #
################
fruits = {'banana', 'orange'}
vegetables = {'cabbage', 'carrot'}

# We can join two sets using the union() or update() method.
fv = fruits.union(vegetables)
print(fv) # {'orange', 'carrot', 'cabbage', 'banana'}

# Update This method inserts a set into a given set
fv = fruits.update(vegetables)
print(fv) # None
print(fruits) # {'orange', 'carrot', 'cabbage', 'banana'}


##############################
# Finding Intersection Items #
##############################
# Intersection returns a set of items which are in both the sets.
python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
# same as:
python = set('python')
dragon = set('dragon')

# repeated letter in both python and dragon
all_intersection = python.intersection(dragon)
print(all_intersection) # {'o', 'n'}

# even numbers
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}

evens = whole_numbers.intersection(even_numbers)
print(evens) # {0, 2, 4, 6, 8, 10}


#################################
# Checking Subset and Super Set #
#################################
# A set can be a subset or super set of other sets:
st_1 = {'item1', 'item2', 'item3', 'item4', 'item5'}
st_2 = {'item1', 'item2'}

is_subset = st_1.issubset(st_2)
print(is_subset)	# False

is_superset = st_1.issuperset(st_2)
print(is_superset)	# True

is_subset = st_2.issubset(st_1)
print(is_subset) 	# True

is_superset = st_2.issuperset(st_1)
print(is_superset)	# False

# if they are all equal len({}) == len({}) and have same values
# They all should print True


############################################
# Checking the Difference Between Two Sets #
############################################
# It returns the difference between two sets.
python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}

print(python.difference(dragon)) # {'y', 'h', 't', 'p'}
print(dragon.difference(python)) # {'r', 'g', 'a', 'd'}

print(python.intersection(dragon)) # {'n', 'o'}


#################################################
# Finding Symmetric Difference Between Two Sets #
#################################################
# Finding the symmetric difference between two sets in Python is useful for determining elements that are:
# unique to each set (i.e., elements that are not shared between the two sets).
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}

print(python.symmetric_difference(dragon)) # {'d', 'y', 'p', 'g', 'r', 'a', 'h', 't'}


################
# Joining Sets #
################
# If two sets do not have a common item or items we call them disjoint sets. 
# We can check if two sets are joint or disjoint using isdisjoint() method.
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}

print(python.isdisjoint(dragon)) # False, there are common items {'o', 'n'}
