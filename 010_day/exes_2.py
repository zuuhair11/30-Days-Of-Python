# 1- Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum_numbers = 0
for number in range(101):
	sum_numbers += number

print('The sum of all numbers is {}.'.format(sum_numbers))


# 2- Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
evens = 0
odds = 0
for number in range(0, 101, 1):
	if number % 2 == 0:
		evens += number
	else:
		odds += number

print(f'The sum of all evens is {evens}. And the sum of all odds is {odds}.')
