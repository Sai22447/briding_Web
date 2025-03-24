""" 4-7, threes: make a lsit of the multples of 3 up to 30"""

threes = list(range(3,31,3))
for three in threes:
    print(three)
   
cubes =[] 
for value in range(1,12):
    cubes.append(value**3)
print("first ten cubes")
print(cubes)

cube_list = [value ** 3 for value in range(1,11)]
print(cube_list)