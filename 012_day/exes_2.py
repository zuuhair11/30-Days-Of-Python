# 1- Write a function named list_of_hexa_colors. 
# This function should generate a specific type of data: a list of hexadecimal color codes.
import random
import string

def list_of_hexa_colors(n: int) -> list:
	colors = list()

	for _ in range(n):
		colors.append('#' + ''.join(random.sample(string.hexdigits, 6)))

	return colors

print(list_of_hexa_colors(3)) # ['#269DEc', '#02C4BF', '#fC37c1']


# 2- Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(n: int) -> list:
	colors = []
	for _ in range(n):
		colors.append('rgb(%s, %s, %s)' %(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))

	return colors

print(list_of_rgb_colors(3)) # [151, 222, 232]


# 3- Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(type_of_number: str, n: int) -> list:
	if type_of_number == 'hexa':
		return list_of_hexa_colors(n)
	elif type_of_number == 'rgb':
		return list_of_rgb_colors(n)

print(generate_colors('hexa', 3)) # ['#a3e12f','#03ed55','#eb3d2b'] 
print(generate_colors('hexa', 1)) # ['#b334ef']
print(generate_colors('rgb', 3))  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
print(generate_colors('rgb', 1))  # ['rgb(33,79, 176)']
