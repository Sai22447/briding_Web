players = ['charlie','martha','wilson','alex','fiorayne']

for player in players:
    print(player.title())
print("The End")

print(players[0:2]) #starting at index 0 and stops at index 2(0,1)
print(players[1:4])
print(players[3:]) 
print(players[:2])
print(players[-3:])

print(players)
print("Here are my team members")
for player in players[:3]:
    print(player.title())
    
print("end")    