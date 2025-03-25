banned_users=('char','shiroko','hamman','reborns')
user = 'char'
if user not in banned_users:
    print(f"Welcome {user.title()}, you can access the system")
else:
    print("Sorry bud you ain't invited")