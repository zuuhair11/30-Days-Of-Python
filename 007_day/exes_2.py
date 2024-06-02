# Exercises: Level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# 1- Join A and B
ab = A.union(B)
print(ab) # {19, 20, 22, 24, 25, 26, 27, 28}

# 2- Find A intersection B
# Basically return a set of items which are in both A and B
all_intersection = A.intersection(B)
print(all_intersection) # {19, 20, 22, 24, 25, 26}

# 3- Is A subset of B
# Basically saying if A is the son of the B, (B has a lot of items and includes A)
print(A.issubset(B)) # True

# 4- Are A and B disjoint sets
# If two sets do not have a common item/items we call them disjoint sets
print(A.isdisjoint(B)) # False

# 5- Join A with B and B with A
A.update(B)
B.update(A)

print(A) # {19, 20, 22, 24, 25, 26, 27, 28}
print(B) # {19, 20, 22, 24, 25, 26, 27, 28}

# 6- What is the symmetric difference between A and B
# Basically saying return numbers that are not shared between the two sets
print(A.symmetric_difference(B)) # set()

# 7- Delete the sets completely
del A, B
