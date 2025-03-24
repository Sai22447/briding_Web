horses = ['Mihono Bourbon', 'Durendel', 'Buena Vista']
horses[0] = 'T.M Opera O'
print (horses)

horses.append('Mihono Bourbon')
print (horses)

horses.insert(0, 'Narita Top Road')
print (horses)

horses.insert(3, 'Seeking The Pearl')
print (horses)

del horses[3]
print (horses)

print ("pop method")
popped_horses = horses.pop()
print (f"b4 {horses}")
print (f"after {popped_horses}")
