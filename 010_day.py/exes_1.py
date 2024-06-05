# 1- Iterate 0 to 10 using for loop, do the same using while loop.
# for loop
for i in range(11):
	print(i)

# while loop
j = 0
while j < 11:
	print(j)
	j = j + 1


# 2- Iterate 10 to 0 using for loop, do the same using while loop.
# for loop
for i in range(10, -1, -1):
	print(i)

# while loop
j = 10
while j >= 0:
	print(j)
	j = j - 1


# 3- Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#
##
###
####
#####
######
#######
for row in range(1, 8):
	print('#' * row)


# 4- Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
for _ in range(8):
	for j in range(1, 9):
		print('# ', end='')

	print()


# 5- Print the following pattern:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
for number in range(11):
	print('%d x %d = %d' % (number, number, number * number))


# 6- Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] 
# using a for loop and print out the items.
for item in ['Python', 'Numpy','Pandas','Django', 'Flask']:
	print(item)


# 7- Use for loop to iterate from 0 to 100 and print only even numbers
for number in range(101):
	if number % 2 == 0:
		print(number)

# 8- Use for loop to iterate from 0 to 100 and print only odd numbers
for number in range(101):
	if number % 2 != 0:
		print(number)
