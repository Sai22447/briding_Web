usernames = ['giorino','mari','joseph','josuke','kiryu']
print(len(usernames))
if len(usernames) == 0:
    print("we need to add users")
else:
    for user in range(0,len(usernames)):
        print(usernames.pop())
print("after popping out users")
print(usernames)