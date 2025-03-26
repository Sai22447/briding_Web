buffet_foods = ('seafood','sushi','tempura','gyoza')

print("\nIn this buffet restaurant, we offers\n")
for food in buffet_foods:
    print(food.title())

#buffet_foods[0]='chicken wings'
buffet_foods = ('seafood','sushi','tempura','gyoza','bacon','fish and chips')
print("\nRevised Menu\n")
for ind, food in enumerate(buffet_foods):
    print(ind,food)
    
