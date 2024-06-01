# 1- Create an empty tuple
# First attempt
empty_tuple = ()

# Second attempt
empty_tuple = tuple()
print(empty_tuple) # ()


# 2- Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# First attempt
names = ('Zouhair', 'Zouhair', 'Zouhair')

# Second attempt
names = tuple(('Zouhair', 'Zouhair', 'Zouhair'))

# Third attempt
names = tuple(['Zouhair', 'Zouhair', 'Zouhair'])
print(names) # ('Zouhair', 'Zouhair', 'Zouhair')

# 3- Join brothers and sisters tuples and assign it to siblings
siblings = ('John', 'John', 'John')
all_names = names + siblings
print(all_names) # ('Zouhair', 'Zouhair', 'Zouhair', 'John', 'John', 'John')

# 4- How many siblings do you have?
length = len(siblings)
print(length) # 3

# 5- Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = siblings + tuple(('Jeff', 'Sara'))
family_members = siblings
print(family_members) # ('John', 'John', 'John', 'Jeff', 'Sara')
