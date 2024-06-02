# Exercises: Level 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1- Find the length of the set it_companies
print(len(it_companies)) # 7

# 2- Add 'Twitter' to it_companies
it_companies.add('Twitter')
it_companies.update(['X'])
print(it_companies) # {'Apple', 'Microsoft', 'Oracle', 'X', 'Facebook', 'IBM', 'Amazon', 'Google', 'Twitter'}

# 3- Insert multiple IT companies at once to the set it_companies
it_companies.update(['ELEVEN', 'Z'])
print(it_companies) # {'Z', 'Apple', 'Twitter', 'ELEVEN', 'Oracle', 'IBM', 'Amazon', 'Google', 'Facebook', 'X', 'Microsoft'}

# 4- Remove one of the companies from the set it_companies
it_companies.pop()
print(it_companies) # {'Amazon', 'Facebook', 'X', 'Oracle', 'IBM', 'Microsoft', 'Z', 'Apple', 'ELEVEN', 'Twitter'}

# 5- What is the difference between remove and discard
# If we use remove to get ride of an item, and that item does not exist, will raise an error
# If we use discard to get ride of an item, and that item does not exist, it's okay than


##########################
# pop - remove - discard #
##########################
items = {'item1', 'item2', 'item3', 'item4', 'item5'}

# Using pop: delete random item, return it
removed_item = items.pop()
print(items) # {'item2', 'item3', 'item1', 'item4'}
print(removed_item) # item5

# Using remove: delete an item, return None | raise an error if the item trying to remove not exist
removed_item = items.remove('item2')
print(items) 		# {'item3', 'item1', 'item5', 'item4'}
print(removed_item)	# None

# Using discard: delete an item, return None | does NOT raise an error if the item trying to remove not exist
removed_item = items.discard('item2')
print(items) # {'item3', 'item4', 'item1', 'item5'}
print(removed_item) # None
