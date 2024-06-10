####################
# What is a Module #
####################
# A module is a file containing a set of codes or a set of functions which can be included to an application. 
# A module could be a file containing a single variable, a function or a big code base.


#####################
# Creating a Module #
#####################
# To create a module we write our codes in a python script and we save it as a .py file. 
# Create a file named mymodule.py inside your project folder. Let us write some code in this file.
# Done


######################
# Importing a Module #
######################
# To import the file we use the import keyword and the name of the file only.
import mymodule
print(mymodule.generate_full_name('Zouhair', 'Sahtout')) # Zouhair Sahtout

# If we want to import only the function
from mymodule import generate_full_name
print(generate_full_name('John', 'Doe')) # John Doe


###############################################
# Import Functions from a Module and Renaming #
###############################################
# During importing we can rename the name of the module.
from mymodule import generate_full_name as full_name
print(full_name('John', 'Doe')) # John Doe


###########################
# Import Built-in Modules #
###########################
# OS Module
###########
###########
# Using python os module it is possible to automatically perform many operating system tasks.
# The OS module in Python provides functions for creating, changing current working directory, 
# And removing a directory (folder), fetching its contents, changing and identifying the current directory.
import os

# Creating a directory
# os.mkdir('directory_name')
# Changing the current directory
# os.chdir('path')
# Getting current working directory
# os.getcwd()
# Removing directory
# os.rmdir()


# Sys Module
############
############
# The sys module provides functions and variables used to manipulate different parts of the Python runtime 
# environment. Function sys.argv returns a list of command line arguments passed to a Python script. 
# The item at index 0 in this list is always the name of the script, at index 1 is
# the argument passed from the command line.
import sys

print('first: {}, second: {}, third: {}'.format(sys.argv[0], sys.argv[1], sys.argv[2]))

# Now to check how this script works I wrote in command line:
# python main.py Zouhair Sahtout => first: main.py, second: Zouhair, third: Sahtout

# Some useful sys commands:
# To know the version of python you are using
print(sys.version) # 3.12.3 (main, Apr 17 2024, 00:00:00) [GCC 14.0.1 20240411 (Red Hat 14.0.1-0)]

# Get the size of an object
x = 11
print('The size of x: %d, bytes' %(sys.getsizeof(x))) # The size of x: 28, bytes

# Print platform information
print('Platfrom: %s' %sys.platform) # Platfrom: linux

# To know the largest integer variable it takes
print(sys.maxsize) # 9223372036854775807

# To exit sys
# sys.exit()
# print('This line will not execute') #


#####################
# Statistics Module #
#####################
# The statistics module provides functions for mathematical statistics of numeric data. 
# The popular statistical functions which are defined in this module: mean, median, mode, stdev etc.
from statistics import * # import all statistics modules
ages = ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print('mean: {:.2f}'.format(mean(ages))) 
print('median: {}'.format(median(ages))) 
print('mode: {}'.format(mode(ages))) 
print('stdev: {:.2f}'.format(stdev(ages))) 


###############
# Math Module #
###############
# Module containing many mathematical operations and constants.
import math
print('math.pi:', math.pi) 						# math.pi: 3.141592653589793
print('math.sqrt(9):', math.sqrt(9)) 			# math.sqrt(9): 3.0
print('math.pow(2, 3):', math.pow(2, 3)) 		# math.pow(2, 3): 8.0
print('math.floor(9.81):', math.floor(9.81)) 	# math.floor(9.81): 9
print('math.ceil(9.81):', math.ceil(9.81)) 		# math.ceil(9.81): 10
print('math.log10(100):', math.log10(100)) 		# math.log10(100): 2.0

 
# To check what functions the module has got, we can use help(math), or dir(math). 
# This will display the available functions in the module.
# print(help(math))
# print(dir(math)) # [..., 'fabs', 'factorial', 'floor', 'fmod', ...]

# It is also possible to import multiple functions at once
from math import pi, sqrt, pow, floor, ceil, log10
print('pi:', pi) 					# pi: 3.141592653589793
print('sqrt(9):', sqrt(9)) 			# sqrt(9): 3.0
print('pow(2, 3):', pow(2, 3)) 		# pow(2, 3): 8.0
print('floor(9.81):', floor(9.81)) 	# floor(9.81): 9
print('ceil(9.81):', ceil(9.81)) 	# ceil(9.81): 10
print('log10(100):', log10(100)) 	# log10(100): 2.0

# But if we want to import all the function in math module we can use * .
from math import *
print('pi:', pi) 					# pi: 3.141592653589793
print('sqrt(9):', sqrt(9)) 			# sqrt(9): 3.0
print('pow(2, 3):', pow(2, 3)) 		# pow(2, 3): 8.0
print('floor(9.81):', floor(9.81)) 	# floor(9.81): 9
print('ceil(9.81):', ceil(9.81)) 	# ceil(9.81): 10
print('log10(100):', log10(100)) 	# log10(100): 2.0

# When we import we can also rename the name of the function.
from math import pi as PI
print('{:.2f}'.format(PI)) # 3.14


#################
# String Module #
#################
import string

print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits) # 0123456789
print(string.punctuation) # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


#################
# Random Module #
#################
# Let us import random module which gives us a random number between 0 and 0.9999.... 
# The random module has lots of functions but in this section we will only use random and randint.
from random import random, randint

print(random()) # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(1, 6)) # it returns a random integer number between [5, 20] inclusive
