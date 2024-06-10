# 1- Writ a function which generates a six digit/character random_user_id.
import random
import string

def random_user_id() -> str:
	itmes = string.ascii_letters + string.digits
	return ''.join(random.sample(itmes, 6))

print(random_user_id()) # aDZP19


# 2- Modify the previous task. Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs 
# which are supposed to be generated.
def random_user_id() -> None:
	num_char, num_ids = input('number of characters & number of IDs (x y): ').split(' ')

	items = string.ascii_letters + string.digits
	for _ in range(int(num_ids)):
		print(''.join(random.sample(items, int(num_char))))

random_user_id()


# 3- Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
import random

def rgb_color_gen() -> tuple:
	return 'rgb({}, {}, {})'.format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

print(rgb_color_gen()) # (248, 164, 157)
