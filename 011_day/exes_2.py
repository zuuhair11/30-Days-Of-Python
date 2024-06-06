# 1- Declare a function named evens_and_odds. 
# It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(n: int) -> None:
	evens = 0
	odds = 0
	for i in range(n + 1):
		if i % 2 == 0:
			evens += 1
		else:
			odds += 1

	print('The number of evens are {}'.format(evens))
	print('The number of odds are {}'.format(odds))

evens_and_odds(100)
# The number of evens are 51
# The number of odds are 50


# 2- Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n: int) -> int:
	if n == 0:
		return 1

	return n * factorial(n - 1)

print(factorial(5)) # 120


# 3- Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(x) -> bool:
	# return True if len(x) > 0 else False
	return bool(len(x))

print(is_empty('Hello')) # True
print(is_empty('')) # False


# 4- Write different functions which take lists. 
# They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
numbers = [1, 2, 3, 4, 5]

def calculate_mean(numbers: list) -> float:
	return sum(numbers) / len(numbers)


def calculate_median(numbers: list) -> float:
	ordered_numbers = sorted(numbers)
	length = len(ordered_numbers)

	if length % 2 == 0:
		x = ordered_numbers[(length // 2) - 1]
		y = ordered_numbers[length // 2]
		return (x + y) / 2
	else:
		return ordered_numbers[length // 2]


def calculate_mode(numbers: list) -> int:
	modes = {}
	heighest = ()

	for number in numbers:
		if number not in modes:
			modes[number] = 0

		modes[number] += 1

	for key, value in modes.items():
		if len(heighest) == 0:
			heighest = (key, value)
		
		if value > heighest[1]:
			heighest = (key, value)

	return heighest[0]


def calculate_range(numbers: list) -> int:
	l = max(numbers)
	s = min(numbers)
	return l - s


def calculate_variance(numbers: list) -> float:
	mean = calculate_mean(numbers)
	return sum([(x - mean) ** 2 for x in numbers]) / len(numbers)


import math
def calculate_std(numbers: list) -> float:
	varaince = calculate_variance(numbers)
	return math.sqrt(varaince)


print(calculate_mean(numbers)) # 3.0
print(calculate_median(numbers)) # 3
print(calculate_mode([7, 11, 3, 11, 5, 3, 4, 11, 9])) # 11
print(calculate_range([7, 11, 3, 11, 5, 3, 4, 11, 9])) # 8
print(calculate_variance(numbers)) # 2.0
print(calculate_std(numbers)) # 1.4142135623730951
