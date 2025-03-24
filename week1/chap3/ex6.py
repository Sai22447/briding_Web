friends = ['Lockon', 'Setsuna', 'Alleliua', 'Tieria']
print ("We got a bigger diner table")
friends.insert(3,'Exia')
friends.insert(0,'Cheridum')
friends.append('Virtue')
print(f"{friends[0]}, please join the dinner tonight.")
print(f"{friends[1]}, please join the dinner tonight.")
print(f"{friends[2]}, please join the dinner tonight.")
print(f"{friends[3]}, please join the dinner tonight.")
print(f"{friends[4]}, please join the dinner tonight.")
print(f"{friends[5]}, please join the dinner tonight.")

print("Sorry, there are only enough meal for two persons.")
print(f"{friends.pop()}, We are sorry that we can't invite you sir.")
print(f"{friends.pop()}, We are sorry that we can't invite you sir.")
print(f"{friends.pop()}, We are sorry that we can't invite you sir.")
print(f"{friends.pop()}, We are sorry that we can't invite you sir.")
print(f"{friends.pop()}, We are sorry that we can't invite you sir.")

print(f"{friends[0]}, don't worry you are still invited.")
print(f"{friends[1]}, don't worry you are still invited.")

del friends[0]
del friends[0]
print (f"After removing the guests from the list: {friends}")