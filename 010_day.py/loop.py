#########
# Loops #
#########
# Life is full of routines. In programming we also do lots of repetitive tasks. 
# In order to handle repetitive task programming languages use loops. 
# Python programming language also provides the following types of two loops:
# 1- while loop
# 2- for loop

##############
# While Loop #
##############
# We use the reserved word while to make a while loop. 
# It is used to execute a block of statements repeatedly until a given condition is satisfied. 
# When the condition becomes false, the lines of code after the loop will be continued to be executed.
count = 0
while count < 5:
	print(count)
	count = count + 1

# => print from 0 to 4


# In the above while loop, the condition becomes false when count is 5. 
# That is when the loop stops. 
# If we are interested to run block of code once the condition is no longer true, we can use else.
count = 0
while count < 5:
	print(count)
	count = count + 1
else:
	print('{}, done!'.format(count))

# => print from 0 to 5, done!
# The above loop condition will be false when count is 5 and the loop stops, and execution starts 
# the else statement. As a result 5 will be printed.


###############################
# Break and Continue - Part 1 #
###############################
# Break: We use break when we like to get out of or stop the loop.
count = 0
while count < 5:
	print(count)
	count = count + 1

	if count == 3:
		break

# => print from 0 to 2, because when it reaches it stops

# Continue: With the continue statement we can skip the current iteration, and continue with the next:
count = 0
while count < 5:
	if count == 3:
		count = count + 1
		continue

	print(count)
	count = count + 1

# => print from 0 to 4 but (skips 3)


############
# For Loop #
############
# A for keyword is used to make a for loop, similar with other programming languages, but with some
# syntax differences. 
# Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# For loop with list
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
	print(number) 	   # the numbers will be printed line by line, from 0 to 5


# For loop with string
language = 'Python'
for letter in language:
	print(letter)

for i in range(len(language)):
	print(language[i].upper())


# For loop with tuple
numbers = tuple(numbers)
for number in numbers:
	print(number)


# For loop with dictionary Looping through a dictionary gives you the key of the dictionary.
person = {
    'first_name':'Zouhair',
    'last_name':'Sahtout',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key in person:
	print(person[key])

for key, value in person.items():
	print('%s: %s' % (key, value))


# Loops in set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
	print(company)


###############################
# Break and Continue - Part 2 #
###############################
# Short reminder: Break: We use break when we like to stop our loop before it is completed.
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
	print(number)
	if number == 3:
		continue

	print('Next number shoud be', number + 1) if number != 5 else print('loop\'s end')
print('Outside the loop')


######################
# The Range Function #
######################
# The range() function is used list of numbers. The range(start, end, step) takes three parameters: 
# starting, ending and increment. 
# By default it starts from 0 and the increment is 1. 
# The range sequence needs at least 1 argument (end). Creating sequences using range
rng = range(5)
print(rng) # range(0, 5)

lst = list(range(5))
print(lst) # [0, 1, 2, 3, 4]

st = set(range(1, 6))
print(st)  # {1, 2, 3, 4, 5}

evens = list(range(0, 11, 2))
print(evens) # [0, 2, 4, 6, 8, 10]

st = set(range(0, 11, 2))
print(st) # {0, 2, 4, 6, 8, 10}

# Example
for i in range(2, 12, 3):
	print('eleven' if i == 11 else i)

# => 2, 5, 8, eleven


###################
# Nested For Loop #
###################
# We can write loops inside a loop.
person = {
    'first_name': 'Zouhair',
    'last_name': 'Sahtout',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for key in person:
	if key == 'skills':
		for skill in person[key]:
			print(skill)

# => JavaScript React Node MongoDB Python


############
# For Else #
############
# If we want to execute some message when the loop ends, we use else.
for number in range(12):
	print(number) # prints 0 to 11, not including 12
else:
	print('The loop stops at', number) # 11


########
# Pass #
########
# In python when statement is required (after semicolon), but we don't like to execute any code there, 
# we can write the word pass to avoid errors. 
# Also we can use it as a placeholder, for future statements.
for number in range(6):
	pass

# => will not execute anything
