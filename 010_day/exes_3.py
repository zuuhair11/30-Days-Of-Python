# 1- Go to the data folder and use the countries.py file. 
# Loop through the countries and extract all the countries containing the word land.
import data
for country in data.countries:
	if 'land' in country:
		print(country)


# 2- This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruits = []
for i in range(len(fruits) - 1, -1, -1):
	new_fruits.append(fruits[i])

print(new_fruits) # ['lemon', 'mango', 'orange', 'banana']


# 3.1- What are the total number of languages in the data
from countries_data import countries_data

lngs = set()
for country in countries_data:
	for language in country['languages']:
		lngs.add(language)

print(len(lngs)) # 112


# 3.2- Find the ten most spoken languages from the data
def most_spoken_languages(countries: list) -> dict:
	most_spoken_languages = {}

	for country in countries_data:
		for language in country['languages']:
			if language not in most_spoken_languages:
				most_spoken_languages[language] = 0

			most_spoken_languages[language] += 1

	return dict(sorted(most_spoken_languages.items(), key=lambda language: language[1], reverse=True))

sorted_languages = most_spoken_languages(countries_data)
print(sorted_languages)


# 3.3- Find the 10 most populated countries in the world
def most_populated_countries(countries: list) -> list:
	return sorted(countries, key=lambda country: country['population'], reverse=True)

sorted_countries = most_populated_countries(countries_data)
print(sorted_countries)
