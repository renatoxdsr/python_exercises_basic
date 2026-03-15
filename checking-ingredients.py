# Checking ingredients
# You're building your recipe scaler for the tomato and basil pasta party! 
# Before scaling up the recipe, you need to check if you have enough of each ingredient in your pantry. 
# The ingredients_needed dictionary contains the quantities needed, and the pantry_stock dictionary contains what you currently have. 
# You'll use conditional statements to determine whether you can proceed with the full recipe, need to buy more ingredients, or should scale down the party size.

# Instructions:
# 01- Write an if statement to check if pantry_stock["tomatoes"] is greater than or equal to ingredients_needed["tomatoes"]. If true, print "Enough tomatoes for the party!".
# Check if you have enough tomatoes for the full party
if pantry_stock["tomatoes"] >= ingredients_needed["tomatoes"]:
    print("Enough tomatoes for the party!");

# 02- If the first condition is false, check if pantry_stock["tomatoes"] is greater than or equal to 800.
# Check if you have enough tomatoes for the full party
if pantry_stock["tomatoes"] >= ingredients_needed["tomatoes"]:
    print("Enough tomatoes for the party!")

# Check if you have enough for a smaller gathering
elif pantry_stock["tomatoes"] >= 800:
    print("Only enough tomatoes for a smaller gathering.")

# 03- If both conditions are false, print "Need to buy tomatoes before the party."
# Check if you have enough tomatoes for the full party
if pantry_stock["tomatoes"] >= ingredients_needed["tomatoes"]:
    print("Enough tomatoes for the party!")

# Check if you have enough for a smaller gathering
elif pantry_stock["tomatoes"] >= 800:
    print("Only enough tomatoes for a smaller gathering.")
    
# Handle the case where you need to buy more
else:
    print("Need to buy tomatoes before the party.")
