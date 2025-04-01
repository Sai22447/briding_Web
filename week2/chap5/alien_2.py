alien_0= {'x_position':0, 'y_position':25, 'speed':'medium'}
#move the alien to the right based on the speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position']=alien_0['x_position']+ x_increment
print(alien_0)

print(f"before deleting {alien_0}")

del alien_0['speed']
print(f"after deleting {alien_0}")
