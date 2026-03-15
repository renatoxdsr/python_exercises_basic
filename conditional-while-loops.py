# Conditional while loops
# Your recipe scaler needs to verify that you have enough of each ingredient before scaling up the recipe. 
# You'll use a while loop combined with conditional logic to check ingredient quantities and provide helpful status updates. 
# You have a variable ingredients_checked that tracks how many ingredients you've verified, and total_ingredients representing the total number of ingredients in your tomato and basil pasta recipe.

# Instructions
# Create a while loop that continues as long as ingredients_checked is less than total_ingredients.
# Increase the ingredients_checked counter by 1 each time the loop runs.
# Using conditional statements, check whether fewer than 4 ingredients have been reviewed.
# If not, check whether 6 or fewer ingredients have been reviewed.

total_ingredients = 7
ingredients_checked = 0

# Set up the loop
while ingredients_checked < total_ingredients:
    # Increment the counter
    ingredients_checked += 1
    # Check if less than 4 ingredients reviewed
    if ingredients_checked < 4:
        print("More than half remaining")
    # Check if 6 or fewer ingredients reviewed
    elif ingredients_checked <= 6:
        print("Nearly finished checking")
    else:
        print("All ingredients verified!")
