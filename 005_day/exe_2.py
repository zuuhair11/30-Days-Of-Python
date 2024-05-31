# 1- The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# -> Sort the list and find the min and max age
min_age = sorted(ages)[0]
max_age = sorted(ages, reverse=True)[0]
print(min_age) # 19
print(max_age) # 26

# -> Add the min age and the max age again to the lis
ages.append(min_age)
ages.append(max_age)
print(ages) # [19, 22, 19, 24, 20, 25, 26, 24, 25, 24, 19, 26]

# -> Find the median age (one middle item or two middle items divided by two)
def find_median(ages: list) -> None:
	sorted_ages = sorted(ages)
	length = len(sorted_ages)

	if length % 2 == 1:
		median = sorted_ages[length // 2]
	else:
		middle_1 = sorted_ages[(length // 2) - 1]
		middle_2 = sorted_ages[length // 2]
		median = (middle_1 + middle_2) / 2

	print(median)

find_median(ages) # 24


# -> Find the average age (sum of all items divided by their number )
def find_average_age(ages: list) -> None:
	average = sum(ages) / len(ages)
	print(average)

find_average_age(ages) # 22.75


# -> Find the range of the ages (max minus min)
average = max(ages) - min(ages)
print(average) # 7


# -> Compare the value of (min - average) and (max - average), use abs() method
print(abs(min(ages) - average) == abs(max(ages) - average)) # False


# 1- Find the middle country(ies) in the countries list
def find_middle_country(countries: list) -> None:
	n = len(countries)

	if n % 2 == 0:
		middle_country = countries[n // 2]
	else:
		middle_country = countries[n // 2 + 1]

	print(middle_country)

import countries
find_middle_country(countries.data) # Liberia


# 2- Divide the countries list into two equal lists if it is even if not one more country for the first half.
def divider(countries: list) -> tuple:
	length = len(countries)

	if length % 2 == 0:
		first = countries[:length // 2]
		second = countries[length // 2:]
	else:
		first = countries[:length // 2 + 1]
		second = countries[length // 2 + 1:]

	return (first, second)


first, second = divider(countries.data)


# 3- ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

country_1, country_2, country_3, *scandic_countries = countries
print(country_1) # China
print(scandic_countries) # ['Finland', 'Sweden', 'Norway', 'Denmark']
