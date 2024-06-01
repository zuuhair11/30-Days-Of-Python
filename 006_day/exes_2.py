# 1- Unpack siblings and parents from family_members
family_members = ('John', 'John', 'John', 'Jeff', 'Sara')

siblings = family_members[:3]
parents = family_members[3:]
print(siblings) # ('John', 'John', 'John')
print(parents)  # ('Jeff', 'Sara')


# 2- Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'orange')
vegetables = ('Cabbage', 'Carrot')
animal_products = ('product1', 'product2')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp) # ('banana', 'orange', 'Cabbage', 'Carrot', 'product1', 'product2')


# 3- Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt) # ['banana', 'orange', 'Cabbage', 'Carrot', 'product1', 'product2']

# 4- Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_stuff_lt.pop(1)
print(food_stuff_lt) # ['banana', 'Cabbage', 'Carrot', 'product1', 'product2']

food_stuff_tp = food_stuff_tp[:1] + food_stuff_tp[2:]
print(food_stuff_tp) # ('banana', 'Cabbage', 'Carrot', 'product1', 'product2')


# 5- Slice out the first two items and the last two items from food_staff_lt list
del food_stuff_lt[0:2]
del food_stuff_lt[1:]
print(food_stuff_lt) # ['Carrot']

# 6- Delete the food_staff_tp tuple completely
del food_stuff_tp
# print(food_stuff_tp) # error: NameError: name 'food_stuff_tp' is not defined.

# 7- Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# -> Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries) # False

# -> Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries) # True
