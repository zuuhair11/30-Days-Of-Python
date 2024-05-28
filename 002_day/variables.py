####################
# Exercises: Level 1
####################
# 1- Create a file named variables.py

# 2- Write a python comment
# Day 2:30 Days Of Python Programming

# 3- Declare a first name variable and assign a value to it
first_name = 'Zouhair'

# 4- Declare a last name variable and assign a value to it
last_name = 'Sahtout'

# 5- Declare a full name variable and assign a value to it
full_name = '{} {}'.format(first_name, last_name)
full_name2 = f'{first_name} {last_name}'

# 6- Declare a country variable and assign a value to it
country = 'Morocco'

# 7- Declare a city variable and assign a value to it
city = 'Sale'

# 8- Declare an age variable and assign a value to it
age = 30

# 9- Declare a year variable and assign a value to it
year = 1997

# 10- Declare a variable is_married and assign a value to it
is_married = False

# 11- Declare a variable is_true and assign a value to it
is_true = is_married

# 12- Declare a variable is_light_on and assign a value to it
is_light_on = True

# 13 Declare multiple variable on one line
fav_color, fav_number = 'Blue', 11



####################
# Exercises: Level 2
####################
# 1- Check the data type of all your variables using type() built-in function
print(type(first_name), type(last_name), type(full_name)) # <class 'str'> <class 'str'> <class 'str'>
print(type(country), type(city), type(age), type(year)) # <class 'str'> ... <class 'int'> <class 'int'>
print(type(is_married), type(is_true), type(is_light_on)) # <class 'bool'> <class 'bool'> <class 'bool'>
print(type(fav_color), type(fav_number)) # <class 'str'> <class 'int'>

# 2- Using the len() built-in function, find the length of your first name
print(len(first_name)) # 7

# 3- Compare the length of your first name and your last name
print(len(first_name) == len(last_name)) # True

# 4- Declare 5 as num_one and 4 as num_two
num_one, num_two = 5, 4

# 4, 1- Add num_one and num_two and assign the value to a variable total
total = num_one + num_two

# 4, 2- Subtract num_two from num_one and assign the value to a variable diff
diff = num_two - num_one

# 4, 3- Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one

# 4, 4- Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two

# 4, 5- Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one

# 4, 6- Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two

# 4, 7- Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two


# 5- The radius of a circle is 30 meters. 
radius = 30

# 5, 1- Calculate the area of a circle and assign the value to a variable name of area_of_circle
import math
area_of_circle = math.pi * (radius ** 2)
print('Area of the circle:', area_of_circle) # Area of the circle: 2827.4333882308138

# 5, 2- Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * math.pi * radius
print('Circumference of the circle:', circum_of_circle) # Circumference of the circle: 188.49555921538757

# 5, 3- Take radius as user input and calculate the area.
radius = int(input('Enter the radius of your circle: '))
area_of_circle = math.pi * (radius ** 2)
print('The area is', area_of_circle) # The area is 314.1592653589793


# 6- Use the built-in input function to get information from the user and store it in variables
first_name = input('First name: ')
last_name = input('Last name: ')
country = input('Country: ')
age = input('Age: ')

# 6- Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
# Here is a list of the Python keywords.  Enter any keyword to get more help.
# False               class               from                or
# None                continue            global              pass
# True                def                 if                  raise
# and                 del                 import              return
# as                  elif                in                  try
# assert              else                is                  while
# async               except              lambda              with
# await               finally             nonlocal            yield
# break               for                 not 
