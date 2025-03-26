requested_toppings = ['mushroom','bacon','cheese']
for topping in requested_toppings:
    if topping == 'mushroom':
        print("sorry we are out of mushroom for the time being")
    else:
        print(f"adding {topping}")
print('\n')
available_toppings = ['shrimp','chicken','green peppers','bacon','cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"{requested_topping} is available")
    else:
        print(f"Sorry, {requested_topping} is not available")