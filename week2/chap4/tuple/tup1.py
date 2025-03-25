#immutable object aka can't change the list
dimensions =(200,50)
print(dimensions[0])
print(dimensions[1])
#dimensions[1]=69

my_t=(500,)
print(type(my_t))

print("original dimension")
for dimension in dimensions:
    print(dimension)
    
dimensions =(1360,720)
print("modified dimension")
for dimension in dimensions:
    print(dimension)
    
