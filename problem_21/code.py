data = []
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        ingredients, rest = line.split(' (contains ')
        ingredients = set(ingredients.split(' '))
        allergens = set(rest[:-1].split(', '))
        data.append((ingredients, allergens))

# PART 1

allergen2ingredients = {}
for ingredients, allergens in data:
    for allergen in allergens:
        if allergen in allergen2ingredients:
            allergen2ingredients[allergen] = allergen2ingredients[allergen] & ingredients
        else:
            allergen2ingredients[allergen] = ingredients

# Logically reduce one by one
while not all(len(ingredients) == 1 for ingredients in allergen2ingredients.values()):
    for alergen, ingredients in allergen2ingredients.items():
        if len(ingredients) == 1:
            for a2, i2 in allergen2ingredients.items():
                if alergen == a2:
                    continue
                allergen2ingredients[a2] = i2 - ingredients


all_ingredients = {ingredient for ingredients, allergens in data for ingredient in ingredients}
ingredients_with_allergen = {ingredient for ingredients in allergen2ingredients.values() for ingredient in ingredients}
ingredients_without_allergen = all_ingredients - ingredients_with_allergen

print(len([ingredient for ingredients, allergens in data for ingredient in ingredients if ingredient in ingredients_without_allergen]))

# PART 2
print(','.join([ing for ings in list(zip(*sorted(allergen2ingredients.items())))[1] for ing in ings]))
