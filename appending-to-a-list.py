# Appending to a list
# You want to test out the shopping list feature for your recipe scaler. 
# Before scaling anything, you want to check which ingredients you don't have enough of in your pantry. 
# You'll loop through the standard recipe dictionary and the items you have in your pantry_stock and add any ingredient to your shopping list where the required amount exceeds what you currently have available.

# Instructions:
# Create an empty list called shopping_list to store ingredients you need to buy.
# Loop through the items in the recipe dictionary to access both ingredient names and required quantities.
# Inside the loop, check if the required_qty is greater than what you have in pantry_stock for that ingredient.
# If you need more of an ingredient, append the ingredient name to shopping_list using the .append() method.

# Create an empty shopping list
shopping_list = [];

# Loop through each ingredient and required quantity
for ingredient, required_qty in recipe.items():
    # Check if we need more than what we have
    if required_qty > pantry_stock[ingredient]:
        # Add the ingredient to our shopping list
        shopping_list.append(ingredient);

# Display the shopping list
print("Shopping list:", shopping_list)
