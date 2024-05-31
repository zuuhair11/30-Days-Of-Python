# 1- Declare an empty list
empty_list = []
empty_list = list()
output = empty_list # []

# 2- Declare a list with more than 5 items
lst = [1, 2, 3, 4, 5]
lst = list((1, 2, 3, 4, 5))
output = lst # [1, 2, 3, 4, 5]

# 3- Find the length of your list
length = len(lst)
output = length # 5

# 4- Get the first item, the middle item and the last item of the list
# First attempt
first, _, middle, _, last = lst

# Second attempt
first = lst[0]
middle = lst[(len(lst) - 1) // 2]
last = lst[-1]

print(first) 	# 1
print(middle) 	# 3
print(last) 	# 5

# 5- Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Zouhair', 26, 1.78, 'Single', '127.0.0.1']
output = mixed_data_types # ['Zouhair', 30, 1.78, 'Single', '127.0.0.1']

# 6- Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7- Print the list using print()
print(it_companies) # ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 8- Print the number of companies in the list
print(len(it_companies)) # 7

# 9- Print the first, middle and last company
first = it_companies[0]
middle = it_companies[(len(it_companies) - 1) // 2]
middle = it_companies[(len(it_companies) - 1) // 2:(len(it_companies) - 1) // 2 + 1][0]
last = list(reversed(it_companies))[0]

print(first) # Facebook
print(middle) # Apple
print(last) # Amazon

# 10- Print the list after modifying one of the companies
it_companies[0] = 'X'
print(it_companies) # ['X', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 11- Add an IT company to it_companies
it_companies.append('ELEVEN')
print(it_companies) # ['X', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'ELEVEN']

# 12- Insert an IT company in the middle of the companies list
it_companies.insert((len(it_companies) - 1) // 2 + 1, 'Meta')
print(it_companies) # ['X', 'Google', 'Microsoft', 'Apple', 'Meta', 'IBM', 'Oracle', 'Amazon', 'ELEVEN']

# 13- Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[-3] = it_companies[-3].upper()
print(it_companies) # ['X', 'Google', 'Microsoft', 'Apple', 'Meta', 'IBM', 'ORACLE', 'Amazon', 'ELEVEN']

# 14- Join the it_companies with a string '#;  '
print('#; '.join(it_companies)) # X#; Google#; Microsoft#; Apple#; Meta#; IBM#; ORACLE#; Amazon#; ELEVEN

# 15- Check if a certain company exists in the it_companies list.
print('ELEVEN' in it_companies) # True
print('X' in it_companies) # True
print('x' in it_companies) # False

# 16- Sort the list using sort() method
# This will mutate the original array
it_companies.sort()
print(it_companies) # ['Amazon', 'Apple', 'ELEVEN', 'Google', 'IBM', 'Meta', 'Microsoft', 'ORACLE', 'X']

# 17- Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies) # ['X', 'ORACLE', 'Microsoft', 'Meta', 'IBM', 'Google', 'ELEVEN', 'Apple', 'Amazon']

# Or
it_companies.sort(reverse=True)
print(it_companies) # ['X', 'ORACLE', 'Microsoft', 'Meta', 'IBM', 'Google', 'ELEVEN', 'Apple', 'Amazon']

# 18- Slice out the first 3 companies from the list
first_three_companies = it_companies[:3]
print(first_three_companies) # ['X', 'ORACLE', 'Microsoft']

# 19- Slice out the last 3 companies from the list
last_three_companies = it_companies[-3:]
print(last_three_companies) # ['ELEVEN', 'Apple', 'Amazon']

# 20- Slice out the middle IT company or companies from the list
middle_companies = it_companies[1:-1]
print(middle_companies) # ['ORACLE', 'Microsoft', 'Meta', 'IBM', 'Google', 'ELEVEN', 'Apple']

# 21- Remove the first IT company from the list
# it_companies.remove('X')
# del it_companies[0]
it_companies.pop(0)
print(it_companies) # ['ORACLE', 'Microsoft', 'Meta', 'IBM', 'Google', 'ELEVEN', 'Apple', 'Amazon']

# 22- Remove the middle IT company or companies from the list
del it_companies[1:-1]
print(it_companies) # ['ORACLE', 'Amazon']

# 23- Remove the last IT company from the list
it_companies.pop()
print(it_companies) # ['ORACLE']

# 24- Remove all IT companies from the list
it_companies.clear()
print(it_companies) # []

# 25- Destroy the IT companies list
del it_companies
# print(it_companies) # error: NameError: name 'it_companies' is not defined

# 26- Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack) # ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']

# 27- After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack) # ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Python', 'SQL', 'Node', 'Express', 'MongoDB']



print(output)
