# 1- Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num_one: int, num_two: int) -> int:
	return num_one + num_two

print(add_two_numbers(2, 3)) # 5


# 2- Area of a circle is calculated as follows: area = π x r x r. 
# Write a function that calculates area_of_circle.
def area_of_circle(r: int) -> float:
	PI = 3.14
	return PI * r ** 2

print(area_of_circle(10)) # 314.0


# 3- Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums: list) -> int:
	total = 10
	for num in nums:
		if type(num) != int:
			print('Not valid number')
			continue

		total += num

	return total

print(add_all_nums(5)) # 15


# 4- Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(c: int) -> float:
	return (c * 9 / 5) + 32

print(convert_celsius_to_fahrenheit(21)) # 69.8


# 5- Write a function called check-season, it takes a month parameter and returns the season: 
# Autumn, Winter, Spring or Summer.
def check_season(month: str) -> str:
	if month.lower() in ['september', 'october', 'november']:
		return 'Autumn'
	elif month.lower() in ['december', 'january', 'february']:
		return 'Winter'
	elif month.lower() in ['march', 'april', 'may']:
		return 'Spring'
	elif month.lower() in ['june', 'july', 'august']:
		return 'Summer'
	else:
		return 'Not a valid month'

print(check_season('August')) # Summer


# 6- Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1:float, y1:float, x2:float, y2:float) -> float:
	# Check for division by zero
	if x1 == x2:
		return float('inf')
	else:
		slope = (y2 - y1) / (x2 - x1)
		return slope

print(calculate_slope(1, 2, 3, 5)) # 1.5


# 7- Quadratic equation is calculated as follows: ax² + bx + c = 0. 
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a: int, b: int, c:int) -> int:
	# Discriminant calculation
	discriminant = b ** 2 - 4 * a * c

	# Check for real number solutions based on the discriminant
	if discriminant >= 0:
		# Two real number solutions
		root1 = (-b + discriminant**0.5) / (2 * a)
		root2 = (-b - discriminant**0.5) / (2 * a)
		return root1, root2
	else:
		# No real number solutions (complex solutions)
		return None

print(solve_quadratic_eqn(1, 2, 1)) # (-1.0, -1.0)


# 8- Declare a function named print_list. 
# It takes a list as a parameter and it prints out each element of the list.
def print_list(fruits: list) -> None:
	for fruit in fruits:
		print(fruit)

print_list(['banana', 'orange', 'mango', 'lemon'])


# 9- Declare a function named reverse_list. 
# It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(my_list: list) -> list:
	reversed_version = []
	for i in range(len(my_list) - 1, -1, -1):
		reversed_version.append(my_list[i])

	return reversed_version

print(reverse_list([1, 2, 3, 4, 5])) # [5, 4, 3, 2, 1]
print(reverse_list(['A', 'B', 'C'])) # ['C', 'B', 'A']


# 10- Declare a function named capitalize_list_items. 
# It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(my_list: list) -> list:
	for i in range(len(my_list)):
		my_list[i] = my_list[i].capitalize()

	return my_list

print(capitalize_list_items(['a', 'b', 'c'])) # ['A', 'B', 'C']


# 11- Declare a function named add_item. It takes a list and an item parameters. 
# It returns a list with the item added at the end.
def add_item(items: list, item) -> list:
	items.append(item)
	return items

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat')) # ['Potato', 'Tomato', 'Mango', 'Milk', 'Meat']

numbers = [2, 3, 7, 9]
print(add_item(numbers, 11)) # [2, 3, 7, 9, 11]


# 12- Declare a function named remove_item. It takes a list and an item parameters. 
# It returns a list with the item removed from it.
def remove_item(items: list, removed_item) -> list:
	items.remove(removed_item)
	# del items[items.index(removed_item)]
	return items

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango')) # ['Potato', 'Tomato', 'Milk']


# 13- Declare a function named sum_of_numbers. 
# It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(n: int) -> int:
	all_numbers = list(range(n + 1))
	return sum(all_numbers)

print(sum_of_numbers(5)) # 15
print(sum_of_numbers(10)) # 55


# 14- Declare a function named sum_of_odds. 
# It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n: int) -> int:
	odds = 0
	for i in range(n + 1):
		if i % 2 != 0:
			odds += i

	return odds

print(sum_of_odds(10)) # 25


# 15- Declare a function named sum_of_evens. 
# It takes a number parameter and it adds all the even numbers in that range.
def sum_of_evens(n: int) -> int:
	evens = 0
	for i in range(n + 1):
		if i % 2 == 0:
			evens += i

	return evens

print(sum_of_evens(10)) # 30
