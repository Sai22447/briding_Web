"""" 3.8 """

location = ['Osaka', 'Aomori', 'Tokyo', 'Okinawa', 'Saitama']
print(sorted(location))

print(f"original list \n{location}\n")
location.reverse()
print(f"reverse order of the lsit \n{location}\n")

location.sort() #小さいやつから大きなやつ
print(f"after sroting in alphabetical order \n{location}\n")

location.sort(reverse=True) #大きなやつから小さいなやつ
print(f"after sorting with decresing order \n{location}\n")

print(f"number of places that I like to travel \n{len(location)}\n")

print(location[-1])