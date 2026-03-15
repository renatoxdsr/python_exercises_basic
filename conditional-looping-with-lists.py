# Conditional looping with lists
# Before you scale your tomato and basil pasta recipe for the party, you need to inspect the ingredient quantities to understand what you're working with. Your recipe quantities are stored in a list called quantities (measured in grams). As a first step in building your recipe scaler, you'll loop through these quantities and use conditionals to categorize them - but you won't scale them yet. 
# This helps you understand the ingredient distribution before making any changes.

# Instructions
# Loop through each quantity in the quantities list using qty as your iterator variable.
# Inside the loop, add a conditional that checks if the qty is greater than or equal to 400 grams. If so, print 'Large quantity'.
# Add an elif condition to check if the qty is greater than or equal to 200 grams. If so, print 'Medium quantity'.
# Add an else clause to handle all remaining quantities and print 'Small quantity'

quantities = [500, 400, 20, 15, 15, 7]

# Loop through each quantity in the recipe
for qty in quantities:
    # Check if it's a large quantity (400g or more)
    if qty >= 400:
        print('Large quantity')
    # Check if it's a medium quantity (200g or more)
    elif qty >= 200:
        print('Medium quantity')
    # Otherwise it's a small quantity
    else:
        print('Small quantity')

  
