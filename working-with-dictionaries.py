# Working with dictionaries
# So far, you've added the ingredients with their quantities in grams.

# Now, you want to practice accessing the dictionary's contents using different methods to confirm the dictionary is set up as expected, and to prepare for scaling later on.

# Instructions:

# Use a method to retrieve all the keys from the recipe dictionary and assign the result to ingredient_names.
# Get all ingredient names
ingredient_names = recipe.keys();

# Use a method to retrieve all the values from the recipe dictionary and assign the result to quantities.
# Get all quantities
quantities = recipe.values();

# Use a method to retrieve all key-value pairs from the recipe dictionary and assign the result to recipe_items.
# Get all key-value pairs
recipe_items = recipe.items();

print("Ingredient names:", ingredient_names)
print("Quantities:", quantities)
print("Recipe items:", recipe_items)
