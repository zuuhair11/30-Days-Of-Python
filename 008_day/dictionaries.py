import pprint
################
# Dictionaries #
################
# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.
# Creating a Dictionary
# To create a dictionary we use curly brackets, {} or the dict() built-in function.
empty_dict = dict()
empty_dict = {}
print(empty_dict) # {}

###########
# Example #
###########
person = {
	'first_name': 'Zouhair',
	'last_name': 'Sahtout',
	'age': 27,
	'country': 'Morocco',
	'is_married': False,
	'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
	'address': {
		'street': 'Localhost',
		'zipcode': '11 ELEVEN'
	}
}


#####################
# Dictionary Length #
#####################
print(len(person)) # 7


##############################
# Accessing Dictionary Items #
##############################
print(person['first_name']) # Zouhair
print(person['address']) 	# {'street': 'Localhost', 'zipcode': '11 ELEVEN'}
print(person['address']['zipcode']) # 11 ELEVEN
# print(person['foo']) # KeyError: 'foo' << =================================


########
# NOTE #
########
# Accessing an item by key name raises an error if the key does not exist. 
# To avoid this error first we have to check if a key exist or we can use the get method. 
# The get method returns None, which is a NoneType object data type, if the key does not exist.
print(person.get('foo')) # None
print(person.get('age')) # 27


################################
# Adding Items to a Dictionary #
################################
# We can add new key and value pairs to a dictionary
person['job_title'] = 'Software Developer'
person['skills'].append('HTML')
print(person.get('skills')) # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python', 'HTML']


###################################
# Modifying Items in a Dictionary #
###################################
# We can modify items in a dictionary
person.get('skills')[0] = 'I love JavaScript'
print(person['skills']) # ['I love JavaScript', 'React', 'Node', 'MongoDB', 'Python', 'HTML']


#################################
# Checking Keys in a Dictionary #
#################################
# We use the in operator to check if a key exist in a dictionary
print('last_name' in person) # True
if 'last_name' in person:
	print('"%s" deleted successfully' % person.get('last_name'))
	del person['last_name']


##################################################
# Removing Key and Value Pairs from a Dictionary #
##################################################
# pop(key): removes the item with the specified key name:
# will raise an error if the key name does not exist
person.pop('country')

# popitem(): removes the last item
person.popitem()

# del: removes an item with specified key name
del person['address']


##########################################
# Changing Dictionary to a List of Items #
##########################################
# The items() method changes dictionary to a list of tuples.
dct = {
	'key1': 'value1',
	'key2': 'value2',
	'key3': 'value3',
}

lst_of_tuples = dct.items()
print(lst_of_tuples) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])

lst_of_tuples = list(dct.items())
print(lst_of_tuples) # [('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')]


#########################
# Clearing a Dictionary #
#########################
# If we don't want the items in a dictionary we can clear them using clear() method
dct = {
	'key1': 'value1',
	'key2': 'value2',
	'key3': 'value3',
}

dct.clear()
print(dct) # {}


#########################
# Deleting a Dictionary #
#########################
# If we do not use the dictionary we can delete it completely
dct = {
	'key1': 'value1',
	'key2': 'value2',
	'key3': 'value3',
}

del dct
# print(dct) # NameError: name 'dct' is not defined.


#####################
# Copy a Dictionary #
#####################
# We can copy a dictionary using a copy() method. Using copy we can avoid mutation of the original dictionary.
dct = {
	'key1': 'value1',
	'key2': 'value2',
	'key3': 'value3',
}

dct_copy = dct.copy()
print(dct_copy) # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}


#####################################
# Getting Dictionary Keys as a List #
#####################################
# The keys() method gives us all the keys of a a dictionary as a list.
keys = list(dct.keys())
print(keys) # ['key1', 'key2', 'key3']


#######################################
# Getting Dictionary Values as a List #
#######################################
# The values method gives us all the values of a a dictionary as a list.
values = list(dct.values())
print(values) # ['value1', 'value2', 'value3']
