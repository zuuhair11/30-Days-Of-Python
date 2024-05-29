# 1- Declare your age as integer variable
age = 30

# 2- Declare your height as a float variable
height = 178.5

# 3- Declare a variable that store a complex number
question = 10 + 1j

# 4- Write a script that prompts the user to enter base and height of the triangle 
# And calculate an area of this triangle (area = 0.5 x b x h).
base = int(input('Enter base: '))
height = int(input('Enter height: '))

area_of_triangle = 0.5 * base * height
print('The area of the triangle is {}'.format(area_of_triangle))


# 5- Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
# Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = int(input('Enter side a: '))
side_b = int(input('Enter side b: '))
side_c = int(input('Enter side c: '))

perimeter = side_a + side_b + side_c
print(f'The perimeter of the triangle is {perimeter}')


# 6- Get length and width of a rectangle using prompt. Calculate its area (area = length x width) 
# and perimeter (perimeter = 2 x (length + width))
length = int(input('Enter length of the rectangle: '))
width = int(input('Enter width of the rectangle: '))

area = length * width
perimeter = 2 * (length + width)
print('The area of the rectangle is', area)
print('The perimeter of the rectangle is {}'.format(perimeter))


# 7- Get radius of a circle using prompt. Calculate the area (area = pi x r x r) 
# And circumference (c = 2 x pi x r) where pi = 3.14.
radius = int(input('Enter a radius: '))
pi = 3.14

area_of_circle = pi * (radius ** 2)
circumference = 2 * pi * radius
print('The area of the circle is {}'.format(area_of_circle))
print('The circumference of the circle is {}'.format(circumference))


# 8- Calculate the slope, x-intercept and y-intercept of y = 2x - 2
# Slope is the coefficient of x
slope = 2

# Solve for x-intercept (implicitly sets y to zero)
x_intercept = 2 / 2

# Solve for y-intercept (set x to zero)
y_intercept = 2 * (0) - 2

# Print the results
print("Slope:", slope)
print("X-intercept:", x_intercept)
print("Y-intercept:", y_intercept)


# 9- Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
import math

slope2 = (10 - 2) / (6 - 2)
euclidean = math.sqrt((6 - 2) ** 2 + (10 - 2) ** 2)

print('The slope between point (2, 2) and point (6,10) is', slope)
print('The Euclidean disctance between point (2, 2) and point (6,10) is', euclidean)


# 10- Compare the slopes in tasks 8 and 9.
compare_slopes = slope == slope2
print('slope == slope2', slope == slope2)


# Calculate the value of y (y = x^2 + 6x + 9). 
# Try to use different x values and figure out at what x value y is going to be 0.
x = -3
y = x ** 2 + 6 * x + 9
print(y)


# 12- Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') == len('dragon')) # True

# 13- Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon') # True

# 14- I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon') # True

# 15- There is no 'on' in both dragon and python
print('on' not in 'dragon' and 'on' not in 'python') # False

# 16- Find the length of the text python and convert the value to float and convert it to string
print(str(float(len('python')))) # 6.0

# 17- Even numbers are divisible by 2 and the remainder is zero. 
# How do you check if a number is even or not using python?
print('Is 4 even, by checking if 4 % 2 == 0:', 4 % 2 == 0) # Is 4 even, by checking if 4 % 2 == 0: True

# 18- Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print('7 // 3 == 2.7:', 7 // 3 == 2.7) # 7 // 3 == 2.7: False

# 19- Check if type of '10' is equal to type of 10
print("type('10') == type(10) is:", type('10') == type(10)) # type('10') == type(10) is: False

# 20- Check if int('9.8') is equal to 10
print("int('9.8') == 10", int(9.8) == 10) # False

# 21- Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input('Enter hours: '))
rate_per_hour = int(input('Enter rate per hour: '))

print('Your weekly earning is', hours * rate_per_hour)


# 22- Write a script that prompts the user to enter number of years. 
# Calculate the number of seconds a person can live. Assume a person can live hundred years
number_of_years = int(input('Enter number of years you have lived: '))
number_of_seconds = number_of_years * 365 * 24 * 60 * 60

print('You have lived for {} seconds.'.format(number_of_seconds))


# 23- Write a Python script that displays the following table
for i in range(1, 6):
    print(i, 1, i * 1, i * i, (i * i) * i)
