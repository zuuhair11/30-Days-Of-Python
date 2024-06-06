#############
# Functions #
#############
# So far we have seen many built-in Python functions. In this section, we will focus on custom functions.
# A function is a reusable block of code or programming statement designed to perform a certain task.
# To define or declare a function, Python provides the 'def' keyword.
# The function block of code is executed only if the function is called or invoked.


####################################
# Declaring and Calling a Function #
####################################
# When we make a function, we call it declaring a function. 
# When we start using the it, we call it calling or invoking a function. 
# Function can be declared with or without parameters.
# Function without Parameters
def add_two_numbers() -> None:
	num_one = 2
	num_two = 3
	total = num_one + num_two
	print(total)

add_two_numbers() # 5


#######################################
# Function Returning a Value - Part 1 #
#######################################
# Function can also return values, if a function does not have a return statement, 
# the value of the function is None.
# Let us rewrite the above function using return.
def add_two_numbers() -> int:
	num_one = 2
	num_two = 3
	total = num_one + num_two
	return total

result = add_two_numbers()
print(result) # 5


############################
# Function with Parameters #
############################
# In a function we can pass different data types(number, string, boolean, list, tuple, dictionary or set) 
# as a parameter
# "Single Parameter": If our function takes a parameter we should call our function with an argument
def area_of_circle(r: int) -> float:
	PI = 3.14
	area = PI * r ** 2
	return area

result = area_of_circle(10)
print(result) # 314.0


# Get the sum of the numbers
def sum_of_numbers(n: int) -> int:
	total = 0
	for i in range(n + 1):
		total = total + i

	return total

result = sum_of_numbers(5)
print(result) # 15


# Get the factorial
def factorial(n: int) -> int:
	if n == 0:
		return 1

	return n * factorial(n - 1)

result = factorial(5)
print(result) # 120


# "Two Parameter": A function may or may not have a parameter or parameters. 
# A function may also have two or more parameters. 
# If our function takes parameters we should call it with arguments. 
# Let us check a function with two parameters:
# Get the sum of two numbers
def sum_two_numbers(num_one: int, num_two: int) -> int:
	s = num_one + num_two
	return s

result = sum_two_numbers(2, 3)
print(result) # 5


# Get the weight of an object
def weight_of_object(mass: int, gravity: float) -> str:
	weight = str(mass * gravity) + ' N'
	return weight

result = weight_of_object(100, 9.81)
print(result) # 981.0 N


########################################
# Passing Arguments with Key and Value #
########################################
# If we pass the arguments with key and value, the order of the arguments does not matter.
def print_fullname(first_name: str, last_name: str) -> str:
	space = ' '
	full_name = first_name + space + last_name

	return full_name

result = print_fullname(last_name = 'Sahtout', first_name = 'Zouhair') # Order does not matter
print(result) # Zouhair Sahtout


#######################################
# Function Returning a Value - Part 2 #
#######################################
# If we do not return a value with a function, then our function is returning None by default.
# To return a value with a function we use the keyword 'return' followed by the variable we are returning. 
# We can return any kind of data types from a function.
# Returning a boolean: Example:
def is_even(n: int) -> bool:
	if n % 2 == 0:
		print('even')
		return True
	return False

print(is_even(2)) # even, True
print(is_even(7)) # False


# Returning a list: Example:
def find_even_numbers(n):
	evens = []
	for i in range(n + 1):
		if i % 2 == 0:
			evens.append(i)

	return evens

result = find_even_numbers(10)
print(result) # [0, 2, 4, 6, 8, 10]


####################################
# Function with Default Parameters #
####################################
# Sometimes we pass default values to parameters, when we invoke the function. 
# If we do not pass arguments when calling the function, their default values will be used.
# Always default values be the last thing
def weight_of_object(mass: int, gravity: float=9.81) -> str:
	weight = str(mass * gravity) + ' N' # the value has to be changed to string first
	return weight

print(weight_of_object(100)) # 981.0 N - average gravity on Earth's surface
print(weight_of_object(100, 1.62)) # 162.0 N - gravity on the surface of the Moon


#################################
# Arbitrary Number of Arguments #
#################################
# If we do not know the number of arguments we pass to our function, we can create a function 
# which can take arbitrary number of arguments by adding * before the parameter name.
def sum_all_nums(*nums: list):
	total = 0
	for num in nums:
		total += num # same as total = total + num

	return total

print(sum_all_nums(2, 3, 5)) # 10


###########################################################
# Default and Arbitrary Number of Parameters in Functions #
###########################################################
def generate_groups(team: str, *args: list) -> None:
	print(team)
	for i in args:
		print(i)

generate_groups('Team-1', 'Zouhair', 'Asabeneh', 'Brooke', 'David')


###############################################
# Function as a Parameter of Another Function #
###############################################
def square_number(n: int) -> int:
	return n ** 2

def do_something(f: str, n: int) -> int:
	return f(n)

print(do_something(square_number, 5)) # 25
