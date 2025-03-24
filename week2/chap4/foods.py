my_foods = ['pizza','falafel','carrot burger']
friend_foods = my_foods[:]
print(f"My food list {my_foods}")
print(f"My friend's food list {friend_foods}")
my_foods[1]='steak'
print(my_foods)
print('friend food list', friend_foods,'\n')
my_foods.append('oyakodon')
friend_foods.append('gyoza')

print(f"My food list \n{my_foods}\n")
print(f"My friend's food list \n{friend_foods}\n")