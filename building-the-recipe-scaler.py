# Building the recipe scaler
# You've learned all the building blocks - now it's time to bring everything together! 
# Your recipe scaler needs to: check if you have enough ingredients in your pantry, scale the recipe for more servings, and create a shopping list for missing items. 
# The original tomato and basil pasta recipe serves 4 people, and you're hosting a party for 10.

# Your pantry has been set up as a dictionary with current quantities, and the recipe dictionary contains the base ingredient amounts. 
# The scale_factor has also been set up as party size / original serving size (10/4).

#Instructions 

# 01- Loop through the recipe dictionary to get each ingredient and amount.
shopping_list = []

# Loop through each ingredient and amount in the recipe
for ingredient, amount in recipe.items():
  print(ingredient)
  
# 02- Inside the loop, calculate the needed_amount by multiplying the amount by the scale_factor.
shopping_list = []

# Loop through each ingredient and amount in the recipe
for ingredient, amount in recipe.items():
    # Calculate the amount needed for the party
    needed_amount = amount * scale_factor;

# 03- Check if the ingredient is not in pantry OR if the needed_amount is greater than the quantity in pantry[ingredient]. If either condition is true, append the ingredient to shopping_list.
shopping_list = []

# Loop through each ingredient and amount in the recipe
for ingredient, amount in recipe.items():
    # Calculate the amount needed for the party
    needed_amount = amount * scale_factor
    
    # Check if we need to buy this ingredient
    if ingredient not in pantry or needed_amount > pantry[ingredient]:
        shopping_list.append(ingredient)

print("Shopping list for your party:")
print(shopping_list)
