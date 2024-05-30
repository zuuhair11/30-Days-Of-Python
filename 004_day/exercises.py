# 1- Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
words = ['Thirty', 'Days', 'Of', 'Python']
my_string = ' '.join(words) # Thirty Days Of Python
print(my_string)

# 2- Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
my_string = '{} {} {}'.format('Coding', 'For', 'All')
print(my_string) # Coding For All

# 3- Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

# 4- Print the variable company using print().
print(company) # Coding For All

# 5- Print the length of the company string using len() method and print().
print(len(company)) # 14

# 6- Change all the characters to uppercase letters using upper() method.
print(company.upper()) # CODING FOR ALL

# 7- Change all the characters to lowercase letters using lower() method.
print(company.lower()) # coding for all

# 8- Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize().title().swapcase()) # cODING fOR aLL

# 9- Cut(slice) out the first word of Coding For All string.
print(company[1:]) # oding For All

# 10- Check if Coding For All string contains a word Coding using the method index, find or other methods.
print('Coding' in company) # True

# 11- Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python')) # Python For All

# 12- Change Python for Everyone to Python for All using the replace method or other methods.
print('Python for %s' %('All')) # Python for Everyone

# 13- Split the string 'Coding For All' using space as the separator (split()).
print(company.split()) # ['Coding', 'For', 'All']

# 14- "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(companies.split(',')) # ['Facebook', ' Google', ' Microsoft', ' Apple', ' IBM', ' Oracle', ' Amazon']

# 15- What is the character at index 0 in the string Coding For All.
# The character at the index 0 in the string 'Coding For All' is: 'C'
print('Coding For All'[0]) # C

# 16- What is the last index of the string Coding For All.
# The last index of the string 'Coding For All' is: length of the string - 1
print(len('Coding For All') - 1) # 13
print('Coding For All'[13]) # l

# 17- What character is at index 10 in "Coding For All" string.
print('Coding For All'[10]) # ' '

# 18- Create an acronym or an abbreviation for the name 'Python For Everyone'.
phrase = 'Python For Everyone'
acronym = ''.join([word[0] for word in phrase.split()])
print(acronym) # PFE

# 19- Create an acronym or an abbreviation for the name 'Coding For All'.
first, second, third = 'Python For All'.split()
abbreviation = '{}{}{}'.format(first[0], second[0], third[0])
abbreviation = '%s%s%s' %(first[0], second[0], third[0])
print(abbreviation) # PFA

# 20- Use index to determine the position of the first occurrence of C in Coding For All.
print('Coding For All'.index('C')) # 0

# 21- Use index to determine the position of the first occurrence of F in Coding For All.
print('Coding For All'.index('F')) # 7

# 22- Use rfind to determine the position of the last occurrence of l in Coding For All People.
print('Coding For All'.rindex('l')) # 13
print(len('Coding For All')) # 14 (14 - 1) = 13

# 23- Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because')) # 31
print(sentence.index('because')) # 31

# 24- Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because')) # 47

# 25- Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# First attempt
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.replace('because because because', ''))

# Second attempt
start_index = sentence.find('because because because')
end_index = start_index + len('because because because')
print(sentence[:start_index] + sentence[end_index:]) # You cannot end a sentence with  is a conjunction

# 26- Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because')) # 31

# 27- Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.replace('because because because', '')) # You cannot end a sentence with  is a conjunction

# 28- Does ''Coding For All' start with a substring Coding?
print('Coding For All'.startswith('Coding')) # True

# 29- Does 'Coding For All' end with a substring coding?
print('Coding For All'.endswith('coding')) # False

# 30- ' Coding For All      '  , remove the left and right trailing spaces in the given string.
print('   Coding For All      '.strip()) # 'Coding For All'

# 31- Which one of the following variables return True when we use the method isidentifier():
    # 30DaysOfPython
    # thirty_days_of_python

# Because it starts with a number
print('30DaysOfPython'.isidentifier()) # False

# Correct
print('thirty_days_of_python'.isidentifier()) # True


# 32- The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libraries)) # Django# Flask# Bottle# Pyramid# Falcon


# 33- Use the new line escape sequence to separate the following sentences.
sentence = 'I am enjoying this challenge.\nI just wonder what is next.'
print(sentence) # I am enjoying this challenge.
				# I just wonder what is next.


# 34- Use a tab escape sequence to write the following lines.
print('Name\tAge\tCountry\tCity')
print('Zouhair\t26\tMorocco\tSale')

# 35- Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
print('radius = %d\narea = %.2f * radius ** %d\nThe area of a circle with radius %d is %d meters square.' %(10, 3.141592653589793238462643383279502884197, 2, 10, 314))

# 36- Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
print('{} + {} = {}'.format(8, 6, 8 + 6)) 		# 8 + 6 = 14
print('{} - {} = {}'.format(8, 6, 8 - 6)) 		# 8 - 6 = 2
print('{} * {} = {}'.format(8, 6, 8 * 6)) 		# 8 - 6 = 48
print('{} / {} = {:.2f}'.format(8, 6, 8 / 6)) 	# 8 - 6 = 1.33
print('{} % {} = {}'.format(8, 6, 8 % 6))	 	# 8 % 6 = 2
print('{} // {} = {}'.format(8, 6, 8 // 6)) 	# 8 - 6 = 1
print('{} ** {} = {}'.format(8, 6, 8 ** 6)) 	# 8 - 6 = 262144
