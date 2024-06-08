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
import string

def is_valid_variable(v: str) -> bool:
	legal = string.ascii_letters + '_'
	illegal = string.punctuation.replace('_', '')

	if len(str(v)) > 0:
		if v[0] in legal:
			for char in v:
				if char in illegal:
					return False
			return True
		else:
			return False
	else:
		return False

print('my_variable:', is_valid_variable("my_variable"))  # True
print('1variable:', is_valid_variable("1variable"))  # False
print('var$iable:', is_valid_variable("var$iable"))  # False
print('"":', is_valid_variable(""))  # False


# 5- Go to the data folder and access the countries-data.py file.
# 5.1- Create a function called the most_spoken_languages in the world. 
# It should return 10 or 20 most spoken languages in the world in descending order
import countries

def most_spoken_languages(countries: list) -> list:
	spoken_languages = {}
	for country in countries:
		for language in country['languages']:
			if language not in spoken_languages:
				spoken_languages[language] = 0

			spoken_languages[language] += 1

	sorted_laguages = sorted(spoken_languages.items(), key=lambda item: item[1], reverse=True)
	return dict(sorted_laguages[:10])

print(most_spoken_languages(countries.countries))


# 5.2- Create a function called the most_populated_countries. 
# It should return 10 or 20 most populated countries in descending order.
def most_populated_countries(countries: list) -> list:
	return sorted(countries, key=lambda country: country['population'], reverse=True)[:10]

sorted_countries = most_populated_countries(countries.countries)
print(sorted_countries)
