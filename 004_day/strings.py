def run() -> None:
	##########
	# Simple #
	##########
	output = 'P'
	output = 'Hello, World!'
	output = len(output)


	###############################
	# Escape Sequences in Strings #
	###############################
	output = 'Hey,\nI hope you are doing well'
	output = '''Hello,
	today I went for a run with my friend,
	it was fun.
	'''.replace('\t', '')


	###############################
	# Escape Sequences in Strings #
	###############################
	# Old Style String Formatting (% Operator)
	output = 'I hope you are having a good day,\nAre you? '
	output = 'Days\tTopics\tExercises'
	output = 'Day 1\t5\t5\t5\t5'


	#####################
	# String formatting #
	#####################
	# Old Style String Formatting (% Operator)
	# %s: String (or any object with a string representation, like numbers or lists)
	# %d: Integer (whole number)
	# %f: Floating-point number
	# %.nf: Floating-point number with n digits after the decimal point (e.g., %.2f for two 
	output = 'Name: %s, Age: %d, Height: %.2f' %('Zouhair', 30, 1.78) # Name: Zouhair, Age: 30, Height: 1.78

	# New Style String Formatting (str.format)
	output = 'I am {} and I\'m {}. Thank you <3'.format('Zouhair', 30) # I am Zouhair and I'm 30. Thank you <3
	output = '{:.2f}'.format(4 / 3) # 1.33

	# String Interpolation / f-Strings (Python 3.6+)
	output = f'{4 / 3:.2f}' # 1.33


	#############################################
	# Python Strings as Sequences of Characters #
	#############################################
	# Strings as Sequences
	my_string = 'Hello'
	output = my_string[0] # H
	output = my_string[1:3] # el
	output = my_string[1:10] # ello
	output = my_string[-1:] # o
	output = my_string[-3:] # llo
	output = my_string[::-1] # olleH

	# Skipping Characters While Slicing
	output = my_string[0:6:2] # Hlo
	for char in my_string:
		print(char)

	# Shared Methods
	output = len(my_string) # 5
	output = my_string + ' World' # Hello World
	output = 'o' in my_string # True
	output = 'thirty days of python'.capitalize() # Thirty days of python
	output = 'thirty days of python'.count('y') # 3
	output = 'thirty days of python'.count('y', 9, 16) # 1
	#         012345...9..... 16...

	# Checks if a string ends with a specified ending
	output = 'thirty days of python'.endswith('on') # True

	# Replaces tab character with spaces, default tab size is 8. It takes tab size argument
	output = 'thirty\tdays\tof\tpython' # thirty	days	of	python
	output = output.expandtabs(1) # thirty days of python

	# Returns the index of the first occurrence of a substring, if not found returns -1
	output = 'Hello'.find('l') # 2

	# Returns the index of the last occurrence of a substring, if not found returns -1
	output = 'Hello'.rfind('l') # 3

	# Returns the lowest index of a substring, additional arguments indicate starting and ending index 
	# (default 0 and string length - 1). If the substring is not found it raises a valueError.
	# string.index(substring, start, end)
	my_string = "hello world"
	output = my_string.index("o")      # Output: 4
	output = my_string.index("o", 5)   # Output: 7
	output = my_string.index("world")  # Output: 6
	# output = my_string.index('foo')  # ValueError: substring not found

	# Returns the highest index of a substring, additional arguments indicate starting and ending index 
	# (default 0 and string length - 1)
	output = my_string.rindex('o')	   # Output: 7

	# Checks alphanumeric character
	my_string = 'ThirtyDaysPython'
	output = my_string.isalnum() # True
	# Space is not an alphanumeric character
	output = (my_string + 'Day 4').isalnum() # False
	output = '123'.isalnum() # False

	# Checks if all string elements are alphabet characters (a-z and A-Z)
	my_string = 'thirty days of python'
	# Once again because there's a space
	output = my_string.isalpha() # False

	my_string = 'ThirtyDaysPython'
	output = my_string.isalpha() # True

	# Checks if all characters in a string are decimal (0-9)
	challenge = 'thirty days of python'
	output = challenge.isdecimal() # False

	challenge = '123'
	output = challenge.isdecimal() # True

	challenge = '\u00B2'
	output = challenge.isdigit() # False

	challenge = '12 3'
	# Once again the space not allowed
	output = challenge.isdecimal() # False


	# Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
	challenge = 'Thirty'
	output = challenge.isdigit() # False

	challenge = '11'
	output = challenge.isdigit() # True

	challenge = '\u00B2' # ²
	output = challenge.isdigit() # True

	# Checks if all characters in a string are numbers or number related 
	# (just like isdigit(), just accepts more symbols, like ½)
	output = '11'.isnumeric() # True
	challenge = '\u00BD' # ½
	output = challenge.isnumeric() # True
	output = '10.5'.isnumeric() # False

	# Checks for a valid identifier - it checks if a string is a valid variable name
	# Because it starts with a number
	output = '30DaysOfPython'.isidentifier() # False
	output = 'thirty_days_of_python'.isidentifier() # True

	# Checks if all alphabet characters in the string are lowercase
	output = 'thirty days of python'.islower() # True
	output = 'Thirty days of python'.islower() # False

	# Checks if all alphabet characters in the string are uppercase
	output = 'thirty days of python'.isupper() # False
	output = 'THIRTY DAYS OF PYTHON'.isupper() # True

	# Returns a concatenated string
	web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
	output = ' '.join(web_tech) # HTML CSS JavaScript React

	# Removes all given characters starting from the beginning and end of the string
	output = '	thirty days of pythoonnn'.strip() # thirty days of pythoonnn
	output = 'thirty days of pythoonnn'.strip('noth') # irty days of py

	# Replaces substring with a given string
	output = 'thirty days of python'.replace('python', 'coding') # thirty days of python

	# Splits the string, using given string or space as a separator
	# string.split(separator, maxsplit)
	# The delimiter by which the string is split. If not provided, any whitespace string is a separator.
	# The maximum number of splits to do. Default value is -1, which means "no limit" on the number of splits.
	output = 'thirty days of python'.split() # ['thirty', 'days', 'of', 'python']

	# Returns a title cased string
	output = 'thirty days of python'.title() # Thirty Days Of Python

	# Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
	output = 'Thirty Days Of Python'.swapcase() # tHIRTY dAYS oF pYTHON

	# Checks if String Starts with the Specified String
	output = 'thirty days of python'.startswith('thirty') # True


	#############
	# Unpacking #
	#############
	# Unpacking
	my_string = 'ABC'
	a, b, c = my_string 
	output = a # A
	output = b # B
	output = c # C


	print(output)


if __name__ == '__main__':
	run()
