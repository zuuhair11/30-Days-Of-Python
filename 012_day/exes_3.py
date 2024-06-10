# 1- Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
import random

def shuffle_list(numbers: list) -> list:
	shuffled_numbers = []
	shuffled_numbers[:] = numbers
	random.shuffle(shuffled_numbers)

	return shuffled_numbers

numbers = [1, 2, 3, 4, 5]

print(shuffle_list(numbers)) # [2, 3, 5, 1, 4]
print(numbers) # [1, 2, 3, 4, 5]


# 2- Write a function which returns an array of seven random numbers in a range of 0-9. 
# All the numbers must be unique.
def generate_random_unique_numbers() -> list:
	numbers = set()

	while len(numbers) != 7:
		numbers.add(random.randint(0, 9))

	return list(numbers)

print(generate_random_unique_numbers()) # [0, 1, 3, 4, 5, 6, 9]
