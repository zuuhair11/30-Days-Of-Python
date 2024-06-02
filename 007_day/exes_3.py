# Exercises: Level 3
ages = [22, 19, 24, 25, 26, 24, 25, 24]

# 1- Convert the ages to a set and compare the length of the list and the set, which one is bigger?
# Convert to a set
ages_st = set(ages)

# Compare the length - list length is bigger because it has duplicates
print('Length of the ages list: %d' %(len(ages)))			# 8
print('Length of the ages set: {}'.format(len(ages_st))) 	# 5


# 2- Explain the difference between the following data types: string, list, tuple and set
# String
# A string is a sequence of characters, accessible by index starting from 0.
# Strings are immutable, meaning they cannot be changed after creation.

# List
# A list is a mutable collection of ordered elements, accessible by index starting from 0.
# Lists can be modified, with elements added, removed, or changed.

# Tuple
# A tuple is an immutable collection of ordered elements, accessible by index starting from 0.
# Tuples cannot be modified once created.

# Set
# A set is a mutable collection of unique, unordered values, not accessible by index.
# Sets can be modified, with elements added or removed, but they do not support indexing.


# 3- How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'

all_words = sentence.split(' ')
unique_words = set(all_words)

print(len(all_words))		# 12
print(len(unique_words))	# 10
