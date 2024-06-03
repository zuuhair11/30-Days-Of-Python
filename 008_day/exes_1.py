# 1- Create an empty dictionary called dog
dog = {}
dog = dict()

# 2- Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Jack'
dog['color'] = 'White'
dog['breed'] = 'Male'
dog['legs'] = 4
dog['age'] = 5

# 3- Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Zouhair',
    'last_name': 'Sahtout',
    'gender': 'Male',
    'age': 27,
    'marital status': 'Single',
    'skills': ['JavaScript', 'Python'],
    'country': 'Localhost',
    'city': '127.0.0.1',
    'address': '11 ELEVEN'
}

# 4- Get the length of the student dictionary
length = len(student)
print(length) # 9

# 5- Get the value of skills and check the data type, it should be a list
skills = student['skills']
skills = student.get('skills')
print(type(skills)) # <class 'list'>

# 6- Modify the skills values by adding one or two skills
student['skills'].append('MongoDB')
student.get('skills').append('MySQL')
student['skills'].extend(['Test', 'Another test'])
print(student['skills']) # ['JavaScript', 'Python', 'MongoDB', 'MySQL', 'Test', 'Another test']

# 7- Get the dictionary keys as a list
dict_keys = list(student.keys())
print(dict_keys) # ['first_name', 'last_name', 'gender', 'age', 'marital status',...]

# 8- Get the dictionary values as a list
dict_values = list(student.values())
print(dict_values) # ['Zouhair', 'Sahtout', 'Male', 27, 'Single', ['JavaScript', 'Python', ...], ...]

# 9- Change the dictionary to a list of tuples using items() method
list_of_tuples = list(student.items())
print(list_of_tuples) # [('first_name', 'Zouhair'), ('last_name', 'Sahtout'), ...]

# 10- Delete one of the items in the dictionary
# Will return the key's value was deleted
item_deleted = student.pop('marital status')
print(item_deleted) # Single

# Second attempt
del student['country']

# Third attemp
# Delete the last one
item_deleted = student.popitem()
print(item_deleted) # ('address', '11 ELEVEN')

# 11- Delete one of the dictionaries
del dog
