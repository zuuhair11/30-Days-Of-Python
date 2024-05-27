# 1- Write an example for different Python data types
print('My name is', 'John', 'the type is:', type('John'))
print('My age is', 30, 'the type is:', type(30))
print('My rate is', 19.5, 'the type is:', type(19.5))
print('An example of complex', 3 + 7j, 'the type is:', type(3 + 7j))
print('Am I programmer', True, 'the type is:', type(True))
print('My favorite fruits are', ['Strawberry', 'Pear'], 'the type is:', type(['Strawberry', 'Pear']))
print('My favorite numbers are', (11, '20:05'), 'the type is:', type((11, '20:05')))
print('My grades are', {18, 19}, 'the type is:', type({18, 19}))
print('My info is', {'name': 'Zouhair', 'age': 30}, 'the type is:', type({'name': 'Zouhair', 'age': 30}))


# 2- Find an Euclidian distance between (2, 3) and (10, 8)
import math

# Coordinates of the points
x1, y1 = 2, 3
x2, y2 = 10, 8

# Calculate the Euclidean distance
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(distance)
