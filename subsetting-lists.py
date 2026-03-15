# Subsetting lists
# Now that you have your recipe scaler set up with the two lists (ingredients and quantities), you want to create a quick preview of your shopping list. 
# You'll need to access specific items from your lists to display the first few ingredients and their amounts, as well as check what the last item on your list is.

# Instructions: 3/3

# 1- Access the second ingredient from the ingredients list and assign it to second_ingredient.
ingredients = ["fusilli", "tomatoes", "garlic", "basil", "olive oil", "salt"]
quantities = [500, 400, 15, 20, 30, 10]

# Get the second ingredient for your preview
second_ingredient = ingredients[1];

print(second_ingredient)

# 2- Get the last item from the quantities list using slice notation and assign it to last_quantity.
ingredients = ["fusilli", "tomatoes", "garlic", "basil", "olive oil", "salt"]
quantities = [500, 400, 15, 20, 30, 10]

# Extract the last quantity
last_quantity = quantities[-1];

print(last_quantity)

# 3- Extract every other element from the ingredients list, starting with the first and assigning it to alternate_ingredient.
ingredients = ["fusilli", "tomatoes", "garlic", "basil", "olive oil", "salt"]
quantities = [500, 400, 15, 20, 30, 10]

# Get every other ingredient starting from the first
alternate_ingredient = ingredients[0::2]

print(alternate_ingredient)


