# 1- Write a function called is_prime, which checks if a nber is prime.
def is_prime(n: int) -> bool:
	if n <= 1:
		return False  # 1 and less are not prime
	if n <= 3:
		return True   # 2 and 3 are prime

	# Check divisibility only up to the square root of num
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return False
		return True

print(is_prime(11)) # True
print(is_prime(4)) # False


# 2- Write a functions which checks if all items are unique in the list.
def check_all_unique(items: list) -> bool:
	# First attempt
	# uniques = []
	# for item in items:
	# 	if item not in uniques:
	# 		uniques.append(item)
	# 	else:
	# 		return False
	# else:
	# 	return True

	# Second attempt
	return True if len(items) == len(set(items)) else False

print(check_all_unique([1, 2, 3])) # True
print(check_all_unique([1, 2, 3, 2])) # False


# 3- Write a function which checks if all the items of the list are of the same data type.
def check_all_same_type(items: list) -> bool:
	tp = ''
	for item in items:
		if tp == '':
			tp = type(item)
		elif type(item) != tp:
			return False

	return True

print(check_all_same_type([1, 2, 3])) # True
print(check_all_same_type([1, '2', 3])) # False


# 4- Write a function which check if provided variable is a valid python variable


# 5- Go to the data folder and access the countries-data.py file.
# 5.1- Create a function called the most_spoken_languages in the world. 
# It should return 10 or 20 most spoken languages in the world in descending order


# 5.2- Create a function called the most_populated_countries. 
# It should return 10 or 20 most populated countries in descending order.
