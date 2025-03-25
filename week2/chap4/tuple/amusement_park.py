print("Age check for amusement park")
age = int(input("Please enter your age: "))

if age < 5:
    print("Admission cost is free")
elif age < 18:
    print("Admission cost is $10")
else:
    print("Admission cost is $16")