# 1- Get user input using input(“Enter your age: ”). 
# If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years
age = int(input('Enter your age: '))
if age >= 18:
	print('You are old enough to drive')
else:
	print('You need %d more years to learn to drive' %(18 - age))


# 2. Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 
# 'years' for bigger differences, and a custom text if my_age = your_age
my_age = 27
your_age = int(input('Enter your age: '))

if my_age > your_age:
	print('I am {} year{} older than you.'.format(my_age - your_age, '' if my_age - your_age == 1 else 's'))
elif your_age > my_age:
	print('You are {} year{} older than me.'.format(your_age - my_age, 's' if your_age - my_age == 1 else 's'))
else:
	print('We are equal!')


# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, else a is equal to b.
a = int(input('Enter number one: '))
b = int(input('Enter number two: '))

if a > b:
	print('%d is greater than %d' % (a, b))
elif b > a:
	print('{} is greater than {}'.format(b, a))
else:
	print('Equal!')


# 3-1. Write a code which gives grade to students according to theirs scores:
# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F
scores = int(input('Enter scores: '))
if 80 <= scores <= 100:
	grade = 'A'
elif scores >= 70:
	grade = 'B'
elif scores >= 60:
	grade = 'C'
elif scores >= 50:
	grade = 'D'
else:
	grade = 'F'

print(f'The student grade is {grade}')


# 3-2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: 
# September, October or November, the season is Autumn. December, January or February, the season is Winter. 
# March, April or May, the season is Spring June, July or August, the season is Summer
month = input('Enter the month: ')

if month in ['September', 'October', 'November']:
	print('The season is Autumn')
elif month in ['December', 'January', 'February']:
	print('The season is Winter')
elif month in ['March', 'April', 'May']:
	print('The season is Spring')
elif month in ['June', 'July', 'August']:
	print('The season is Summer')


# 3-3. The following list contains some fruits
fruits = ['banana', 'orange', 'mango', 'lemon']

new_fruit = input('Enter new fruit: ')
if new_fruit not in fruits:
	fruits.append(new_fruit)
	print(fruits)
else:
	print('That fruit already exist in the list')


# 4. Here we have a person dictionary. Feel free to modify it!
person = {
	'first_name': 'Zouhair',
	'last_name': 'Sahtout',
	'age': 31,
	'country': 'Finland',
	'is_married': True,
	'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
	'address': {
	    'street': 'Space street',
	    'zipcode': '02210'
	}
}

# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
	# print(person.get('skills', 'Here you specify what default value you want to pass'))
	print(person['skills'][len(person['skills']) // 2])


# * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in list(person.keys()):
	if 'Python' in person.get('skills'):
		print('Python')


# * If a person skills has only JavaScript and React, print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
# else print('unknown title')
skills = person['skills']

if 'Node' in skills and 'MongoDB' in skills:
	if 'React' in skills:
		print('He is a fullstack developer')
	elif 'Python' in skills:
		print('He is a backend developer')

elif 'JavaScript' in skills and 'React' in skills:
	print('He is a front end developer')
else:
	print('unknown title')


# * If the person is married and if he lives in Finland, print the information in the following format:
# get() can take a default value, which I set it to False instead of using [] which going to throw an error
if person.get('is_married', False) and person['country'] == 'Finland':
	print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
