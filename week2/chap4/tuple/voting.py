print("Age check clock")
age = int(input("enter your age: "))
if age >= 18:
    print("It is legal age")
    print("You're safe, for now")
else:
    print(f"{18-age} years left till legal")
    print("Calling the FBI")